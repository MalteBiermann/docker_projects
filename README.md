# docker_projects monorepo

This repository is a monorepo containing multiple Docker-based projects under apps/.

## Apps
- [apps/conda-docker](apps/conda-docker)
- [apps/cupsd](apps/cupsd)
- [apps/docker-pep](apps/docker-pep)
- [apps/docker-swarm](apps/docker-swarm)
- [apps/geoserver-docker](apps/geoserver-docker)
- [apps/gmt-docker](apps/gmt-docker)
- [apps/latex](apps/latex)
- [apps/mb-system-docker](apps/mb-system-docker)
- [apps/streamripper](apps/streamripper)
- [apps/texlive-test](apps/texlive-test)
- [apps/ubuntu-dev](apps/ubuntu-dev)

## Notes
- Each app is self-contained. Refer to each app folder for its Dockerfile, compose file, and project-specific README.
- Use per-app .env files where applicable (see .env.example files).
