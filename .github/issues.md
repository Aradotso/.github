# Initial Tracked Work & Issues

These issues map to the current priorities defined in ROADMAP.md.

## Issues List

### 1. [FEATURE] Implement Lazy-Created git worktrees in desktop UI
* **Description**: Delay git worktree creation until the first chat prompt is submitted or when a background task actually triggers. This eliminates upfront workspace preparation latency.
* **Milestone**: Milestone 1: Lazy-Loaded Workspace Worktrees
* **Labels**: `enhancement`, `worktree`, `p1`

### 2. [FEATURE] Proactive "New Chat" suggestion engine synthesis
* **Description**: Create a background daemon that synthesizes recent workspace signals, git diffs, session history, and user memories to formulate actionable starting prompt cards for a new session.
* **Milestone**: Milestone 2: Proactive "New Chat" Suggestion Engine
* **Labels**: `enhancement`, `suggestions`, `p2`

### 3. [BUG] Custom scaling omissions on multi-display sweep-display-sizes
* **Description**: Address situations where scaling is native (scaling:off) or completely omitted in displayplacer lists. Robustly parse the scaling output to prevent coordinate calculation mismatches in browser automation.
* **Milestone**: Milestone 4: Multi-Display & UI Layout Optimization
* **Labels**: `bug`, `cua`, `p1`

### 4. [FEATURE] Validate and sanitize custom conversation ID headers in AraWeb Gateway
* **Description**: Ensure `x-ara-conversation-id` header is correctly propagated from AnthropicMessagesClient/Sender, checking that any special value keys are correctly validated as UUIDs to prevent log spoofing or injection.
* **Milestone**: Milestone 3: Secure & Validated Gateway Propagation
* **Labels**: `enhancement`, `gateway`, `p2`
