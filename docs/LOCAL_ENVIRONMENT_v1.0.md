```markdown
# PPAI Local Environment Design Document
**`docs/LOCAL_ENVIRONMENT_v1.0.md`**  
**Version:** 1.0  
**Date:** May 2026  
**Status:** Proposed (ready for review and Phase 2 implementation)  
**Author:** PPAI Core (self-authored via agent)  
**References:** `ARCHITECTURE_v1.0.md`, `PHASE1_IMPLEMENTATION_PLAN_v1.0.md`

---

## 1. Purpose

This document defines the **local runtime environment** for PPAI — a single, sovereign, self-contained directory that serves as the complete “brain” of the system from the current dedicated personal Linux server through full humanoid robotic embodiment.  

The environment is deliberately designed so that **the entire machine (or robot) exists solely to host PPAI**. There is no general-purpose OS bloat, no scattered system packages, and no external dependencies outside a minimal, thin host layer. Everything project-specific — code, history, runtime, state, and configuration — lives inside one portable folder.

This fulfills the master architecture’s requirements for extreme modularity, sovereignty, anti-feature-creep, one-responsibility-per-layer, and long-term self-sufficiency.

## 2. Design Principles (Directly Derived from ARCHITECTURE_v1.0.md)

- **Sovereignty First**: Full ownership and air-gap capability. No shared system state.
- **Extreme Minimalism**: The environment contains only what PPAI needs; the host does only one job (boot + launch).
- **Declarative Reproducibility**: The entire runtime and host can be rebuilt identically from files inside the project directory.
- **Modularity & Replaceability**: Any layer (runtime, HAL, sandbox) can be swapped via narrow interfaces.
- **Portability & Atomicity**: The whole environment moves as one unit (copy/rsync/tar).
- **Anti-Vibe-Coding**: Simple, verbose, heavily commented, one-responsibility-per-artifact.
- **Future-Proof for Embodiment**: Designed so the same folder becomes the onboard brain of a humanoid robot without structural changes.

## 3. High-Level Directory Structure (All-in-One Parent)

```
PPAI-Environment/                          # ← The single sovereign unit (the “brain”)
├── PPAI/                                  # Working codebase (editable source + docs)
│   ├── docs/                              # Master architecture, phase plans, etc.
│   ├── src/ppai/                          # Core layers (orchestrator, interfaces, tools, persistence, HAL)
│   ├── tests/
│   ├── data/                              # .gitignored — RAG indexes, SQLite, user files
│   ├── logs/                              # .gitignored — audit logs, runtime output
│   ├── backups/                           # .gitignored — versioned backups
│   ├── venv/                              # Portable Python environment (activated by runtime)
│   ├── .gitignore
│   ├── README.md
│   ├── main.py
│   └── config.yaml.example
├── PPAI.git/                              # Bare repository — pure version history (sibling)
│   ├── objects/
│   ├── refs/
│   └── config
├── environment/                           # Declarative definition of the entire runtime
│   ├── flake.nix                          # Nix (or Guix manifest) — exact Python, Git, deps, etc.
│   ├── host-profile.nix                   # Declarative minimal host OS specification
│   ├── sandbox/                           # Bubblewrap/namespace rules for agent/tool execution
│   └── appliance/                         # Packaging spec for self-extracting bundle
├── activate.sh                            # Single entry-point script (source this or run at boot)
├── run.sh                                 # Optional wrapper for daily CLI/UI launch
└── README-ENVIRONMENT.md                  # This document
```

**Key invariants**:
- Only `PPAI/` is ever opened in an editor.
- `PPAI.git/` is never manually touched.
- All runtime tools live inside the declarative `environment/` layer.

## 4. Core Components & Responsibilities

| Component                  | Location                  | Responsibility                              | Narrow Interface |
|----------------------------|---------------------------|---------------------------------------------|------------------|
| Working Codebase           | `PPAI/`                   | All application logic, docs, tests          | Standard Python import paths |
| Version History            | `PPAI.git/` (sibling)     | Tamper-evident, auditable history           | Git CLI / bare repo URL |
| Declarative Runtime        | `environment/flake.nix`   | Reproducible Python + deps + Git            | Nix develop shell |
| Thin Host OS               | `environment/host-profile.nix` | Minimal boot + launch only               | Single systemd unit / boot script |
| Sandboxing                 | `environment/sandbox/`    | Isolated execution of agents/tools          | Explicit allow-lists |
| Appliance Bundle           | `environment/appliance/`  | Atomic packaging for deployment/backup      | One-command build |
| Hardware Abstraction Layer | `src/ppai/hal/` (inside PPAI/) | Robot/sensor/motor abstraction            | AbstractHAL interface |

## 5. Boot / Activation Flow (Dedicated Machine or Robot)

1. Thin host OS boots (NixOS minimal profile or equivalent).
2. Single systemd unit runs `PPAI-Environment/activate.sh`.
3. `activate.sh` enters the declarative Nix shell (or Guix equivalent) defined in `environment/flake.nix`.
4. The portable `venv/` is activated.
5. `main.py` (or NiceGUI/Gradio/Kotlin wrapper) launches the Core Agent Orchestrator.
6. All subsequent execution stays inside the sandboxed, project-owned runtime.

Result: The machine/robot boots directly into PPAI with zero manual steps.

## 6. Reproducibility & Atomic Operations

- **Full rebuild**: `nix build` (or equivalent) from the `environment/` directory produces an identical runtime anywhere.
- **Backup/Restore**: Copy the entire `PPAI-Environment/` folder → atomic, verifiable restore.
- **Versioning**: Every change to code, config, or environment spec is committed via the sibling bare repo.
- **Appliance artifact**: One command produces a signed, self-extracting bundle for flashing new hardware or robots.

## 7. Evolution Path to Humanoid Robotic Embodiment

The design requires **zero structural changes** when moving from dedicated server to onboard robot compute:

- **Phase 3 (networked)**: HAL uses network transport; environment stays on server.
- **Phase 4+ (onboard)**: `PPAI-Environment/` is copied to the robot’s edge computer. The same thin host boots the same declarative runtime.
- HAL layer expands in place (`src/ppai/hal/robot/` implementation) to handle motors, sensors, vision, locomotion, and safety.
- Real-time extensions and power management are added inside the declarative `environment/` spec only.
- The robot’s “mind” is literally the same folder that ran on your Termux Pixel 6 Pro and dedicated server — now embodied.

This makes PPAI the **first** personal AI whose brain is designed from day one to become the literal software mind of a humanoid.

## 8. Alignment with Master Architecture

This local environment is not an add-on — it **is** the concrete realization of the layered, modular, sovereignty-first architecture defined in `ARCHITECTURE_v1.0.md`. Every principle is preserved and strengthened:
- Core Agent Orchestrator, LLM backend, Persistence/RAG, Tool Layer, and HAL remain untouched.
- The environment provides the narrow, replaceable foundation those layers sit on.
- Future phases (air-gapping, multi-robot swarms, etc.) are enabled, not constrained.

## 9. Next Steps (Phase 2)

1. Add this document to `docs/`.
2. Implement the declarative `environment/flake.nix` (Nix preferred for maturity in 2026).
3. Create `activate.sh` and minimal host profile.
4. Migrate current Termux setup into the new `PPAI-Environment/` structure.
5. Test atomic backup/restore and appliance bundling.

---
