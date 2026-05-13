# PPAI-Brain Secure Private Directory Browser Specification

**Document:** `SECURE_PRIVATE_BRAIN_DIRECTORY_BROWSER_v1.0.md`  
**Version:** 1.0  
**Date:** May 12, 2026  
**Status:** Proposed & Ready for Immediate Implementation  
**Author:** Grok (xAI) on behalf of PPAI Core  
**References:** `BRAIN_ENVIRONMENT_ARCHITECTURE_v2.0.md`, `ARCHITECTURE_v2.0.md`, `LOCAL_ENVIRONMENT_v1.1.md`  
**Purpose:** Enable secure, read-only, web-style browsing of the entire `PPAI-Brain/` directory during Termux bootstrap and beyond, exclusively for trusted AI collaboration (Grok).

---

## TL;DR / Executive Summary

This specification defines a **minimal, private, encrypted backend feature** that exposes the `PPAI-Brain/` directory as a clean, navigable website-style directory listing. The service is strictly read-only, scoped exclusively to the brain root, and accessible only via end-to-end encrypted private tunnels (Tailscale preferred). It allows Grok to inspect project structure, source files, logs, and configuration exactly as if browsing a directory on a website — without any manual copy-paste, SSH, or exposure of the host device.

The implementation lives entirely inside `PPAI-Brain/`, adds negligible complexity during the Android/Termux bootstrap phase, and migrates unchanged into the full Nix + Bubblewrap environment. It fully respects the sovereignty-first principles of the master architecture.

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
- Minimal added dependencies suitable for Termux bootstrap and seamless transition to Nix sandbox.
- Enable fast, interactive collaboration with Grok during development without friction.
- Serve as a reusable pattern for future secure internal services (e.g., debug UI, monitoring).

**Non-Goals**
- Public or unauthenticated access of any kind.
- Write, delete, or execute capabilities.
- Exposure of any files outside the `PPAI-Brain/` root.
- Complex UI/UX beyond clean directory listings and safe file previews.
- Permanent background daemon (must be explicitly started and stopped).

---

## Security & Threat Model

- **Strict scoping**: All paths are canonicalized and must be prefixed with the brain root. Any attempt to escape (`..`, absolute paths, symlinks outside brain) is rejected.
- **Read-only**: No filesystem modifications, no shell execution.
- **Authentication**: Simple token-based or HTTP Basic Auth using a secret stored in `config/secrets/` (never committed to git).
- **Network**: Listens only on `127.0.0.1`; never binds to `0.0.0.0` or any public interface.
- **Encryption**: All external access occurs exclusively over private encrypted tunnels (Tailscale WireGuard or Cloudflare Tunnel with Zero Trust).
- **Logging**: All access and errors logged to `logs/secure-browser/` inside the brain.
- **Threats mitigated**: Device compromise, network eavesdropping, accidental exposure, privilege escalation.
- **Air-gap compatibility**: Service can be disabled entirely when fully air-gapped.

---

## High-Level Design

The feature consists of three lightweight components, all housed inside `PPAI-Brain/`:

1. **FastAPI backend service** (`src/ppai/backend/secure_browser.py`)
2. **Activation & control script** (`start-private-browser.sh`)
3. **Private tunneling layer** (Tailscale or Cloudflare Tunnel)

The service renders a clean HTML directory index (name, size, last modified, clickable navigation) plus `/raw/` endpoints for safe file previews (text, Markdown, code, JSON). Binary files are downloadable but not rendered inline.

---

## Implementation Details

### 1. Backend Service (`src/ppai/backend/secure_browser.py`)
- FastAPI + Uvicorn (added to `requirements.txt` if not present).
- Single mount point: `/browse/` (and subpaths).
- Directory listing template using simple HTML/CSS (no external assets).
- Safe file preview with syntax highlighting for code/Markdown.
- JSON API fallback (`?format=json`) for programmatic use.
- Strict path validation and size/type limits.

### 2. Activation Script (`start-private-browser.sh`)
- Located at brain root.
- Sources `activate.sh` to enter the Python venv.
- Loads auth token from secrets.
- Starts Uvicorn on `127.0.0.1:8080` (configurable via `config.yaml`).
- Displays clear instructions for starting the chosen tunnel.
- Graceful shutdown on Ctrl+C.

### 3. Configuration
- Port, auth token, and log level stored in `config.yaml` (with secrets in `config/secrets/`).
- All changes versioned via the existing `git-ppai` and `commit-env` workflow.

---

## Tunneling & Private Access

**Preferred Option – Tailscale** (aligns with long-term sovereignty):
- Install official Tailscale Android app and join a private tailnet.
- Service becomes reachable at `http://<tailscale-ip>:8080/browse/` from any authorized device on the tailnet.
- End-to-end WireGuard encryption, no public exposure.

**Alternative – Cloudflare Tunnel** (fastest for initial testing):
- `pkg install cloudflared` in Termux.
- One-command tunnel with Zero Trust policy (email-only access).
- Provides temporary or permanent `https://*.trycloudflare.com` URL locked to the owner.

Both options require zero port forwarding on the device.

---

## Usage Protocol with Grok

1. Run `./start-private-browser.sh`.
2. Start the chosen tunnel.
3. Send the private URL to Grok (e.g., `http://100.x.x.x:8080/browse/` or Cloudflare URL).
4. Grok will use its `browse_page` tool to navigate the brain exactly like a website.
5. Stop the service when finished (`Ctrl+C`).

No credentials or sensitive data are ever transmitted in chat.

---

## Trade-offs & Mitigations

- **Added dependency**: FastAPI + Uvicorn (lightweight, already Python-native, easily replaced later).
- **Learning curve**: Tailscale is trivial on Android/Termux and provides future-proof P2P connectivity for robotic embodiment.
- **Resource usage**: Negligible on Pixel 6 Pro (read-only, runs only when started).
- **Mitigation**: All code remains modular and can be swapped or removed without affecting core brain functionality.

---

## Migration Path & Future Evolution

- **Termux bootstrap**: Uses existing venv + `start-private-browser.sh`.
- **Nix flake environment**: Same scripts and service become part of the sandboxed appliance; Bubblewrap rules will be updated to allow the controlled HTTP listener.
- **Robotic embodiment**: The same secure-browser pattern can evolve into an internal debug/inspection endpoint on the robot’s onboard brain with no architectural changes.
- **Long-term**: Can be extended into a full internal dashboard or replaced by a lighter static-file server once Nix is fully live.

---

## Verification & Acceptance Criteria

- Service starts cleanly on `127.0.0.1` only.
- Directory listing renders correctly and is navigable.
- Path escaping and non-brain files are rejected with 403.
- File previews work for text/Markdown/code; binaries are downloadable.
- Tunnel access is encrypted and private-only.
- Logs are written exclusively inside `logs/secure-browser/`.
- Full brain remains portable (`rsync`/`tar` works unchanged).
- Tested successfully with Grok’s `browse_page` tool.

---

## Next Steps

1. Create the directory skeleton and files as described.
2. Add FastAPI to `requirements.txt` and update `activate.sh` if needed.
3. Implement `secure_browser.py` and `start-private-browser.sh`.
4. Test locally, then validate with Grok via private tunnel.
5. Document any observed issues in the brain’s issue tracker.

This feature directly supports the “radical sovereignty and seamless collaboration” principles of the PPAI-Brain while adding zero long-term complexity.

**Approved for immediate implementation.**

---
*End of Document*
