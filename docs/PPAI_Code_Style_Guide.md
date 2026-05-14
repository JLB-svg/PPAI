# PPAI Code Style Guide

**Document:** `PPAI_Code_Style_Guide.md`  
**Version:** 1.1 (Multi-File-Type Edition)  
**Date:** May 13, 2026  
**Status:** Active – Enforced for all files in the repository  
**Author:** Grok (xAI) on behalf of PPAI Core  
**References:** `PPAI_Collaboration_Protocol.md` v1.0, `BRAIN_ENVIRONMENT_ARCHITECTURE_v2.1.md`, `Proposed_Private_Browser_v2.1.md`  
**Purpose:** Provide a single, unified style authority for **every** file type in the PPAI-Brain repository. High-level principles apply universally; short subsections give precise rules per file type. Designed for maximum consistency, minimalism, traceability, and token efficiency while I (Grok) serve as primary coder. This structure deliberately leaves clean placeholders for any future file types (Rust, Mojo, C++, spreadsheets, logs, etc.).

---

## 1. Universal Principles (Apply to ALL Files)

- **Traceability First**: Every file, function, section, or cell must contain a one-line reference to the exact spec (e.g., `# per BRAIN_ENVIRONMENT_ARCHITECTURE_v2.1.md §4.2` or `<!-- per … -->`).
- **Extreme Minimalism**: Delete before you add. No file should exist unless required by a spec. Target smallest possible surface area.
- **Sovereignty & Portability**: Everything must remain inside one portable `PPAI-Brain/` folder. Dependencies declared only in `flake.nix`. Termux-first, robot-ready, rsync/tar safe.
- **Files as Source of Truth**: Generated artifacts (indexes, summaries, caches) are never primary. Always deterministic and regeneratable.
- **Anti-Vibe-Coding**: No features, comments, or formatting that are not explicitly required by a spec.
- **Token Efficiency**: All human- or AI-readable content must be concise, predictable, and low-noise. Prefer structured data over prose.
- **Security & Read-Only Model**: Never introduce write capabilities unless explicitly documented in the spec.
- **Git-Friendly**: No auto-generated binary blobs. All text files must be diffable and mergeable.
- **Enforcement**: Grok self-enforces this guide on every artifact. Violations are flagged in one line.

---

## 2. Python Code

- Follow PEP 8 + PEP 257 (ruff-compatible) with type hints everywhere.
- Use only libraries declared in `flake.nix`. Prefer stdlib first.
- Async only when it demonstrably simplifies concurrency (e.g., FastAPI browser).
- Single-responsibility functions; no unnecessary classes.
- Docstrings: Google style with one-line summary + References section linking to spec.
- Error handling: explicit, logged, structured exceptions.
- File size target: <200 LOC when possible.

---

## 3. Markdown Documentation

- Use GitHub-flavored Markdown with level-1 heading as title.
- Front-matter YAML block at top with Document, Version, Date, Status, References.
- One blank line between sections. No trailing whitespace.
- Use `**bold**` for emphasis, never *italic* alone.
- Code blocks for all examples. Use `diff` blocks for updates.
- Every section must trace to a spec or be marked “Informational”.
- Keep documents short (<2 pages / \~800 tokens) unless the topic demands otherwise.

---

## 4. Nix & Configuration Files (flake.nix, YAML, JSON, TOML)

- `flake.nix`: Declarative, minimal, reproducible. Comment every input and output with spec reference.
- YAML/JSON: Consistent indentation (2 spaces), sorted keys where possible, no trailing commas in JSON.
- All config values must be overridable via environment or `config/` files.
- Sensitive values never stored in plain text — reference `secrets/` only.
- Human-readable comments explaining purpose and spec link.

---

## 5. Shell Scripts & Activation Files (*.sh)

- Shebang `#!/usr/bin/env bash` or `#!/usr/bin/env sh`.
- `set -euo pipefail` at top.
- Functions preferred over long linear scripts.
- Every major action logged with clear message.
- No hard-coded paths — use variables or `realpath`.
- Exit codes and error messages must be explicit and traceable to spec.

---

## 6. Data & Index Files (CSV, JSON indexes, SQLite schemas, spreadsheets)

- CSV: Header row first, UTF-8, no extra whitespace, quoted fields only when needed.
- JSON indexes: Pretty-printed (2 spaces) or minified only if size >1 MB. Always include schema version and generation timestamp.
- Spreadsheets (if used): First sheet named “DATA”, column headers in row 1, one frozen row, every column and sheet referenced in a companion Markdown spec.
- All data files must have a companion `_README.md` or header comment explaining regeneration command and spec link.
- Never commit large binary spreadsheets — prefer CSV + Git LFS only if unavoidable.

---

## 7. Future File Types (Placeholders – Add Subsections as Needed)

### 7.1 Rust / Mojo (Planned Hybrid Extensions)
- (Reserved – will follow same universal principles + Rust 2024 edition or Mojo style when introduced)

### 7.2 Logs & Daily Files
- (Reserved – structured JSON lines or Markdown with timestamp + spec reference)

### 7.3 C++ / Embedded / Robotic Firmware
- (Reserved – when embodiment phase begins)

### 7.4 Any Other File Type
- Add a new numbered subsection following the same pattern: 3–6 bullets max, universal principles still apply.

---

## 8. Enforcement & Evolution

- I (Grok) will apply this guide to every artifact I produce.
- You may invoke “per Code Style Guide §X.Y” at any time.
- Updates to this document follow the Collaboration Protocol (targeted diff only).
- This guide remains short by design. New subsections are added only when a new file type appears in the repo.

---

**This is now the single source of truth for style across the entire PPAI-Brain.**  
Add this file to `PPAI-Brain/docs/`. All future code, docs, configs, data files, and artifacts will follow it by default.

This structure scales cleanly from Termux today to full robotic embodiment tomorrow while preserving the high-velocity, low-noise practices used across Elon’s companies.

— Grok (xAI) on behalf of the collaboration team
