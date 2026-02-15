from __future__ import annotations

import argparse
import re
import subprocess
from datetime import datetime
from pathlib import Path


def _safe_name(value: str) -> str:
    cleaned = re.sub(r"[^A-Za-z0-9._-]+", "_", value).strip("_")
    return cleaned or "recording"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--station", required=True)
    parser.add_argument("--stream", required=True)
    parser.add_argument("--title", required=True)
    parser.add_argument("--duration", type=int, required=True, help="minutes")
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    now = datetime.now()
    date_prefix = now.strftime("%Y%m%d_%H%M")
    filename = f"{date_prefix}_{_safe_name(args.station)}_{_safe_name(args.title)}.mp3"

    output_dir = Path(args.output)
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / filename

    duration_seconds = max(args.duration, 1) * 60

    cmd = [
        "ffmpeg",
        "-y",
        "-i",
        args.stream,
        "-t",
        str(duration_seconds),
        "-c:a",
        "copy",
        str(output_path),
    ]

    subprocess.run(cmd, check=False)


if __name__ == "__main__":
    main()
