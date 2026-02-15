# AdGuard Home (Docker)

This setup uses host networking and reads settings from the local `.env` file.

## Quick start

1. Update `.env` with your timezone and desired admin credentials.
2. Start the stack:
   ```sh
   docker compose up -d
   ```
3. Open the web UI at `http://<host-ip>:3000` and complete the initial setup.

## Notes

- Host networking is supported on Linux. Docker Desktop for macOS does not support host networking.
- If you are on macOS, switch back to port mappings by removing `network_mode: "host"` and adding explicit `ports` in the compose file.
- AdGuard Home stores its runtime data in `./data` and configuration in `./config`.
- AdGuard Home does not read admin credentials from environment variables; set them during first-run in the web UI and keep the values in `.env` for your records.
