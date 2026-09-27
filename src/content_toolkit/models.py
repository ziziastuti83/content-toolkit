from dataclasses import asdict, dataclass
from typing import Any


@dataclass(frozen=True)
class ContentBrief:
    topic: str
    platform: str
    titles: list[str]
    description: str
    cta: str
    hashtags: list[str]
    keywords: list[str]
    thumbnail: str

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)
