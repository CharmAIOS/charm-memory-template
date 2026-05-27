# Charm Memory Storage Template

A starter template for building custom Memory & State backend providers (like Redis, MongoDB, Pinecone) for the Charm ecosystem.

## Setup

```bash
uv venv
source .venv/bin/activate
uv pip install -e .
```

## How it works

1. Open `src/charm_memory_helloworld/store.py` and implement your database client logic in `load_messages` and `save_messages`.
2. Rename the package in `pyproject.toml` (e.g. `charm-memory-redis`).
3. Update the `[project.entry-points."charm.memory"]` with your provider ID (e.g. `redis = ...`).
4. Publish to PyPI.

## Using it in an Agent

Users can opt-in to your memory backend via `charm.yaml`:

```yaml
runtime:
  memory:
    provider: helloworld
    config:
      url: "your-connection-string"
```

## Publish to Charm Store

To let other developers discover your plugin:
1. Fork [charm-community-plugin](https://github.com/CharmAIOS/charm-community-plugin)
2. Add your package to `memory/registry.json`
3. Submit a Pull Request!
