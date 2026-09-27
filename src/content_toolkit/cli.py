import argparse
import json
from pathlib import Path

from .generator import SUPPORTED_PLATFORMS, generate_brief


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="content-toolkit", description="Generate a structured social-media content brief from one topic.")
    parser.add_argument("topic", help="The content topic to build around.")
    parser.add_argument("--platform", choices=SUPPORTED_PLATFORMS, default="youtube")
    parser.add_argument("--json", action="store_true", help="Print the result as JSON.")
    parser.add_argument("--output", type=Path, help="Write JSON output to a file.")
    return parser


def _render_text(data: dict) -> str:
    lines = ["CONTENT BRIEF", f"Topic: {data['topic']}", f"Platform: {data['platform'].title()}", "", "TITLES"]
    lines.extend(f"{i}. {title}" for i, title in enumerate(data["titles"], 1))
    lines += ["", "DESCRIPTION", data["description"], "", "CTA", data["cta"], "", "HASHTAGS", " ".join(data["hashtags"]), "", "KEYWORDS", ", ".join(data["keywords"]), "", "THUMBNAIL", data["thumbnail"]]
    return "\n".join(lines)


def main() -> None:
    args = build_parser().parse_args()
    try:
        data = generate_brief(args.topic, args.platform).to_dict()
    except ValueError as exc:
        raise SystemExit(f"error: {exc}") from exc
    payload = json.dumps(data, ensure_ascii=False, indent=2)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(payload + "\n", encoding="utf-8")
        print(f"Saved: {args.output}")
    elif args.json:
        print(payload)
    else:
        print(_render_text(data))


if __name__ == "__main__":
    main()
