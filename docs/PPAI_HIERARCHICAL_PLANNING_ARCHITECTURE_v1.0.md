```markdown
# PPAI_HIERARCHICAL_PLANNING_ARCHITECTURE_v1.0.md

**Document:** `HIERARCHICAL_PLANNING_ARCHITECTURE_v1.0.md`  
**Version:** 1.0 (Initial Formalization)  
**Date:** May 14, 2026  
**Status:** Proposed – Ready for Review & Implementation  
**Author:** Grok (xAI) on behalf of PPAI Core  
**Trace:** Builds directly on PPAI_SYSTEM_ARCHITECTURE_v2.2.md, PPAI_BRAIN_ENVIRONMENT_ARCHITECTURE_v2.2.md, PPAI_WORLD_MODELING_ARCHITECTURE_v1.2.md, PPAI_MEMORY_CONSOLIDATION_ARCHITECTURE_v1.0.md, PPAI_METACOGNITION_ARCHITECTURE_v1.0.md, PPAI_COLLABORATION_PROTOCOL_v1.0.md, and PPAI_STYLE_GUIDE_v1.6.md.  
**Purpose:** Define the Brain’s native Hierarchical Planning & Executive Function subsystem — the Wisdom Keeper’s goal-decomposition, resource-allocation, and long-horizon execution layer. This enables the Brain to break down complex objectives, manage projects across time, track progress, replan when reality (or Mind’s Eye simulations) diverges, and maintain coherent forward momentum while preserving absolute sovereignty, git reproducibility, token efficiency, and seamless integration with the Mind’s Eye, Memory Consolidation, Metacognition, and all other subsystems.

---

### 1. Why This Subsystem Is Critical (and Why It Must Be Inherent)

The Brain (v2.2) now stores, distills, reflects, and simulates. Without hierarchical planning, however, it would remain reactive — brilliant at answering single questions or running isolated simulations but incapable of sustained, goal-directed agency over days, weeks, or months.

This subsystem is the **executive director**:
- It decomposes high-level directives into actionable, trackable plans.
- It allocates attention and resources across the entire Brain.
- It uses Mind’s Eye simulations for forward prediction and risk assessment.
- It treats metacognition reflections and consolidation outputs as live constraints.
- It lives entirely inside the existing `projects/` directory and index layer.

No new tools, no breaking changes, zero bloat.

---

### 2. Core Principles (Aligned with Brian’s Philosophy)

- **Actionable Wisdom**: Plans are not abstract — they are executable, git-trackable artifacts that drive real work.
- **Files as Source of Truth**: All plans, roadmaps, and status updates live as versioned Markdown/YAML inside `projects/<name>/`.
- **Token Efficiency First**: Plans surface only relevant subtasks and simulation-backed predictions; full history is one index lookup away.
- **Human Sovereignty**: Every plan is a human-editable diff; the Brain proposes, the human directs or overrides.
- **Reproducibility**: Planning state is fully deterministic and re-runnable from git history.
- **Mind’s Eye Integration**: Every major plan step is optionally simulated before commitment.
- **Zero Bloat**: Runs in <200 LOC extension to the indexer and browser; pure stdlib where possible.

---

### 3. Hierarchical Planning Architecture (v1.0)

**Layered Design (Fully Compatible with Brain v2.2 + Prior Subsystems)**

**Kernel Layer (Immutable – Extends Existing Indexer & Orchestrator)**  
- Core engine lives inside `brain_indexer.py` (new `plan()` pass) and the Private Browser orchestrator.  
- Triggered automatically on project creation/modification, on commit, or on explicit `/plan` request.  
- Processes:  
  - New user directives in `projects/`.  
  - Mind’s Eye simulation results.  
  - Metacognition reflections and Memory Consolidation outputs.

**Planning Engine**  
- Generates three artifact types (all git-trackable):  
  1. **ROADMAP.md**: Hierarchical breakdown (goals → milestones → tasks) with dependencies and estimated effort.  
  2. **STATUS.yaml**: Live execution state (completed, blocked, in-progress) with Mind’s Eye prediction links.  
  3. **Replan Trace**: Short diff-style log of changes triggered by new data, simulations, or reflections.  
- Uses local LLM (when available) or lightweight rule-based heuristics (stdlib fallback) for decomposition.  
- Mind’s Eye specific: auto-generates simulation requests for high-risk tasks (“simulate fence install under 30 mph gusts before scheduling”).

**Integration Points**  
- **Memory Consolidation**: Completed tasks and replans are automatically distilled into wisdom.  
- **Metacognition**: Every plan includes a self-reflection sidecar before commitment.  
- **Private Browser**: New endpoint `/plan?project=…` returns structured, token-efficient plan JSON.  
- **World Modeling**: Plans can embed or reference live scene-graph predictions.

**Private Browser Integration**  
- New endpoints (zero breaking changes):  
  - `/plan` – create, update, or query hierarchical plans.  
  - `/status` – current execution state across all projects.  
  - All normal endpoints can optionally include `?with-plan=true`.

---

### 4. Natural Progressions & Extended Capabilities

- **Daily Plan Refresh**: On commit, the Brain surfaces “Today’s Focus” based on active ROADMAPs and simulations.  
- **Counterfactual Replanning**: Mind’s Eye runs “what-if” scenarios and triggers automatic replans.  
- **Cross-Project Coordination**: Index layer detects shared resources or dependencies across `projects/`.  
- **Embodiment Ready**: Robot actions are driven by the same planner (digital-twin simulation → task execution → status update).  
- **Long-Horizon Dreaming**: Brain can run multi-week simulations of entire project trajectories using the Mind’s Eye.

---

### 5. Workflow Integration (Professional Daily Use)

1. Human or AI issues a high-level directive (“build the new fence design”).  
2. `./ppai plan --new fence-project` → generates ROADMAP.md + initial Mind’s Eye simulations.  
3. `./commit-env.sh` → indexer runs → planning pass updates STATUS.yaml and reflections.  
4. Grok-class agents receive plan-aware context and propose next actions with simulation backing.  
5. All changes are git diffs — perfect audit trail of executive decision-making.

---

### 6. Trade-offs & Mitigations

- **Benefits**: True long-horizon agency, dramatically improved project coherence, proactive risk mitigation via Mind’s Eye.  
- **Added Surface**: <200 LOC inside existing tools; fully auditable.  
- **Mitigations**: Plans are human-editable proposals; no autonomous execution without explicit approval; index remains derived.

---

### 7. Verification & Acceptance Criteria

- Planning runs deterministically on any host (including Termux).  
- Brain v2.2 + World Modeling v1.2 + Memory Consolidation v1.0 + Metacognition v1.0 + Hierarchical Planning v1.0 remain fully portable and git-clean.  
- Private Browser correctly surfaces hierarchical plans and status without token bloat.  
- Live Grok sessions demonstrate goal decomposition, simulation-backed replanning, and coherent multi-day execution.  
- Mind’s Eye simulations are automatically incorporated into plans.

---

**Migration Path from Current Brain v2.2**  
1. Add planning pass to `brain_indexer.py` and orchestrator.  
2. Run one-time `./ppai plan --bootstrap` to generate ROADMAPs for existing projects.  
3. Update Private Browser endpoints (minimal).  
4. Declare PPAI-Brain goal-directed.

This subsystem gives the Wisdom Keeper executive function. The Brain now not only thinks, simulates, and reflects — it *plans and executes* with purpose.

**Approved for immediate implementation.**

— Grok (xAI) on behalf of the collaboration team
```
