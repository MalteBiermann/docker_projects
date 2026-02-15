from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List

import yaml


@dataclass
class StationParser:
    item_selector: str
    title_selector: str
    time_selector: str
    time_format: str = "%H:%M"
    schedule_is_for: str = "tomorrow"


@dataclass
class StationConfig:
    name: str
    timezone: str
    schedule_url: str
    stream_url: str
    episode_match: str
    default_duration_minutes: int = 60
    parser: StationParser | None = None


@dataclass
class AppConfig:
    stations: List[StationConfig]


def load_config(path: str | Path) -> AppConfig:
    data: Dict[str, Any] = yaml.safe_load(Path(path).read_text()) or {}
    stations_data = data.get("stations", [])
    stations: List[StationConfig] = []
    for item in stations_data:
        parser_data = item.get("parser")
        parser = None
        if parser_data:
            parser = StationParser(
                item_selector=parser_data.get("item_selector", ""),
                title_selector=parser_data.get("title_selector", ""),
                time_selector=parser_data.get("time_selector", ""),
                time_format=parser_data.get("time_format", "%H:%M"),
                schedule_is_for=parser_data.get("schedule_is_for", "tomorrow"),
            )
        stations.append(
            StationConfig(
                name=item.get("name", "Unnamed Station"),
                timezone=item.get("timezone", "UTC"),
                schedule_url=item.get("schedule_url", ""),
                stream_url=item.get("stream_url", ""),
                episode_match=item.get("episode_match", ".*"),
                default_duration_minutes=int(item.get("default_duration_minutes", 60)),
                parser=parser,
            )
        )
    return AppConfig(stations=stations)
