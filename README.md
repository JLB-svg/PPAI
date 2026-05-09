# Personal Private AI (PPAI)

**Sovereign, on-device Intelligence Amplifier and Wisdom Keeper**

See the constitution:
- `docs/ARCHITECTURE_v1.0.md`
- `docs/PHASE1_IMPLEMENTATION_PLAN_v1.0.md`

## Quick Start (Termux bootstrap – temporary)

```bash
source venv/bin/activate
pip install -r requirements.txt
cp config.yaml.example config.yaml
# edit config.yaml with your Grok API key
python -m src.ppai.main   # (once we refactor)

s -la
ls -la
