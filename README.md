# docker_projects monorepo

This repository is a monorepo containing multiple Docker-based projects.

## Apps
- [conda-docker](conda-docker)
- [cupsd](cupsd)
- [docker-pep](docker-pep)
- [docker-swarm](docker-swarm)
- [geoserver-docker](geoserver-docker)
- [gmt-docker](gmt-docker)
- [latex](latex)
- [mb-system-docker](mb-system-docker)
- [streamripper](streamripper)
- [texlive-test](texlive-test)
- [ubuntu-dev](ubuntu-dev)

## Notes
- Each app is self-contained. Refer to each app folder for its Dockerfile, compose file, and project-specific README.
- Use per-app .env files where applicable (see .env.example files).
