# Streamripper Next

This container scrapes a station's programme page nightly, matches episodes by name, and creates cron entries to record audio streams as MP3 files.

## How it works

1. **Nightly (02:00)** the container runs `fetch_schedule.py` to scrape the schedule page.
2. `plan_jobs.py` creates cron entries for matching episodes.
3. Cron runs `record.py` at the episode start time and saves the MP3 to `/data`.

## Configure

Edit `config/stations.yaml`:

- `timezone`: must match the container `TZ` (one timezone per container).
- `episode_match`: regex to match the episode title.
- `parser`: CSS selectors for the schedule page.

If the schedule page uses JavaScript rendering, you will need to replace the scraper with Playwright.

## Run

```
docker compose up -d --build
```

Recordings will be stored in `apps/streamripper-next/data`.
Logs are in `apps/streamripper-next/logs`.

## Notes

- The cron file is regenerated nightly and contains one-off entries for the next day.
- The current implementation expects times like `HH:MM`. Adjust `time_format` if needed.
- For multiple timezones, run multiple containers with different `TZ` values.
