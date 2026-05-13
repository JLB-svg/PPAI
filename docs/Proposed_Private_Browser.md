# PPAI-Brain Secure Private Directory Browser Specification

**Document:** `SECURE_PRIVATE_BRAIN_DIRECTORY_BROWSER_v1.1.md`  
**Version:** 1.1  
**Date:** May 12, 2026  
**Status:** Approved for Immediate Implementation  
**Author:** Grok (xAI) on behalf of PPAI Core  
**Previous Version:** v1.0  
**References:** `BRAIN_ENVIRONMENT_ARCHITECTURE_v2.0.md`, `ARCHITECTURE_v2.0.md`, `LOCAL_ENVIRONMENT_v1.1.md`  
**Purpose:** Enable secure, read-only, web-style browsing of the entire `PPAI-Brain/` directory during Termux bootstrap and beyond, exclusively for trusted AI collaboration (Grok).

---

## TL;DR / Executive Summary

This specification defines a **minimal, private, encrypted backend feature** that exposes the `PPAI-Brain/` directory as a clean, navigable website-style directory listing. 

The service is **strictly read-only**, scoped exclusively to the brain root, and accessible only via end-to-end encrypted private tunnels (Tailscale preferred). It allows Grok to inspect project structure, source files, logs, and configuration exactly as if browsing a directory on a website — without any manual copy-paste, SSH, or exposure of the host device.

**Key simplification in v1.1**: Replaced FastAPI + Uvicorn with a **single pure-stdlib Python script** (`http.server` + custom handler). This eliminates all external dependencies, reduces complexity, improves startup time and resource usage on the Pixel 6 Pro, and further strengthens sovereignty and anti-vibe-coding principles while preserving 100% of the original functionality.

The implementation lives entirely inside `PPAI-Brain/`, adds negligible complexity during the Android/Termux bootstrap phase, and migrates unchanged into the full Nix + Bubblewrap environment.

---

## Table of Contents

