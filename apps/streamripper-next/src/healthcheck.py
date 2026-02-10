from __future__ import annotations

import os
import sys


def _cron_running() -> bool:
    proc_root = "/proc"
    try:
        for pid in os.listdir(proc_root):
            if not pid.isdigit():
                continue
            cmdline_path = os.path.join(proc_root, pid, "cmdline")
            try:
                with open(cmdline_path, "rb") as handle:
                    raw = handle.read().decode("utf-8", errors="ignore")
            except OSError:
                continue
            if "cron" in raw:
                return True
    except FileNotFoundError:
        return False
    return False


def main() -> int:
    if _cron_running():
        return 0
    return 1


if __name__ == "__main__":
    sys.exit(main())
