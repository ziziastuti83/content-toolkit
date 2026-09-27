import pytest

from content_toolkit.generator import generate_brief


def test_generate_youtube_brief():
    brief = generate_brief("Night Drive Music", "youtube")
    assert brief.topic == "Night Drive Music"
    assert brief.platform == "youtube"
    assert len(brief.titles) == 5
    assert "#NightDriveMusic" in brief.hashtags
    assert "night drive music" in brief.keywords


def test_platform_is_case_insensitive():
    assert generate_brief("Morning Motivation", "YOUTUBE").platform == "youtube"


def test_empty_topic_is_rejected():
    with pytest.raises(ValueError, match="Topic cannot be empty"):
        generate_brief("   ")


def test_unknown_platform_is_rejected():
    with pytest.raises(ValueError, match="Unsupported platform"):
        generate_brief("Test", "unknown")
