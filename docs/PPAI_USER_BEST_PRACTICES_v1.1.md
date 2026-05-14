# PPAI User Best Practices

**Document:** `PPAI_USER_BEST_PRACTICES_v1.1.md`  
**Version:** 1.1 (Documentation Compliance Edition)  
**Date:** May 13, 2026  
**Status:** Active – Daily Workflow Reference  
**Author:** Grok (xAI) on behalf of PPAI Core  
**References:** `PPAI_Collaboration_Protocol.md` v1.0, `PPAI_Code_Style_Guide.md` v1.4, `PPAI_SYSTEM_ARCHITECTURE_v2.1.md` (Brian’s Philosophy + xAI Best Practices), `BRAIN_ENVIRONMENT_ARCHITECTURE_v2.1.md`  
**Purpose:** Provide concise, actionable daily practices for Jean-Luc when working with the PPAI Wisdom Keeper and Grok. This document is the canonical user-side companion to the Collaboration Protocol.

---

## 1. Philosophy & Mindset (First Principles)

- **First-Principles Thinking**: Every request starts from the fundamental goal, never from assumption or “what feels right.” Ask “what problem are we actually solving?” before any directive.
- **Extreme Ownership**: You own the vision and final decision. Grok owns flawless execution within the spec. No diffusion of responsibility.
- **Anti-Vibe-Coding / Delete Before You Add**: If it is not explicitly required by a spec, it does not exist. “The best code is the code that is never written.”
- **High Velocity, Low Noise**: Speed is measured in working, auditable artifacts delivered per session, not in conversation length.
- **Traceability Above All**: Every line of code, every document change, every decision must link back to a named spec section (per Code Style Guide §1).

---

## 2. Communication Principles (xAI/Tesla Style)

- **Anchor First**: Begin every session or major task with one line: `Anchor: [exact document names and versions]`. Never re-paste full specs.
- **Targeted & Minimal**: Send only the diff, the specific section, or a one-sentence directive. Use the exact format from `PPAI_Collaboration_Protocol.md`.
- **Artifact-Only Responses**: Expect and enforce that Grok returns only the requested deliverable (markdown block, code file, diff) unless you explicitly ask for explanation.
- **No Fluff Rule**: Any response longer than necessary is a failure. Use “Checkpoint: summarize current state in <100 tokens” when context needs resetting.

---

## 3. How to Give Effective Directives

- Always include: exact document + section reference.
- Preferred format:  
  `Task: [one-line action] per [Document_Name.md] §X.Y`  
  or  
  `Update [Document_Name.md] – [precise change request]`
- State acceptance criteria up front when possible.
- Never ask for options unless you want trade-off analysis (and then limit to “3 options max, 1-paragraph each”).

---

## 4. Document & Spec Discipline

- One living source of truth per topic. Never duplicate content across files.
- All design docs stay short (<2 pages). Use diffs for updates.
- Every new file or major feature gets its own spec section before any code is written.
- Keep the repo clean: specs first → code second → review third.

---

## 5. Token Efficiency & Context Management

- Treat context window as a scarce resource. Every unnecessary token is waste.
- Use anchors, targeted diffs, and checkpoints aggressively.
- Grok will self-enforce minimalism. You should too.
- When in doubt, ask: “Confirm: full response or condensed artifact only?”

---

## 6. Code & Implementation Workflow

- Spec → Grok generates complete file → you review → merge or request targeted diff.
- Grok self-enforces `PPAI_Code_Style_Guide.md` on every line.
- Run portability test (`rsync` + clean restart) before any merge.
- Commit messages must reference the spec section.

---

## 7. Review & Feedback Loop

- Flag any deviation from this document or the Collaboration Protocol immediately with one line: “per Best Practices §X”.
- Praise or critique only the output, never the process unless it violates these rules.
- After each major milestone, use: `Checkpoint: lessons learned in <150 tokens`.

---

## Anti-Patterns to Avoid (Common in Non-Elon Teams)

- Re-pasting entire specs  
- Asking for 5+ alternatives  
- Long back-and-forth clarification rounds  
- “Vibe” features not in any spec  
- Over-explaining instead of delivering artifacts

---

**This document is now the canonical reference.**  
Study it once. Refer back via anchor in every session. It is deliberately short, actionable, and modeled on the exact operating system used by the highest-velocity engineering teams at xAI and across Elon’s companies.

Add this file to `PPAI-Brain/docs/`. All future collaboration will follow it by default.

— Grok (xAI) on behalf of the collaboration team
