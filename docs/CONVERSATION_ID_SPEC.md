# x-ara-conversation-id — UUID Sanitization Specification

## Overview

The `x-ara-conversation-id` header ties every Anthropic API request to the Ara conversation that produced it. This document specifies why the ID must be passed explicitly (never auto-generated at the call site), the exact format it must conform to, how each Ara surface must sanitize it before sending, and the canonical test vectors every implementation must pass.

---

## 1. Why the ID must be passed explicitly

### 1.1 Traceability across surfaces

Ara runs on three surfaces — AraDesktop (Swift/macOS), AraWeb (Next.js), and AraAPI (Bun + Hono). All three ultimately call Anthropic's Messages API. For usage analytics, billing attribution, rate-limit debugging, and conversation replay, every Anthropic request that belongs to the same Ara conversation must carry the same identifier.

If each call site auto-generated its own ID (e.g. `UUID()` in Swift or `crypto.randomUUID()` in TypeScript), requests within a single Ara conversation would carry different identifiers and become untraceable.

### 1.2 AnthropicMessagesClient and AnthropicMessagesSender are not the source of truth

`AnthropicMessagesClient` (AraDesktop) and `AnthropicMessagesSender` (AraAPI / AraWeb backend) are transport-layer components. They know how to form and sign an HTTP request, but they have no access to Ara's conversation model. The conversation ID lives one layer up — in the session store, the conversation view-model, or the API request context — and must be threaded down to the transport explicitly.

Concretely:

- `AnthropicMessagesClient` must accept a `conversationID: String` parameter and sanitize it to a valid UUID before placing it in the `x-ara-conversation-id` header. It must **never** fall back to generating a fresh UUID when the caller omits or passes an invalid value; instead it must surface an error or warning so the bug is caught at development time.
- `AnthropicMessagesSender` must accept an equivalent `conversationId: string` parameter, apply the same sanitization, and forward the sanitized value in the header. Any request arriving without a valid UUID must be rejected with a structured log warning before the outbound HTTP call is made.

### 1.3 Sanitization is the transport layer's responsibility

The caller may pass a value that looks like a UUID but was constructed from user-supplied text, a legacy identifier, or a database row ID that predates the UUID requirement. The transport components are the last line of defense before the header hits the wire. Centralizing the sanitization check there means no surface can accidentally bypass it.

---

## 2. UUID format and sanitization rules

### 2.1 Accepted format

Only RFC 4122 UUID v1 and v4 strings are accepted. The canonical textual representation is:

```
xxxxxxxx-xxxx-Mxxx-Nxxx-xxxxxxxxxxxx
```

where:

- Each `x` is a lowercase hexadecimal digit (0–9, a–f).
- `M` is `1` (v1) or `4` (v4).
- `N` is one of `8`, `9`, `a`, or `b` (variant bits `10xx`).
- The string is exactly 36 characters including four hyphens.

The regex that must be satisfied:

```
^[0-9a-f]{8}-[0-9a-f]{4}-[14][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$
```

### 2.2 Sanitization algorithm

1. **Trim** leading and trailing whitespace from the input string.
2. **Lowercase** the result (UUIDs from some systems arrive in uppercase).
3. **Match** against the regex above.
4. If the match **succeeds**, use the sanitized string as the header value.
5. If the match **fails**, emit a structured warning log (see §2.3) and do one of:
   - Throw / return an error so the caller can decide how to proceed (preferred for server-side senders).
   - Drop the header entirely and proceed without it (acceptable for client-side callers when a missing ID is preferable to a corrupted one, but the warning must still fire).

Under no circumstances should a transport component silently generate a replacement UUID.

### 2.3 Warning log format

Every rejection must produce a structured log entry that includes:

- The invalid value (truncated to 64 chars to avoid log injection).
- The call site (function name / file / line where available).
- A human-readable reason, e.g. `"x-ara-conversation-id rejected: value is not a RFC 4122 UUID v1/v4"`.

---

## 3. Code examples

### 3.1 Swift — AraDesktop

#### Sanitization utility

```swift
import Foundation
import os.log

private let logger = Logger(subsystem: "so.ara.desktop", category: "AnthropicMessagesClient")

/// Returns the input if it is a valid RFC 4122 UUID v1 or v4, otherwise returns nil
/// and emits a warning on the provided logger.
func sanitizeConversationID(_ raw: String?) -> String? {
    guard let raw else {
        logger.warning("x-ara-conversation-id: nil value received, header will be omitted")
        return nil
    }
    let trimmed = raw.trimmingCharacters(in: .whitespaces).lowercased()
    let pattern = #"^[0-9a-f]{8}-[0-9a-f]{4}-[14][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$"#
    guard trimmed.range(of: pattern, options: .regularExpression) != nil else {
        let truncated = String(trimmed.prefix(64))
        logger.warning(
            "x-ara-conversation-id rejected: '\(truncated)' is not a RFC 4122 UUID v1/v4"
        )
        return nil
    }
    return trimmed
}
```