- [TL;DR / Executive Summary](#tldr--executive-summary)
- [Goals & Non-Goals](#goals--non-goals)
- [Security & Threat Model](#security--threat-model)
- [High-Level Design](#high-level-design)
- [Implementation Details](#implementation-details)
- [Tunneling & Private Access](#tunneling--private-access)
- [Usage Protocol with Grok](#usage-protocol-with-grok)
- [Trade-offs & Mitigations](#trade-offs--mitigations)
- [Migration Path & Future Evolution](#migration-path--future-evolution)
- [Verification & Acceptance Criteria](#verification--acceptance-criteria)
- [Next Steps](#next-steps)

---

## Goals & Non-Goals

**Goals**
- Provide a clean, web-like directory browsing experience for the complete `PPAI-Brain/` folder.
- Maintain absolute privacy and encryption at all times (private-only, never public).
- Zero structural changes to the brain directory; fully portable and reproducible.
- **Minimalism**: Single pure-Python stdlib file, no external runtime dependencies.
- Enable fast, interactive collaboration with Grok during development without friction.
- Serve as a reusable pattern for future secure internal services.

**Non-Goals**
- Public or unauthenticated access of any kind.
- Write, delete, or execute capabilities.
- Exposure of any files outside the `PPAI-Brain/` root.
- Complex UI/UX beyond clean directory listings and safe file previews.
- Permanent background daemon (must be explicitly started and stopped).

---

## Security & Threat Model

- **Strict scoping**: All paths are canonicalized with `pathlib` and must be prefixed with the brain root. Any attempt to escape (`..`, absolute paths, symlinks outside brain) is rejected with 403.
- **Read-only**: No filesystem modifications, no shell execution.
- **Authentication**: Optional token-based auth via query parameter or HTTP Basic Auth (secret stored in `config/secrets/` — never committed).
- **Network**: Listens **only** on `127.0.0.1`; never binds to `0.0.0.0`.
- **Encryption**: All external access occurs exclusively over private encrypted tunnels (Tailscale WireGuard or Cloudflare Tunnel with Zero Trust).
- **Logging**: All access and errors logged to `logs/secure-browser/` inside the brain.
- **Air-gap compatibility**: Service can be disabled entirely when fully air-gapped.

---

## High-Level Design

The feature consists of three lightweight components, all housed inside `PPAI-Brain/`:

1. **Single pure-Python backend** (`src/ppai/backend/secure_browser.py`)
2. **Activation & control script** (`start-private-browser.sh`)
3. **Private tunneling layer** (Tailscale or Cloudflare Tunnel)

The backend uses Python’s standard library `http.server` with a custom `SecureBrainDirectoryHandler` for full control over security and presentation.

---

## Implementation Details

### 1. Backend Service (`src/ppai/backend/secure_browser.py`)
- **Pure stdlib only** — no external packages.
- Subclasses `http.server.SimpleHTTPRequestHandler` (or `ThreadingHTTPServer` for better concurrency).
- Single mount point: `/browse/` (and subpaths).
- Clean HTML directory index with:
  - Breadcrumb navigation
  - Table (name, size, last modified, type)
  - Inline CSS (no external assets)
- Safe file preview:
  - Text, Markdown, Python, JSON, etc. rendered with `<pre><code>` (basic syntax-aware via content-type).
  - `/browse/<path>?raw=1` or `/raw/<path>` for plain text download/view.
  - Binary files served as downloadable attachments only.
- Full path validation and escaping protection.
- Optional JSON mode (`?format=json`).
- Logging to brain-internal directory.
- \~200 lines total (including generous comments).

### 2. Activation Script (`start-private-browser.sh`)
- Located at brain root.
- Sources `activate.sh` to enter the Python venv.
- Starts the server: `python -m src.ppai.backend.secure_browser`
- Configurable port and token via `config.yaml`.
- Displays clear instructions for starting the tunnel.
- Graceful shutdown on Ctrl+C.

### 3. Configuration
- Port, auth token (if used), and log level in `config.yaml`.
- Secrets kept in `config/secrets/` (git-ignored).

---

## Tunneling & Private Access

**Preferred Option – Tailscale** (sovereignty-aligned):  
Install official Tailscale Android app, join private tailnet. Service reachable at `http://<tailscale-ip>:8080/browse/`.

**Alternative – Cloudflare Tunnel** (fast bootstrap):  
`pkg install cloudflared` → one-command tunnel with Zero Trust.

Both require zero port forwarding.

---

## Usage Protocol with Grok

1. Run `./start-private-browser.sh`.
2. Start the chosen tunnel.
3. Send the private URL to Grok (e.g., `http://100.x.x.x:8080/browse/` or Cloudflare URL).
4. Grok uses its `browse_page` tool to navigate the brain exactly like a website.
5. Stop the service when finished (`Ctrl+C`).

No credentials or sensitive data are transmitted in chat.

---

## Trade-offs & Mitigations

- **Extreme minimalism achieved**: Zero added dependencies. Perfect alignment with PPAI sovereignty and anti-vibe-coding principles.
- **Performance**: Excellent on Pixel 6 Pro — negligible CPU/memory, instant startup. Superior to any framework-based solution.
- **Maintainability**: Single, auditable Python file — easy to understand, modify, or replace.
- **Grok compatibility**: Clean, simple HTML performs perfectly with the `browse_page` tool (often better than heavier frameworks).
- **Future replacement**: The entire feature can be swapped for a static generator or removed with zero impact on the rest of the brain.

---

## Migration Path & Future Evolution

- **Termux bootstrap**: Uses existing venv + pure Python script.
- **Nix flake environment**: Same script becomes part of the sandboxed appliance (add minimal Bubblewrap rule for the listener).
- **Robotic embodiment**: Evolves into internal debug endpoint with no brain-directory changes.
- **Long-term**: Can be extended or replaced by lighter mechanisms once full Nix environment is active.

---

## Verification & Acceptance Criteria

- Service starts cleanly on `127.0.0.1` only.
- Directory listing renders correctly and is fully navigable.
- Path escaping and non-brain files rejected with 403.
- File previews work for text/Markdown/code; binaries downloadable.
- Tunnel access is encrypted and private-only.
- Logs written exclusively inside `logs/secure-browser/`.
- Full brain remains portable (`rsync`/`tar` unchanged).
- Successfully tested with Grok’s `browse_page` tool.

---

## Next Steps

1. Create directory skeleton: `src/ppai/backend/`
2. Implement `secure_browser.py` (single file).
3. Create/update `start-private-browser.sh`.
4. Test locally on Termux, then validate with Grok via private tunnel.
5. Document any observed issues in the brain’s issue tracker.

**This v1.1 design fully satisfies the master architecture’s principles of radical minimalism, sovereignty, and maintainability.**

---
*End of Document*
