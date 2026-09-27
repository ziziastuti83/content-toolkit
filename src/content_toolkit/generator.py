import re

from .models import ContentBrief
from .templates import PLATFORM_CTA, PLATFORM_STYLE, TITLE_PATTERNS

SUPPORTED_PLATFORMS = tuple(PLATFORM_CTA)


def _clean_topic(topic: str) -> str:
    return re.sub(r"\\s+", " ", topic).strip()


def _slug_words(topic: str) -> list[str]:
    return re.findall(r"[a-z0-9]+", topic.lower())


def _hashtags(topic: str) -> list[str]:
    words = _slug_words(topic)
    compact = "".join(words)
    tags = [f"#{word.capitalize()}" for word in words if len(word) > 2]
    tags.extend(["#ContentCreator", "#NewContent", "#Trending"])
    if compact:
        tags.insert(0, f"#{compact.capitalize()}")
    return list(dict.fromkeys(tags))[:12]


def _keywords(topic: str) -> list[str]:
    base = [
        topic.lower(),
        f"{topic.lower()} mix",
        f"{topic.lower()} 2026",
        f"best {topic.lower()}",
        f"{topic.lower()} playlist",
        f"{topic.lower()} vibes",
    ]
    base.extend(_slug_words(topic))
    return list(dict.fromkeys(base))[:12]


def generate_brief(topic: str, platform: str = "youtube") -> ContentBrief:
    topic = _clean_topic(topic)
    platform = platform.lower().strip()
    if not topic:
        raise ValueError("Topic cannot be empty.")
    if platform not in SUPPORTED_PLATFORMS:
        supported = ", ".join(SUPPORTED_PLATFORMS)
        raise ValueError(f"Unsupported platform '{platform}'. Choose from: {supported}")
    titles = [pattern.format(topic=topic) for pattern in TITLE_PATTERNS[platform]]
    style = PLATFORM_STYLE[platform]
    description = (
        f"{topic} is a {style} content concept designed to give viewers a clear reason "
        f"to stop, watch, and engage. Keep the opening focused on the main value, match "
        f"the visual style to the topic, and deliver the strongest idea early."
    )
    thumbnail = (
        f"Create a high-contrast thumbnail focused on '{topic}'. Use one clear visual "
        f"subject, strong depth, readable typography, and a clean composition with "
        f"generous safe margins. Avoid clutter and unsupported claims."
    )
    return ContentBrief(topic, platform, titles, description, PLATFORM_CTA[platform], _hashtags(topic), _keywords(topic), thumbnail)