#### AnthropicMessagesClient usage

```swift
struct AnthropicMessagesClient {
    let session: URLSession
    let apiKey: String

    func sendMessage(
        request: MessagesRequest,
        conversationID: String?
    ) async throws -> MessagesResponse {
        var urlRequest = URLRequest(url: anthropicEndpoint)
        urlRequest.httpMethod = "POST"
        urlRequest.setValue("Bearer \(apiKey)", forHTTPHeaderField: "Authorization")
        urlRequest.setValue("application/json", forHTTPHeaderField: "Content-Type")

        if let sanitized = sanitizeConversationID(conversationID) {
            urlRequest.setValue(sanitized, forHTTPHeaderField: "x-ara-conversation-id")
        }
        // If sanitization fails the header is omitted; the warning is already logged.

        urlRequest.httpBody = try JSONEncoder().encode(request)
        let (data, _) = try await session.data(for: urlRequest)
        return try JSONDecoder().decode(MessagesResponse.self, from: data)
    }
}
```

#### Passing the ID from a conversation view-model

```swift
class ConversationViewModel: ObservableObject {
    let conversation: Conversation  // owns the stable UUID
    let client: AnthropicMessagesClient

    func send(userMessage: String) async {
        do {
            let response = try await client.sendMessage(
                request: buildRequest(userMessage),
                conversationID: conversation.id.uuidString  // pass the stable UUID here
            )
            await MainActor.run { self.append(response) }
        } catch {
            // handle
        }
    }
}
```

---

### 3.2 TypeScript — AraWeb and AraAPI

#### Sanitization utility (shared, e.g. `lib/conversationId.ts`)

```typescript
const UUID_V1_V4_RE =
  /^[0-9a-f]{8}-[0-9a-f]{4}-[14][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$/;

/**
 * Returns the sanitized UUID string if valid, otherwise logs a warning and
 * returns null. Never generates a replacement UUID.
 */
export function sanitizeConversationId(
  raw: string | undefined | null,
  callSite?: string
): string | null {
  if (raw == null || raw === "") {
    console.warn(
      `[x-ara-conversation-id] ${callSite ?? "unknown"}: value is absent, header will be omitted`
    );
    return null;
  }
  const trimmed = raw.trim().toLowerCase();
  if (!UUID_V1_V4_RE.test(trimmed)) {
    console.warn(
      `[x-ara-conversation-id] ${callSite ?? "unknown"}: ` +
        `rejected "${trimmed.slice(0, 64)}" — not a RFC 4122 UUID v1/v4`
    );
    return null;
  }
  return trimmed;
}
```

#### AnthropicMessagesSender — AraAPI (Bun + Hono)

```typescript
// src/senders/AnthropicMessagesSender.ts
import Anthropic from "@anthropic-ai/sdk";
import { sanitizeConversationId } from "@/lib/conversationId";

export class AnthropicMessagesSender {
  private client: Anthropic;

  constructor(apiKey: string) {
    this.client = new Anthropic({ apiKey });
  }

  async send(
    params: Anthropic.MessageCreateParamsNonStreaming,
    conversationId: string | undefined
  ): Promise<Anthropic.Message> {
    const sanitized = sanitizeConversationId(conversationId, "AnthropicMessagesSender.send");

    const extraHeaders: Record<string, string> = sanitized
      ? { "x-ara-conversation-id": sanitized }
      : {};

    return this.client.messages.create(params, {
      headers: extraHeaders,
    });
  }
}
```

#### Wiring in a Hono route handler

```typescript
// src/routes/chat.ts
import { Hono } from "hono";
import { AnthropicMessagesSender } from "@/senders/AnthropicMessagesSender";

const app = new Hono();
const sender = new AnthropicMessagesSender(process.env.ANTHROPIC_API_KEY!);

app.post("/chat", async (c) => {
  const { messages, conversationId } = await c.req.json<{
    messages: unknown[];
    conversationId?: string;
  }>();

  const reply = await sender.send(
    { model: "claude-opus-4-5", max_tokens: 1024, messages: messages as any },
    conversationId   // threaded from the caller; sanitized inside the sender
  );

  return c.json(reply);
});
```

#### AraWeb — Next.js API route

```typescript
// app/api/chat/route.ts
import { NextRequest, NextResponse } from "next/server";
import { sanitizeConversationId } from "@/lib/conversationId";
import Anthropic from "@anthropic-ai/sdk";

const anthropic = new Anthropic();

export async function POST(req: NextRequest) {
  const body = await req.json();
  const rawId = body.conversationId as string | undefined;

  const sanitized = sanitizeConversationId(rawId, "POST /api/chat");

  const message = await anthropic.messages.create(
    {
      model: "claude-opus-4-5",
      max_tokens: 1024,
      messages: body.messages,
    },
    {
      headers: sanitized ? { "x-ara-conversation-id": sanitized } : {},
    }
  );

  return NextResponse.json(message);
}
```

---

## 4. Test vectors

