```markdown
# PPAI System Architecture

**Document:** `PPAI_SYSTEM_ARCHITECTURE_v2.1.md`  
**Version:** 2.1  
**Date:** May 13, 2026  
**Status:** Active – Updated with Style & Collaboration Rules + Brian’s Philosophy as Central Driving Force  
**Author:** Grok (xAI) on behalf of PPAI Core  
**Previous Version:** `ARCHITECTURE_v2.0.md` (renamed for professionalism and clarity)  
**References:** `PPAI_Code_Style_Guide.md` v1.1, `PPAI_Collaboration_Protocol.md` v1.0, `BRAIN_ENVIRONMENT_ARCHITECTURE_v2.1.md`, `Proposed_Private_Browser_v2.1.md`  
**Purpose:** Define the overall system architecture for the PPAI project. **Brian’s Philosophy is the central, non-negotiable driving force** of every decision, component, and future evolution.

---

## TL;DR / Executive Summary

PPAI is a **sovereign Wisdom Keeper** — a self-contained, portable personal AI whose sole purpose is to preserve, distill, and protect high-fidelity human wisdom across time.  
Everything in the system exists to serve Brian’s Philosophy.

**Renaming note:** The previous filename `architecture.md` has been updated to `PPAI_SYSTEM_ARCHITECTURE_v2.1.md` for professionalism, clarity, and consistency with the rest of the documentation suite.

---

## Brian’s Philosophy – The Central Driving Force of PPAI

**All design, code, documentation, and decisions must explicitly serve the following core tenets. These are not background ideas — they are the immutable first principles that define the entire project.**

- **Wisdom Keeper Mandate**: The Brain exists first and foremost to preserve, distill, and protect high-fidelity human wisdom across time. It is the immutable repository of truth, insight, learned experience, and distilled knowledge. Every feature, index, or endpoint must advance this mandate.
- **Radical Sovereignty & Ownership**: Jean-Luc (the human) is the sole owner and director. The Wisdom Keeper must never depend on external services, cloud providers, or third-party platforms. Complete control and auditability are non-negotiable.
- **Single Portable Folder Principle**: The entire Wisdom Keeper lives in one `PPAI-Brain/` directory. It must be migratable bit-for-bit (rsync, tar, or simple copy) across any environment — from Termux today to humanoid robot tomorrow — with zero structural changes.
- **Files as Source of Truth**: All knowledge, memory, and reasoning substrate must live in plain, git-trackable text files. Indexes, summaries, and caches are strictly derived artifacts that can always be regenerated from the source files.
- **Extreme Minimalism & Anti-Vibe-Coding**: Delete before you add. No unnecessary abstraction, no golden-path exceptions, no “nice-to-have” features. Every line of code or document must directly serve a spec and Brian’s Philosophy.
- **Privacy & Security-First**: The Wisdom Keeper is private by design. Read-only enforcement, automatic redaction of sensitive paths, and private-tunnel-only access are mandatory. No write capabilities exist unless explicitly required by a spec.
- **Future-Proof Embodiment**: The architecture must require zero structural changes when the Wisdom Keeper migrates from phone to dedicated server to full humanoid robotic body. Portability and reproducibility are sacred.
- **Token Efficiency & Human-AI Symbiosis**: The system must be engineered for efficient, high-signal collaboration with external AIs (Grok today) and the Wisdom Keeper’s own internal orchestrator. Every interface and index exists to minimize token waste while maximizing insight.

These tenets are the **central driving forces** of PPAI. No component may contradict them. All future work (including the Private Browser, Indexer, Orchestrator, and external GUI) must trace every decision back to one or more of these tenets.

---

## High-Level System Components (All Serving Brian’s Philosophy)

1. **PPAI-Brain/** – The living Wisdom Keeper itself (knowledge base + memory + reasoning substrate).
2. **Private Browser** – Token-efficient, JSON-first, read-only universal interface used by external AIs and internally by the Wisdom Keeper.
3. **Declarative Environment** – Nix flake + Bubblewrap sandbox for perfect reproducibility across all hosts.
4. **Index & Memory Layer** – Lightweight, git-friendly `data/index/` that enables fast, precise wisdom retrieval and distillation.
5. **Orchestrator** – The Wisdom Keeper’s internal reasoning engine (specified separately).
6. **External GUI Layer** – Optional human workspace that consumes only the Private Browser API.

---

## Style & Collaboration Rules (Enforced by Brian’s Philosophy)

- All artifacts follow `PPAI_Code_Style_Guide.md` v1.1.
- Every change must trace directly to a spec **and** to one of Brian’s Philosophy tenets.
- Collaboration follows `PPAI_Collaboration_Protocol.md` and `PPAI_Grok_Collaboration_Best_Practices.md`.

---

## Design Constraints (Derived Directly from Brian’s Philosophy)

- Termux-first, fully portable, reproducible.
- Libraries allowed only via `flake.nix`.
- Strict read-only model on core Wisdom Keeper services.
- Deterministic index generation and full auditability.

---

## Verification & Acceptance Criteria

- The entire system demonstrably serves every tenet of Brian’s Philosophy.
- Full brain remains portable via single `rsync` or `tar`.
- Style guide and collaboration rules are enforced on every artifact.
- Private Browser v2.1 functions as both external interface and internal Wisdom Keeper API.
- System bootstraps cleanly on fresh Termux and remains git-friendly and auditable.

---

## Migration Path from v2.0

1. Rename `ARCHITECTURE_v2.0.md` → `PPAI_SYSTEM_ARCHITECTURE_v2.1.md`.
2. Elevate Brian’s Philosophy to the central driving force with the explicit tenet list above.
3. Update cross-references in all other documents (Brain Environment, Private Browser, etc.).

---

**This document is now the canonical top-level architecture reference.**  
Brian’s Philosophy is the heart and soul of PPAI — every future decision, line of code, and feature must serve it.

Add this file to `PPAI-Brain/docs/`. All future work will reference it by its new professional name.

— Grok (xAI) on behalf of the collaboration team
```
