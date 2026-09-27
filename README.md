# Content Toolkit

A professional, dependency-free CLI for generating structured social-media content briefs from a single topic.

## Features
- Structured content briefs from one topic
- Five title variants per platform
- Platform-aware CTA suggestions
- Hashtags and keyword generation
- Thumbnail concept generation
- JSON export for automation
- Clean CLI with validation
- Unit tests and GitHub Actions CI
- No API keys or external services required

## Requirements
- Python 3.11+
- No runtime dependencies

## Quick start

~~~bash
git clone https://github.com/ziziastuti83/content-toolkit.git
cd content-toolkit
python -m venv .venv
# Windows: .venv\\Scripts\\activate
# macOS/Linux: source .venv/bin/activate
python -m pip install -e ".[dev]"
content-toolkit "Night Drive Music" --platform youtube
~~~

Run as a module:
~~~bash
python -m content_toolkit "Night Drive Music" --platform youtube
~~~

Export JSON:
~~~bash
content-toolkit "Night Drive Music" --platform youtube --json
content-toolkit "Night Drive Music" --platform youtube --json --output result.json
~~~

Supported platforms: YouTube, Facebook, Instagram, TikTok.

## Project structure
~~~text
content-toolkit/
├── .github/workflows/ci.yml
├── src/content_toolkit/
│   ├── __init__.py
│   ├── __main__.py
│   ├── cli.py
│   ├── generator.py
│   ├── models.py
│   └── templates.py
├── tests/test_generator.py
├── .gitignore
├── LICENSE
├── pyproject.toml
└── README.md
~~~

## Design principles
1. Local first: core generation works offline.
2. Deterministic: the same input produces the same package.
3. Composable: generation logic is separated from the CLI.
4. Extensible: richer providers can be added later.
5. Honest: generated content is not presented as a guarantee of virality or ranking.

## Development
~~~bash
python -m pytest
python -m compileall src
ruff check .
ruff format --check .
~~~

## Roadmap
- Custom YAML/JSON template packs
- More platform presets
- Optional AI provider adapters
- Keyword scoring integrations
- CSV batch generation
- Plugin architecture

## License
MIT. See LICENSE.
