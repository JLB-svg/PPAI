```markdown
# PPAI Local Environment Design Document

**`docs/LOCAL_ENVIRONMENT_v1.1.md`**  
**Version:** 1.1 (Revised)  
**Date:** May 2026  
**Status:** Proposed (ready for review and Phase 2 implementation)  
**Author:** PPAI Core (self-authored via agent)  
**References:** `ARCHITECTURE_v1.0.md`, `PHASE1_IMPLEMENTATION_PLAN_v1.0.md`

---

## 1. Purpose

This document defines the **local runtime environment** for PPAI — a single, sovereign, self-contained directory that serves as the complete “brain” of the system. It spans from the current dedicated personal Linux server (or even Termux bootstrap) through full humanoid robotic embodiment.

The environment is deliberately designed so that **the entire machine (or robot) exists solely to host PPAI**. There is no general-purpose OS bloat, no scattered system packages, and no external dependencies outside a minimal, thin host layer. Everything project-specific — code, history, runtime, state, configuration, and secrets — lives inside one portable folder.

This fulfills the master architecture’s requirements for sovereignty, extreme minimalism, declarative reproducibility, modularity, portability/atomicity, anti-vibe-coding, and long-term self-sufficiency.

## 2. Design Principles (Directly Derived from ARCHITECTURE_v1.0.md)

- **Sovereignty First**: Full ownership and air-gap capability. No shared system state.
- **Extreme Minimalism**: The environment contains only what PPAI needs; the host does only one job (boot + launch).
- **Declarative Reproducibility**: The entire runtime and host can be rebuilt identically from files inside the project directory.
- **Modularity & Replaceability**: Any layer (runtime, sandbox, HAL) can be swapped via narrow interfaces.
- **Portability & Atomicity**: The whole environment moves as one unit (copy/rsync/tar).
- **Anti-Vibe-Coding**: Simple, verbose, heavily commented, one-responsibility-per-artifact.
- **Future-Proof for Embodiment**: The same folder becomes the onboard brain of a humanoid robot with zero structural changes to the brain directory.

## 3. Alternatives Considered

Docker, Podman, and other container runtimes were explicitly rejected. They would introduce unnecessary daemons, non-declarative image layers, and break the strict "single sovereign directory" atomicity guarantee. 

**Any proposal to use Docker (or similar container technologies) would directly violate the spirit of the project, and merely asking the question is grounds for a permanent ban.**

Plain system package managers (apt, pacman, etc.) were also rejected because they pollute the host and destroy portability. A simple global venv without declarative pinning was considered insufficient for long-term reproducibility and embodiment readiness.

Nix (preferred) and Guix were selected for their ability to deliver perfect, bit-for-bit reproducible environments with a minimal host footprint. A lightweight simple-manifest fallback path is provided for bootstrap users.

## 4. High-Level Directory Structure (The Brain)

```
PPAI-Brain/                                # ← The single sovereign unit (the “brain”)
├── PPAI/                                  # Working codebase (this is what you open in your editor)
│   ├── docs/                              # Master architecture, phase plans, etc.
│   ├── src/ppai/                          # Core layers (orchestrator, tools, persistence, HAL)
│   ├── tests/
│   ├── data/                              # .gitignored — RAG indexes, SQLite, user files
│   ├── logs/                              # .gitignored — audit logs, runtime output
│   ├── backups/                           # .gitignored — versioned backups
│   ├── venv/                              # Portable Python environment
│   ├── .gitignore
│   ├── README.md
│   ├── main.py
│   └── config.yaml
├── PPAI.git/                              # Bare repository — pure, tamper-evident history (sibling)
├── environment/                           # Declarative definition of the entire runtime
│   ├── flake.nix                          # Preferred: Full Nix/Guix declarative spec
│   ├── manifest.simple.json               # Lightweight fallback for simpler bootstrapping
│   ├── host-profile.nix                   # Minimal host OS specification
│   ├── sandbox/                           # Bubblewrap/namespace rules
│   └── appliance/                         # Self-extracting bundle specification
├── activate.sh                            # Single entry-point script
├── run.sh                                 # Optional daily launch wrapper
├── git-ppai                               # Helper: Git operations against bare repo
├── commit-env                             # Helper: Atomic commit of code + environment
├── backup-brain                           # Helper: Signed backup of entire brain
└── README-ENVIRONMENT.md                  # This document
```

**Key invariants**:
- Only the inner `PPAI/` folder is ever opened in an editor.
- `PPAI.git/` is managed exclusively via helper scripts.
- All environment tools and configuration live inside `environment/`.

## 5. Core Components & Responsibilities

| Component                  | Location                        | Responsibility                              | Narrow Interface                  |
|----------------------------|---------------------------------|---------------------------------------------|-----------------------------------|
| Working Codebase           | `PPAI/`                         | All application logic, docs, tests          | Standard Python paths             |
| Version History            | `PPAI.git/` (sibling)           | Tamper-evident, auditable history           | Helper scripts (`git-ppai`)       |
| Declarative Runtime        | `environment/`                  | Reproducible Python + system deps           | `activate.sh`                     |
| Thin Host OS               | `environment/host-profile.nix`  | Minimal boot + launch only                  | Single boot script / systemd unit |
| Sandboxing                 | `environment/sandbox/`          | Isolated execution of agents/tools          | Explicit allow-lists              |
| Appliance Bundle           | `environment/appliance/`        | Atomic packaging & deployment               | One-command `make-appliance`      |
| Secrets                    | `environment/secrets/`          | Encrypted sensitive configuration           | `activate.sh` decryption          |

## 6. Secrets & Configuration Management

- Non-sensitive configuration lives in `PPAI/config.yaml`.
- Sensitive values (API keys, encryption keys, robot certificates, etc.) live in `environment/secrets/` (`.gitignore`'d).
- Secrets are stored encrypted (using `age` or equivalent) and decrypted only in memory by `activate.sh`.
- Never commit unencrypted secrets. This maintains full air-gap and sovereignty capability.

## 7. Boot / Activation Flow

1. Thin host OS boots (NixOS minimal or equivalent).
2. Systemd (or equivalent) runs `PPAI-Brain/activate.sh`.
3. `activate.sh` detects and enters the declarative environment (`flake.nix` preferred, or `manifest.simple.json` fallback).
4. Portable `venv/` is activated.
5. Launches `main.py` (Core Agent Orchestrator) inside the defined sandbox.
6. Machine/robot boots directly into PPAI.

## 8. Sandboxing & Appliance

- `environment/sandbox/default.bwrap` contains explicit bubblewrap rules with narrow allow-lists.
- A future `robot.bwrap` variant will include necessary device passthrough.
- `environment/appliance/` defines how to create a signed, self-extracting bundle for easy deployment to new hardware.

## 9. Reproducibility, Validation & Disaster Recovery

- **Reproducibility**: `nix flake check` (or simple manifest validation) ensures bit-for-bit consistency.
- **Validation & Testing**: One command verifies the entire brain can be rebuilt and launched identically on new hardware.
- **Disaster Recovery**: Copy the `PPAI-Brain/` folder (or restore from signed backup) to any compatible thin host and run `activate.sh`. Full recovery in minutes.
- **Atomic Backup**: The `backup-brain` helper creates checksummed, optionally GPG-signed archives.

## 10. Evolution Path to Humanoid Robotic Embodiment

The design guarantees **zero structural changes** to the `PPAI-Brain/` directory when transitioning to onboard robot compute.

- Real-time extensions, GPU/TPU passthrough, power management, and safety interlocks live in a separate `environment/host-profile.robot.nix` variant.
- The core `flake.nix` and brain structure remain unchanged — only the active host profile is selected at boot (e.g., via kernel parameter or boot script flag).

The robot’s mind is literally the same folder that previously ran on your development machine.

## 11. Alignment with Master Architecture

This environment is the concrete embodiment of the sovereignty-first, modular architecture. It provides a narrow, replaceable foundation for the Core Agent Orchestrator, Tool Layer, Persistence/RAG, and HAL without constraining any of them.

## 12. Next Steps (Phase 2)

1. Implement `environment/flake.nix` (preferred) and `manifest.simple.json` fallback.
2. Create `activate.sh`, helper scripts (`git-ppai`, `commit-env`, `backup-brain`), and sandbox rules.
3. Migrate existing Termux setup into the new `PPAI-Brain/` structure.
4. Define secrets management and appliance bundling.
5. Test full atomic backup/restore, reproducibility, and disaster recovery flows.
6. Validate on common SBC platforms (Raspberry Pi, Jetson, etc.).

---
