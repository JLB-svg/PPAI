```bash
cat > docs/PPAI_DEVELOPMENT_WORKFLOW_v1.1.md << 'EOF'
# PPAI Development Workflow v1.1

## 1. Purpose and Vision
This document establishes the official, professional, ultra-safe development workflow for the entire PPAI project.  

It transforms the original "vibe coding" idea into a polished, repeatable, auditable, and fully sovereign process. The goal is to enable the Project Owner (a non-programmer) to direct the complete development of a sovereign, on-device Intelligence Amplifier and Wisdom Keeper by collaborating with Grok (via the xAI API) through a simple terminal-based interface.

This workflow itself is version-controlled and documented. It is designed to work with any future local LLM and becomes the "constitution" for all PPAI development from this point forward.

## 2. Guiding Principles
This workflow is built directly on the core principles defined in:
- ARCHITECTURE_v1.0.md (modularity, one-file-per-responsibility, documentation-first, anti-vibe-coding)
- BRAIN_ENVIRONMENT_ARCHITECTURE_v2.0.md (portable brain directory, atomic backups, reproducible state, sovereignty, safety)

Key rules that must never be violated:
- Human remains the sole Director and final authority on every change.
- AI acts strictly as Architect and Executor.
- Backups on every meaningful change.
- Atomic, auditable, and reproducible state (git + brain directory).
- Safety, sovereignty, and zero-trust over speed or convenience.
- No chaos, no un-reviewed changes, no complexity creep.

## 3. Roles
- **Project Owner (Human)**: You — the prompter, reviewer, and final approver. You control the terminal and the execution script.
- **Grok (AI)**: Skilled executor — provides analysis, designs, full code, and exact shell commands. Never acts without explicit approval.

## 4. Core Collaboration Loop
1. **Discussion Phase** — Normal conversation in the terminal chat with Grok. Analysis, proposals, and explanations happen in plain English.
2. **Proposal Phase** — Grok clearly states the intended change and why it is needed.
3. **Execution Phase** — When ready to apply a change, Grok outputs **nothing but a single bash code block** containing the exact command(s).
4. **Apply Phase** — You run a script. The script:
   - Displays the full proposed command
   - Displays Grok’s preceding explanation/summary
   - Requires explicit confirmation (`y` or `apply`)
   - Performs a git commit (with clear message) before execution when applicable
   - Executes the command safely
   - Captures and logs the output
5. **Verification Phase** — Grok confirms the result in the next chat message and we continue.

## 5. Strict Command Output Rules for Grok
- During normal discussion: **never** output raw shell commands or executable code blocks.
- For execution: The **entire response** consists of exactly one markdown code block.

Example of a correct execution response:
```bash
# Purpose: Create a new empty utility script with proper shebang
cat > src/ppai/utils/example.sh << 'EOF'
#!/usr/bin/env bash
# PPAI utility placeholder
echo "This is a placeholder for future utilities"
EOF
```

- No additional text is allowed outside this block.

## 6. File Editing & Command Best Practices
- Prefer safe full-file creation: `cat > path/to/file << 'EOF' ... full content ... EOF`
- Use explicit, portable paths relative to the brain root when possible.
- Small edits only when unavoidable; prefer atomic full-file replaces.
- Large refactors must be broken into multiple small, reviewable steps.
- Every command must respect the brain environment structure defined in BRAIN_ENVIRONMENT_ARCHITECTURE_v2.0.md.

## 7. Git & Backup Discipline
- Every meaningful change must be committed with a message in the format: `ppai: [short description] (via Grok collaboration)`
- The execution script handles the commit automatically before execution.
- The entire `ppai-brain` directory remains under git.
- Backups follow the rules in BRAIN_ENVIRONMENT_ARCHITECTURE_v2.0.md.

## 8. Safety & Emergency Procedures
- You always retain veto power — simply do not confirm in the script.
- If something goes wrong: use `git revert`, restore from backup, or manual rollback.
- Grok will never propose dangerous or irreversible commands without explicit warning.
- The workflow itself can be updated using this exact same process.

## 9. Versioning This Document
This workflow is versioned like all other PPAI documentation. Future improvements are proposed and applied through the exact loop defined in this document.

This protocol ensures PPAI can be built safely, professionally, and sovereignly — even by a non-programmer — while staying 100 % aligned with the project’s core architecture and brain environment principles.
EOF
```