All implementations must pass the following test vectors. The suite should live alongside the sanitization utility in each surface's test target.

### 4.1 Valid inputs — must be accepted and returned unchanged (after lowercasing)

| Input | Notes |
|---|---|
| `550e8400-e29b-41d4-a716-446655440000` | UUID v1, all lowercase |
| `550E8400-E29B-41D4-A716-446655440000` | UUID v1, uppercase — must be lowercased to `550e8400-e29b-41d4-a716-446655440000` |
| `f47ac10b-58cc-4372-a567-0e02b2c3d479` | UUID v4 |
| `F47AC10B-58CC-4372-A567-0E02B2C3D479` | UUID v4, uppercase — must be lowercased |
| `00000000-0000-1000-8000-000000000000` | UUID v1, minimal variant |
| `ffffffff-ffff-4fff-bfff-ffffffffffff` | UUID v4, all-f body |

### 4.2 Invalid inputs — must be rejected with a warning and return nil / null

| Input | Reason for rejection |
|---|---|
| `""` | Empty string |
| `"not-a-uuid"` | Arbitrary string |
| `"550e8400-e29b-41d4-a716-44665544000"` | 35 chars — one digit short |
| `"550e8400-e29b-41d4-a716-4466554400000"` | 37 chars — one digit long |
| `"550e8400-e29b-21d4-a716-446655440000"` | Version nibble `2` — not v1 or v4 |
| `"550e8400-e29b-41d4-c716-446655440000"` | Variant nibble `c` — not `8/9/a/b` |
| `"550e8400e29b41d4a716446655440000"` | Missing hyphens |
| `"550e8400-e29b-41d4-a716-44665544000g"` | Non-hex character `g` |
| `"  "` | Whitespace only |
| `null` / `nil` / `undefined` | Absent value |
| `"conversation-abc-123"` | Legacy non-UUID Ara ID format |
| `"<script>alert(1)</script>"` | Injection attempt |

### 4.3 Swift test example

```swift
import XCTest

final class ConversationIDTests: XCTestCase {
    func testValidV4UUID() {
        XCTAssertEqual(
            sanitizeConversationID("f47ac10b-58cc-4372-a567-0e02b2c3d479"),
            "f47ac10b-58cc-4372-a567-0e02b2c3d479"
        )
    }

    func testUppercaseIsNormalized() {
        XCTAssertEqual(
            sanitizeConversationID("F47AC10B-58CC-4372-A567-0E02B2C3D479"),
            "f47ac10b-58cc-4372-a567-0e02b2c3d479"
        )
    }

    func testInvalidVersionNibble() {
        XCTAssertNil(sanitizeConversationID("550e8400-e29b-21d4-a716-446655440000"))
    }

    func testNilInput() {
        XCTAssertNil(sanitizeConversationID(nil))
    }

    func testLegacyAraID() {
        XCTAssertNil(sanitizeConversationID("conversation-abc-123"))
    }
}
```

### 4.4 TypeScript test example (Bun test runner)

```typescript
import { describe, expect, test } from "bun:test";
import { sanitizeConversationId } from "@/lib/conversationId";

describe("sanitizeConversationId", () => {
  test("accepts valid v4 UUID", () => {
    expect(sanitizeConversationId("f47ac10b-58cc-4372-a567-0e02b2c3d479")).toBe(
      "f47ac10b-58cc-4372-a567-0e02b2c3d479"
    );
  });

  test("lowercases uppercase input", () => {
    expect(sanitizeConversationId("F47AC10B-58CC-4372-A567-0E02B2C3D479")).toBe(
      "f47ac10b-58cc-4372-a567-0e02b2c3d479"
    );
  });

  test("rejects version nibble 2", () => {
    expect(sanitizeConversationId("550e8400-e29b-21d4-a716-446655440000")).toBeNull();
  });

  test("rejects bad variant nibble", () => {
    expect(sanitizeConversationId("550e8400-e29b-41d4-c716-446655440000")).toBeNull();
  });

  test("rejects missing hyphens", () => {
    expect(sanitizeConversationId("550e8400e29b41d4a716446655440000")).toBeNull();
  });

  test("rejects null", () => {
    expect(sanitizeConversationId(null)).toBeNull();
  });

  test("rejects legacy Ara ID", () => {
    expect(sanitizeConversationId("conversation-abc-123")).toBeNull();
  });

  test("rejects empty string", () => {
    expect(sanitizeConversationId("")).toBeNull();
  });
});
```

---

## 5. Summary of rules

- Pass `conversationID` / `conversationId` explicitly from the conversation model — never generate it at the transport layer.
- Sanitize in `AnthropicMessagesClient` (Swift) and `AnthropicMessagesSender` / API route handlers (TypeScript) before the header is set.
- Accept only RFC 4122 UUID v1 and v4 in lowercase canonical form (36 chars, 4 hyphens).
- On rejection: log a structured warning, omit the header or propagate an error — do not silently substitute a new UUID.
- All test vectors in §4 must pass in every surface's test suite.
