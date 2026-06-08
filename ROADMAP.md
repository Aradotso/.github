# Ara Roadmap

This document outlines the milestones and roadmap for Ara, focusing on enhancing agent execution, desktop integration, workspace scaling, and robust gateway communication.

## Milestones

### Milestone 1: Lazy-Loaded Workspace Worktrees (Q2 2026)
Improve startup speed and client responsiveness by delaying the generation of isolated git worktrees until the first task execution or message submission.
- Optimize background session initialization time.
- Implement lazy-creation logic for background throwaway slots in the desktop UI.
- Maintain a local pool of ready-to-use temporary slots to eliminate latency when execution begins.

### Milestone 2: Proactive "New Chat" Suggestion Engine (Q3 2026)
Leverage historical sessions, active git state, user memory, and local macOS desktop signals to generate contextual, high-confidence chat suggestions.
- Implement Ara-CUA (Computer Use Agent) desktop event indexing.
- Synthesize recent coding context to formulate actionable suggestion cards with confidence ratings ranging from 0.65 to 0.95+.
- Expose suggestions dynamically via the dashboard interface on application start.

### Milestone 3: Secure & Validated Gateway Propagation (Q3 2026)
Ensure consistent and verified message routing and authorization tracing throughout the AraWeb Gateway.
- Implement strict UUID validation and sanitization for custom communication headers.
- Propagate `x-ara-conversation-id` securely within AnthropicMessagesClient and AnthropicMessagesSender pipelines.
- Verify tracing endpoints in high-throughput production environments.

### Milestone 4: Multi-Display & UI Layout Optimization (Q4 2026)
Further enhance local browser automation and native display handling on macOS.
- Expand sweep-display-sizes to handle diverse high-density multi-display topologies automatically.
- Prevent layout flicker and improve layout-restoration logic under fast workspace transitions.
- Resolve custom multi-display resolution mapping when native scaling is turned off or omitted.
