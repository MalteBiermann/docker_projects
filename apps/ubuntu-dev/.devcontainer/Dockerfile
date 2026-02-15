FROM ubuntu:noble-20260113

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update

RUN apt-get install -y python3
RUN apt-get install -y bash git ssh tmux zsh sudo curl wget vim nano
# tmate
RUN apt-get install -y tzdata \
    && ln -fs /usr/share/zoneinfo/Europe/Berlin /etc/localtime \
    && dpkg-reconfigure --frontend noninteractive tzdata

RUN apt-get clean -y \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

ARG USERNAME=appuser
ARG USER_UID=1001
ARG USER_GID=$USER_UID
ARG WS='/workspace'


# Create the user
RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m --shell /bin/bash $USERNAME
RUN echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME \
    && chmod 0440 /etc/sudoers.d/$USERNAME

RUN mkdir $WS
RUN chown -R $USERNAME $WS
USER $USERNAME

# WORKDIR $WS
# COPY app.py .

CMD ["/usr/bin/bash"]