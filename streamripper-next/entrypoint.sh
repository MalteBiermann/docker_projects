#!/usr/bin/env bash
set -e

mkdir -p /var/lib/streamripper /data /var/log/streamripper
chown -R appuser:appuser /var/lib/streamripper /data /var/log/streamripper

# Initial schedule generation (non-fatal)
/usr/local/bin/python /app/src/fetch_schedule.py \
  --config /config/stations.yaml \
  --out /var/lib/streamripper/schedule.json || true

/usr/local/bin/python /app/src/plan_jobs.py \
  --config /config/stations.yaml \
  --schedule /var/lib/streamripper/schedule.json \
  --cron /etc/cron.d/streamripper || true

# Nightly refresh at 02:00
cat <<'EOF' > /etc/cron.d/nightly
0 2 * * * root /usr/local/bin/python /app/src/nightly.py --config /config/stations.yaml --schedule /var/lib/streamripper/schedule.json --cron /etc/cron.d/streamripper >> /var/log/streamripper/nightly.log 2>&1
EOF

chmod 0644 /etc/cron.d/nightly /etc/cron.d/streamripper || true

touch /var/log/streamripper/cron.log

cron -f
