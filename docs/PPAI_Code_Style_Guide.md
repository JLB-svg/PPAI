```markdown
# PPAI Code Style Guide

**Document:** `PPAI_Code_Style_Guide.md`  
**Version:** 1.2 (Naming Conventions Edition)  
**Date:** May 13, 2026  
**Status:** Active – Enforced for all files in the repository  
**Author:** Grok (xAI) on behalf of PPAI Core  
**References:** `PPAI_Collaboration_Protocol.md` v1.0, `PPAI_SYSTEM_ARCHITECTURE_v2.1.md` – Brian’s Philosophy, `BRAIN_ENVIRONMENT_ARCHITECTURE_v2.1.md`  
**Purpose:** Provide a single, unified style authority for **every** file type in the PPAI-Brain repository. High-level principles apply universally; short subsections give precise rules per file type. This v1.2 adds explicit, consistent Naming Conventions to eliminate repeated clarification and further reduce token waste.

---

## 1. Universal Principles (Apply to ALL Files)

- **Traceability First**: Every file, function, section, or cell must contain a one-line reference to the exact spec (e.g., `# per PPAI_SYSTEM_ARCHITECTURE_v2.1.md – Brian’s Philosophy` or `<!-- per … -->`).
- **Extreme Minimalism**: Delete before you add. No file should exist unless required by a spec. Target smallest possible surface area.
- **Sovereignty & Portability**: Everything must remain inside one portable `PPAI-Brain/` folder. Dependencies declared only in `flake.nix`. Termux-first, robot-ready, rsync/tar safe.
- **Files as Source of Truth**: Generated artifacts (indexes, summaries, caches) are never primary. Always deterministic and regeneratable.
- **Anti-Vibe-Coding**: No features, comments, or formatting that are not explicitly required by a spec.
- **Token Efficiency**: All human- or AI-readable content must be concise, predictable, and low-noise. Prefer structured data over prose.
- **Security & Read-Only Model**: Never introduce write capabilities unless explicitly documented in the spec.
- **Git-Friendly**: No auto-generated binary blobs. All text files must be diffable and mergeable.
- **Enforcement**: Grok self-enforces this guide on every artifact. Violations are flagged in one line.

---

## 2. Naming Conventions (New in v1.2 – Apply to ALL Files)

- **File Names**: `snake_case` (e.g. `brain_indexer.py`, `secure_browser.py`, `ai_knowledge_organization.md`). Use kebab-case only for very specific external-facing files (e.g. `start-private-browser.sh`).
- **Functions & Variables**: `snake_case` (e.g. `generate_file_preview()`, `token_estimate`).
- **Constants & Config Keys**: `UPPER_SNAKE_CASE` (e.g. `MAX_PREVIEW_CHARS`).
- **Classes (if ever used)**: `PascalCase` (rare; only when they demonstrably reduce duplication per Code Style Guide §1).
- **Markdown Headings & Section Titles**: Title Case with no trailing punctuation unless it is a question (e.g. `## Brian’s Philosophy`).
- **Data / Index Files & Keys**: `snake_case` for keys and filenames; sorted keys in JSON/YAML where practical.
- **Shell Variables & Flags**: `snake_case` or `UPPER_SNAKE_CASE` for environment variables.
- **References to Specs**: Always use the exact filename + version (e.g. `per PPAI_Code_Style_Guide.md v1.2 – Naming Conventions`).
- **No Ambiguity**: Names must be self-documenting and trace back to a spec section. Avoid abbreviations longer than 3 letters unless universally obvious (e.g. `url` is allowed).

---

## 3. Python Code

- Follow PEP 8 + PEP 257 (ruff-compatible) with type hints everywhere.
- Use only libraries declared in `flake.nix`. Prefer stdlib first.
- Async only when it demonstrably simplifies concurrency (e.g., FastAPI browser).
- Single-responsibility functions; no unnecessary classes.
- Docstrings: Google style with one-line summary + References section linking to spec.
- Error handling: explicit, logged, structured exceptions.
- File size target: <200 LOC when possible.

---

## 4. Markdown Documentation

- Use GitHub-flavored Markdown with level-1 heading as title.
- Front-matter YAML block at top with Document, Version, Date, Status, References.
- One blank line between sections. No trailing whitespace.
- Use `**bold**` for emphasis, never *italic* alone.
- Code blocks for all examples. Use `diff` blocks for updates.
- Every section must trace to a spec or be marked “Informational”.
- Keep documents short (<2 pages / ~800 tokens) unless the topic demands otherwise.

---

## 5. Nix & Configuration Files (flake.nix, YAML, JSON, TOML)

- `flake.nix`: Declarative, minimal, reproducible. Comment every input and output with spec reference.
- YAML/JSON: Consistent indentation (2 spaces), sorted keys where possible, no trailing commas in JSON.
- All config values must be overridable via environment or `config/` files.
- Sensitive values never stored in plain text — reference `secrets/` only.
- Human-readable comments explaining purpose and spec link.

---

## 6. Shell Scripts & Activation Files (*.sh)

- Shebang `#!/usr/bin/env bash` or `#!/usr/bin/env sh`.
- `set -euo pipefail` at top.
- Functions preferred over long linear scripts.
- Every major action logged with clear message.
- No hard-coded paths — use variables or `realpath`.
- Exit codes and error messages must be explicit and traceable to spec.

---

## 7. Data & Index Files (CSV, JSON indexes, SQLite schemas, spreadsheets)

- CSV: Header row first, UTF-8, no extra whitespace, quoted fields only when needed.
- JSON indexes: Pretty-printed (2 spaces) or minified only if size >1 MB. Always include schema version and generation timestamp.
- Spreadsheets (if used): First sheet named “DATA”, column headers in row 1, one frozen row, every column and sheet referenced in a companion Markdown spec.
- All data files must have a companion `_README.md` or header comment explaining regeneration command and spec link.
- Never commit large binary spreadsheets — prefer CSV + Git LFS only if unavoidable.

---

## 8. Future File Types (Placeholders – Add Subsections as Needed)

### 8.1 Rust / Mojo (Planned Hybrid Extensions)
- (Reserved – will follow same universal principles + Rust 2024 edition or Mojo style when introduced)

### 8.2 Logs & Daily Files
- (Reserved – structured JSON lines or Markdown with timestamp + spec reference)

### 8.3 C++ / Embedded / Robotic Firmware
- (Reserved – when embodiment phase begins)

### 8.4 Any Other File Type
- Add a new numbered subsection following the same pattern: 3–6 bullets max, universal principles still apply.

---

## 9. Enforcement & Evolution

- I (Grok) will apply this guide to every artifact I produce.
- You may invoke “per Code Style Guide §X.Y” at any time.
- Updates to this document follow the Collaboration Protocol (targeted diff only).
- This guide remains short by design. New subsections are added only when a new file type appears in the repo.

---

**This is now the single source of truth for style across the entire PPAI-Brain.**  
Copy and paste this entire block into `docs/PPAI_Code_Style_Guide.md` (or let me know if you want me to push it via the GitHub connector after the repo is restored).

— Grok (xAI) on behalf of the collaboration team
```
