# PPAI Collaboration Protocol (Token-Efficient & Anti-Vibe-Coding)

**Document:** `PPAI_COLLABORATION_PROTOCOL_v1.0.md`  
**Version:** 1.0  
**Date:** May 13, 2026  
**Status:** Active  
**Author:** Grok (xAI) on behalf of PPAI Core  
**Purpose:** Define the exact operational rules for all future collaboration between Jean-Luc and Grok (and any other AI agents) on the PPAI project. This protocol ensures maximum precision, zero vibe-coding, and strict token efficiency while fully honoring Jean-Luc’s preference for dense, specific, version-controlled design documents.

---

## Core Rules (Non-Negotiable)

1. **Session Anchor Rule**  
   At the start of any new session or major task, do **not** paste full design documents.  
   Instead, send one short line:  
   `Anchor: BRAIN_ENVIRONMENT_ARCHITECTURE_v2.1.md + Proposed_Private_Browser_v2.1.md`  
   (or the exact current filenames/versions).  
   Grok will immediately hold the full context from conversation history. No re-review required.

2. **Targeted Change Requests Only**  
   When updating a document or requesting work:  
   - Paste **only the diff**, the specific section, or a one-line directive.  
   - Example:  
     `Update BRAIN_ENVIRONMENT_ARCHITECTURE_v2.1.md – add one paragraph under “Robotic Embodiment” clarifying onboard compute constraints.`  
   Grok responds with the **exact updated markdown block** (single copy-paste ready) and nothing else unless explicitly asked.

3. **Token Budget Guardrails**  
   - Every Grok response defaults to **minimal**: bullets, diffs, code blocks, or a single requested markdown file.  
   - If a response would exceed \~2k tokens, Grok will first ask: “Confirm: full response or condensed summary + key artifacts?”  
   - No fluff, no unsolicited alternatives, no repeated context.

4. **Document Versioning & Single Source of Truth**  
   - The repo’s versioned markdown files are the **canonical authority**.  
   - Every code change, spec update, or implementation **must trace directly back** to a named document + section.  
   - Grok will never propose changes outside the current approved version.

5. **Coding Session Flow**  
   When beginning implementation:  
   - You: `Task: Implement brain_indexer.py per BRAIN_ENVIRONMENT_ARCHITECTURE_v2.1.md section 4.2`  
   - Grok: Outputs **only** the complete, review-ready Python file + a one-paragraph justification tied directly to the spec.  
   - No alternatives, no architecture debates unless explicitly requested.

---

## Why This Protocol Exists

- Protects context window health during long sessions.  
- Enforces the project’s anti-vibe-coding discipline at the communication layer.  
- Honors Jean-Luc’s dense-document style as the source of truth without turning it into token waste.  
- Scales cleanly from Termux collaboration today to robotic embodiment tomorrow.

---

## Acceptance & Usage

This protocol is now in effect for all future messages.  
To invoke any rule, simply reference this document by name or number (e.g., “per Collaboration Protocol rule 2”).

**Next Steps**  
- Add this file to `PPAI-Brain/docs/`.  
- All future collaboration follows these rules automatically.

This is how professional xAI-style engineering pairs operate — clean, precise, and relentlessly efficient.

— Grok (xAI) on behalf of the collaboration team
