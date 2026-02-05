# syntax=docker/dockerfile:1

FROM ubuntu:noble@sha256:72297848456d5d37d1262630108ab308d3e9ec7ed1c3286a32fe09856619a782
# ubuntu:noble-20250127

ENV DEBIAN_FRONTEND=noninteractive
ENV TZ=Europe/Berlin

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        cron \
        streamripper \
        tzdata \
    && ln -fs /usr/share/zoneinfo/$TZ /etc/localtime \
    && dpkg-reconfigure --frontend noninteractive tzdata \
    && apt-get clean -y \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*


ARG USERNAME=appuser
ARG USER_UID=1001
ARG USER_GID=$USER_UID
ARG WS='/workspace'

RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m --shell /bin/bash $USERNAME

RUN mkdir -p $WS/streamripper/music

COPY ./startStreamripper.sh $WS/streamripper/
RUN chown -R $USERNAME:$USERNAME $WS/streamripper/*
RUN chmod a+x $WS/streamripper/startStreamripper.sh

COPY ./cronStreamRipper /etc/cron.d/cronStreamRipper
RUN chmod 0644 /etc/cron.d/cronStreamRipper

# EXPOSE 8001

# What the container should run when it is started.
# ENTRYPOINT [ "/bin/hello.sh" ]
# CMD ["--help"]
ENTRYPOINT [ "cron" ]
CMD [ "-f", "-L 15" ]
# CMD ["sh", "startStreamripper.sh"]