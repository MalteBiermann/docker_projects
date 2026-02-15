from __future__ import annotations

import argparse
import subprocess
import sys


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", required=True)
    parser.add_argument("--schedule", required=True)
    parser.add_argument("--cron", required=True)
    args = parser.parse_args()

    subprocess.run(
        [
            sys.executable,
            "/app/src/fetch_schedule.py",
            "--config",
            args.config,
            "--out",
            args.schedule,
        ],
        check=False,
    )

    subprocess.run(
        [
            sys.executable,
            "/app/src/plan_jobs.py",
            "--config",
            args.config,
            "--schedule",
            args.schedule,
            "--cron",
            args.cron,
        ],
        check=False,
    )


if __name__ == "__main__":
    main()
