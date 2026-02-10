from __future__ import annotations

import argparse
import json
from datetime import datetime, timedelta, timezone
from typing import Any, Dict, List
from zoneinfo import ZoneInfo

import requests
from bs4 import BeautifulSoup

from config import load_config


def _target_date(tz: str, schedule_is_for: str) -> str:
    now = datetime.now(ZoneInfo(tz))
    if schedule_is_for == "today":
        target = now.date()
    else:
        target = (now + timedelta(days=1)).date()
    return target.isoformat()


def _parse_station(station) -> Dict[str, Any]:
    parser = station.parser
    if not parser or not station.schedule_url:
        return {
            "name": station.name,
            "timezone": station.timezone,
            "stream_url": station.stream_url,
            "entries": [],
        }

    resp = requests.get(station.schedule_url, timeout=30)
    resp.raise_for_status()

    soup = BeautifulSoup(resp.text, "html.parser")
    items = soup.select(parser.item_selector)

    date_str = _target_date(station.timezone, parser.schedule_is_for)
    entries: List[Dict[str, Any]] = []

    for item in items:
        title_el = item.select_one(parser.title_selector)
        time_el = item.select_one(parser.time_selector)
        if not title_el or not time_el:
            continue
        title = " ".join(title_el.get_text(strip=True).split())
        time_text = " ".join(time_el.get_text(strip=True).split())
        if not title or not time_text:
            continue

        normalized_time = time_text
        candidate_time = time_text
        if "-" in time_text:
            candidate_time = time_text.split("-")[0].strip()
        try:
            parsed_time = datetime.strptime(candidate_time, parser.time_format)
            normalized_time = parsed_time.strftime("%H:%M")
        except ValueError:
            pass

        entries.append(
            {
                "title": title,
                "start_time": normalized_time,
                "date": date_str,
            }
        )

    return {
        "name": station.name,
        "timezone": station.timezone,
        "stream_url": station.stream_url,
        "entries": entries,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", required=True)
    parser.add_argument("--out", required=True)
    args = parser.parse_args()

    cfg = load_config(args.config)
    stations = [_parse_station(station) for station in cfg.stations]

    payload = {
        "generated_at": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        "stations": stations,
    }

    with open(args.out, "w", encoding="utf-8") as handle:
        json.dump(payload, handle, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    main()
