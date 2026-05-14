# PPAI Code Style Guide

**Document:** `PPAI_Code_Style_Guide.md`  
**Version:** 1.0  
**Date:** May 13, 2026  
**Status:** Active – Enforced for all new code  
**Author:** Grok (xAI) on behalf of PPAI Core  
**References:** `PPAI_Collaboration_Protocol.md`, `BRAIN_ENVIRONMENT_ARCHITECTURE_v2.1.md`, `Proposed_Private_Browser_v2.1.md`  
**Purpose:** Provide concise, enforceable rules that keep the PPAI-Brain codebase minimal, auditable, sovereign, and token-efficient while I (Grok) serve as primary coder. This guide replaces all ad-hoc style discussions and enforces the project’s anti-vibe-coding discipline.

---

## 1. Core Principles (Non-Negotiable)

- **Traceability First**: Every function, class, or module **must** include a one-line comment linking back to the exact spec section (e.g., `# per BRAIN_ENVIRONMENT_ARCHITECTURE_v2.1.md §4.2`). No exceptions.
- **Extreme Minimalism**: Prefer deletion over addition. Target <200 LOC per file when possible. No classes or abstractions unless they eliminate >20 lines of duplication.
- **Sovereignty & Portability**: The entire codebase must remain one portable `PPAI-Brain/` folder. All dependencies are declared in `flake.nix` (Nix-managed). Termux-first, robot-ready.
- **Files as Source of Truth**: Indexes, caches, and generated artifacts are never primary. Always regeneratable from source files.
- **Read-Only Security Model**: The Private Browser and all Brain services remain strictly read-only unless explicitly documented otherwise.
- **Token Efficiency**: All public APIs (especially JSON responses) must be concise, predictable, and LLM-native. Include token estimates where relevant.
- **Anti-Vibe-Coding**: No “nice-to-have” features, no golden-path exceptions, no cleverness for its own sake.

---

## 2. Python Language Rules (2026 Edition)

- **Baseline**: Follow PEP 8 + PEP 257 with ruff-compatible formatting.
- **Libraries**: Allowed **only** if declared in `flake.nix` and they deliver measurable value (performance, safety, token efficiency, or portability). Prefer pure-Python stdlib first. Current allowed set will be listed in `flake.nix`.
- **Async**: Use `asyncio` / FastAPI where it simplifies concurrency (Private Browser). Keep synchronous when it does not.
- **Typing**: Use type hints everywhere (Pydantic v2 preferred for schemas).
- **Error Handling**: Explicit, logged, and never silent. Use structured exceptions that map cleanly to JSON error responses.
- **No Globals**: Configuration comes from `config/` or environment only.

---

## 3. Naming & Structure Conventions

- **Files**: `snake_case.py` (e.g., `brain_indexer.py`, `secure_browser.py`).
- **Functions**: `verb_noun()` – clear, single responsibility.
- **Variables**: `snake_case`. Short but descriptive (e.g., `file_preview` not `fp`).
- **Constants**: `UPPER_SNAKE_CASE`.
- **Modules**: One primary purpose per file. Keep `__init__.py` minimal.
- **Docstrings**: Google style, one-line summary + Args/Returns/References section. Always include spec link.

---

## 4. Browser & API Rules

- Default response: Clean, predictable JSON (Pydantic models).
- Query params for navigation (`?depth=`, `?q=`, `?mode=concise`).
- All sensitive paths redacted automatically.
- Security headers and rate limiting mandatory on every response.
- Human HTML fallback must be minimal (inline CSS/JS only).

---

## 5. Indexer & Memory Layer Rules

- All index generation must be deterministic and reproducible via `commit-env.sh`.
- Store only derived data in `data/index/`.
- Use lightweight formats (JSON + optional SQLite) that stay git-friendly.

---

## 6. Testing & Verification

- Every new module must include a one-line acceptance test comment referencing Verification & Acceptance Criteria from its spec.
- Run full brain portability test (`rsync` + restart on clean Termux) before any merge.

---

## 7. Enforcement

- I (Grok) will self-enforce this guide on every line of code I produce.
- You may invoke “per Code Style Guide §X” at any time.
- Violations will be flagged immediately with a one-line correction.

---

**This guide is intentionally short (one page) and will evolve only via explicit updates to this document.**

Add this file to `PPAI-Brain/docs/`. All future coding tasks will reference it by name.

This is how we build a professional, sovereign, AI-native codebase together.

— Grok (xAI) on behalf of the collaboration team
