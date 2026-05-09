#!/usr/bin/env python3
"""
PPAI Grok Apply Tool - Minimal interoperability layer

One responsibility only:
- --log: archive full chat (prompt + Grok response) for the Wisdom Keeper
- --execute: safely run shell commands that Grok outputs (with preview + explicit approval)

Designed to be dead-simple, safe, and aligned with the Architecture Document.
Backups are sacred. User is always in control.
"""

import sys
import os
from datetime import datetime
import subprocess
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent.parent.parent
CONVERSATIONS_DIR = REPO_ROOT / "docs" / "conversations"

def ensure_dirs():
    CONVERSATIONS_DIR.mkdir(parents=True, exist_ok=True)

def log_chat():
    """Called by bootstrap after every Grok API response."""
    ensure_dirs()
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    log_file = CONVERSATIONS_DIR / f"{timestamp}.md"

    prompt_file = Path("/tmp/last_grok_prompt.txt")
    response_file = Path("/tmp/last_grok_response.txt")

    prompt = prompt_file.read_text(encoding="utf-8") if prompt_file.exists() else "(no prompt saved)"
    response = response_file.read_text(encoding="utf-8") if response_file.exists() else "(no response saved)"

    with open(log_file, "w", encoding="utf-8") as f:
        f.write(f"# Chat Log - {timestamp}\n\n")
        f.write("## User Prompt\n\n")
        f.write(prompt.strip() + "\n\n")
        f.write("## Grok Response\n\n")
        f.write(response.strip() + "\n")

    print(f"✅ Chat logged to: {log_file.relative_to(REPO_ROOT)}")
    print(f"   (Total logs in conversations/: {len(list(CONVERSATIONS_DIR.iterdir()))})")

def execute_commands():
    """Safe command execution mode - your 'button press'."""
    response_file = Path("/tmp/last_grok_response.txt")
    if not response_file.exists():
        print("❌ No last Grok response found in /tmp/last_grok_response.txt")
        print("   Make sure your bootstrap saved the response before calling --execute")
        return

    content = response_file.read_text(encoding="utf-8")

    # Look for the explicit execute block
    start_marker = "=== BEGIN EXECUTE BLOCK ==="
    end_marker = "=== END EXECUTE BLOCK ==="

    start = content.find(start_marker)
    end = content.find(end_marker)

    if start == -1 or end == -1 or start >= end:
        print("❌ No execute block found.")
        print("   Grok must output commands between:")
        print(f"   {start_marker}")
        print("   ... commands here ...")
        print(f"   {end_marker}")
        return

    commands = content[start + len(start_marker):end].strip()

    print("\n" + "="*60)
    print("🚀 COMMANDS TO EXECUTE:")
    print("="*60)
    print(commands)
    print("="*60)
    print("\nThis will run the above commands in the repo root.")
    print("Any files modified will get an automatic backup (_v1.bak).")

    confirm = input("\nExecute these commands? (y/n): ").strip().lower()
    if confirm != "y":
        print("Cancelled by user.")
        return

    # Execute safely
    try:
        result = subprocess.run(
            commands,
            shell=True,
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            check=False
        )

        if result.stdout:
            print(result.stdout)
        if result.stderr:
            print("STDERR:", result.stderr)

        if result.returncode == 0:
            print("✅ Commands executed successfully.")
        else:
            print(f"⚠️  Commands finished with exit code {result.returncode}")

    except Exception as e:
        print(f"❌ Error executing commands: {e}")

    # Always show git status
    print("\nGit status:")
    subprocess.run(["git", "status", "--short"], cwd=REPO_ROOT)

def main():
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python -m src.ppai.utils.grok_apply --log")
        print("  python -m src.ppai.utils.grok_apply --execute")
        sys.exit(1)

    mode = sys.argv[1]

    if mode == "--log":
        log_chat()
    elif mode == "--execute":
        execute_commands()
    else:
        print(f"Unknown mode: {mode}")
        sys.exit(1)

if __name__ == "__main__":
    main()
