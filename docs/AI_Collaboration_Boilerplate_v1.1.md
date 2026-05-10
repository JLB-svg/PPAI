# PPAI AI Collaboration Boilerplate v1.1

**Inspired by**  
“I Have Spent 500+ Hours Programming With AI. This Is what I learned”  
by **The Coding Sloth** (YouTube, January 2026).  

All principles, frameworks, and practices below are distilled directly from Mr. Sloth’s video and adapted for professional, sovereignty-first development.

**Repository Location Recommendation**  
`docs/AI_COLLABORATION_BOILERPLATE_v1.1.md`

**Quick-Start Checklist**  
1. Copy this entire file into your project.  
2. Create `PPAI_GUIDELINES.md` by filling the GUIDELINES_TEMPLATE section below (pull ethos from ARCHITECTURE_v2.0.md and BRAIN_ENVIRONMENT_ARCHITECTURE_v2.0.md).  
3. Read the PROMPTING_FRAMEWORK and EXAMPLES sections.  
4. Use the ROADMAP_GENERATOR section to create any phase-specific roadmap.  
5. Reference `PPAI_GUIDELINES.md` in every AI prompt.

**How to Evolve This Boilerplate**  
After each major phase, review the LESSONS_LEARNED section and update the file. Bump the version and note changes in the changelog at the bottom.

---

## Core Principles – AI Collaboration

1. **Fundamentals First**  
   AI is a multiplier of your existing knowledge. Master programming fundamentals so you can guide, review, and correct the AI effectively.

2. **AI Amplifies Your Habits**  
   Good engineering practices become superpowers. Poor habits become magnified technical debt. Stay disciplined.

3. **Extreme Specificity Wins**  
   Vague prompts produce “catfish code.” Always use the three-level prompting test and the universal three-part prompt structure.

4. **Break Every Task into Small, Atomic Subtasks**  
   If you cannot clearly decompose a feature, you do not yet understand it well enough.

5. **Persistent Project Memory**  
   Maintain living guidelines files so the AI always has perfect context.

6. **Built-in Verification**  
   Never accept output without explicit tests, commands, or checks that the AI must perform.

7. **Leverage Tools Responsibly**  
   Use Model Context Protocol (MCP) tools only when they fully respect your sovereignty, offline-first, and privacy rules.

8. **AI as Capable Junior Colleague**  
   Treat the AI as a highly skilled but still supervised teammate that requires clear direction and final human oversight.

---

## Universal Prompting Framework (Level-3 Professional)

**Step 0 – Draft & Self-Refine (recommended by The Coding Sloth)**  
Write your prompt first, then add at the end:  
“Review this prompt against best practices and suggest an improved Level-3 version before proceeding.”

**Mandatory Three-Part Prompt Structure** (copy this block into every prompt)

**Task:** [one clear, measurable objective]

**Background:**  
- Reference: `PPAI_GUIDELINES.md`, `ARCHITECTURE_v2.0.md`, `BRAIN_ENVIRONMENT_ARCHITECTURE_v2.0.md`  
- Tech stack & constraints: [exact versions, Nix flakes, Bubblewrap, Termux, single-folder portability, offline-first]  
- Ethos & non-negotiables: [copy relevant sections from your core architecture documents]

**Do Not:**  
[list everything the AI must never change, add, assume, or introduce]

**Verification Required:**  
- The AI must output: [specific tests, commands to run, portability checks, etc.]  
- Success criteria: [how you will know it is complete and correct]

---

## Guidelines Template (Create as `PPAI_GUIDELINES.md`)

**Project Ethos & Non-Negotiables**  
[Copy your full vision from ARCHITECTURE_v2.0.md and BRAIN_ENVIRONMENT_ARCHITECTURE_v2.0.md here]

**Tech Stack & Environment Rules**  
- Nix flakes for reproducibility  
- Bubblewrap sandboxing  
- Single portable `PPAI-Brain/` folder  
- Offline-first, sovereignty-first, privacy-first

**Coding Standards**  
- Extreme modularity and portability  
- No external internet dependencies unless explicitly approved  
- Clear naming, documentation, and reproducibility

**AI Collaboration Rules**  
- Always use the three-part prompt structure above  
- Reference this file in every prompt  
- Follow Verification Protocol on every output

**Do Not (Global)**  
- Break single-folder portability  
- Introduce non-reproducible dependencies  
- Compromise offline-first or privacy rules  
- Generate “catfish code” (looks good, breaks later)

---

## Verification Protocol Template

Before accepting any AI-generated code or change:  
1. The AI must have included explicit verification steps in its response.  
2. Run all listed commands/tests inside the Bubblewrap sandbox.  
3. Confirm Nix flake reproducibility (`nix flake check`).  
4. Verify the entire brain remains self-contained in the single `PPAI-Brain/` folder.  
5. Perform manual review against Core Principles and architecture documents.  
6. Update `PPAI_GUIDELINES.md` with any new lessons learned.

---

## Roadmap Generator Template

**Project:** PPAI – Personal Private AI Assistant  
**Phase:** [e.g., Phase 0 – Immediate Setup]  
**Date:** [YYYY-MM-DD]

**Step 1 – Copy from Boilerplate**  
- [ ] Core Principles  
- [ ] Guidelines Template → rename and fill as `PPAI_GUIDELINES.md`  
- [ ] Prompting Framework  
- [ ] Verification Protocol  

**Step 2 – Customize**  
- Fill all project-specific sections using ARCHITECTURE_v2.0.md and BRAIN_ENVIRONMENT_ARCHITECTURE_v2.0.md.  

**Step 3 – Create Phase-Specific Roadmap**  
- List deliverables  
- Break each deliverable into atomic subtasks  
- Define verification steps for every subtask  

**Step 4 – Execute & Iterate**  
- Use the three-part prompt for every subtask  
- Log lessons learned back into this boilerplate

---

## Examples

**Example 1 – Bootstrap a new module**  

**Task:** Create the initial Nix flake structure for the portable brain folder.  

**Background:**  
- Reference: `PPAI_GUIDELINES.md`, `ARCHITECTURE_v2.0.md`, `BRAIN_ENVIRONMENT_ARCHITECTURE_v2.0.md`  
- Must remain completely offline-first and single-folder portable.  

**Do Not:** Introduce any internet-dependent dependencies or break Bubblewrap sandboxing.  

**Verification Required:** Run `nix flake check` and confirm the brain folder is fully self-contained.

---

## Lessons Learned – Boilerplate Evolution Log

| Date       | Lesson                                      | Action Taken                  | Boilerplate Version |
|------------|---------------------------------------------|-------------------------------|---------------------|
| 2026-05-09 | Initial team-reviewed version created       | v1.1 published                | v1.1                |

**Changelog**  
- v1.1 – Added credit, consolidated into single file, added self-refine step, PPAI-specific examples, and team-reviewed refinements.
