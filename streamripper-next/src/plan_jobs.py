from __future__ import annotations

import argparse
import json
import re
import shlex
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List
from zoneinfo import ZoneInfo

from config import load_config


def _load_schedule(path: str) -> Dict[str, Any]:
    if not Path(path).exists():
        return {"stations": []}
    with open(path, "r", encoding="utf-8") as handle:
        return json.load(handle)


def _build_cron_lines(schedule: Dict[str, Any], config) -> List[str]:
    lines: List[str] = []

    for station_cfg in config.stations:
        matcher = re.compile(station_cfg.episode_match, re.IGNORECASE)
        station_schedule = next(
            (s for s in schedule.get("stations", []) if s.get("name") == station_cfg.name),
            None,
        )
        if not station_schedule:
            continue

        for entry in station_schedule.get("entries", []):
            title = entry.get("title", "")
            if not matcher.search(title):
                continue

            date_str = entry.get("date")
            time_str = entry.get("start_time")
            if not date_str or not time_str:
                continue

            try:
                dt = datetime.strptime(
                    f"{date_str} {time_str}",
                    "%Y-%m-%d %H:%M",
                ).replace(tzinfo=ZoneInfo(station_cfg.timezone))
            except ValueError:
                continue

            minute = dt.minute
            hour = dt.hour
            day = dt.day
            month = dt.month

            station_arg = shlex.quote(station_cfg.name)
            stream_arg = shlex.quote(station_cfg.stream_url)
            title_arg = shlex.quote(title)
            duration = station_cfg.default_duration_minutes
            output_arg = shlex.quote("/data")

            line = (
                f"{minute} {hour} {day} {month} * appuser /usr/local/bin/python /app/src/record.py "
                f"--station {station_arg} --stream {stream_arg} --title {title_arg} "
                f"--duration {duration} --output {output_arg} >> /var/log/streamripper/record.log 2>&1"
            )
            lines.append(line)

    if not lines:
        lines.append(
            "# No recordings matched. This file is regenerated nightly."
        )

    return lines


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", required=True)
    parser.add_argument("--schedule", required=True)
    parser.add_argument("--cron", required=True)
    args = parser.parse_args()

    config = load_config(args.config)
    schedule = _load_schedule(args.schedule)
    lines = _build_cron_lines(schedule, config)

    content = "\n".join(lines) + "\n"
    Path(args.cron).write_text(content, encoding="utf-8")


if __name__ == "__main__":
    main()
