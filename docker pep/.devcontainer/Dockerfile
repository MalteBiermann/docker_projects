FROM ubuntu:latest

ENV PYTHONUNBUFFERED=1 \
    # prevents python creating .pyc files
    PYTHONDONTWRITEBYTECODE=1 \
    \
    # pip
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    \
    # poetry
    # https://python-poetry.org/docs/configuration/#using-environment-variables
    # POETRY_VERSION=1.0.3 \
    # make poetry install to this location
    # POETRY_HOME="/opt/poetry" \
    # make poetry create the virtual environment in the project's root
    # it gets named `.venv`
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    # do not ask any interactive question
    POETRY_NO_INTERACTION=1
    # \
    # paths
    # this is where our requirements + virtual environment will live
    # PYSETUP_PATH="/opt/pysetup" \
    # VENV_PATH="/opt/pysetup/.venv"


RUN apt-get update

RUN DEBIAN_FRONTEND=noninteractive TZ=Europe/Berlin apt-get -y install tzdata
RUN apt-get install -y python3 pip pipx
RUN apt-get install -y bash git ssh tmux tmate zsh

RUN apt-get clean -y

RUN mkdir /app
# RUN adduser -u 2001 --disabled-password --gecos "" appuser && chown -R appuser /app
# RUN sudo -u appuser ssh-keygen -A -t ed25519
# USER appuser

WORKDIR /app

RUN pipx ensurepath
RUN pipx install poetry
#CMD ["/usr/bin/zsh"]