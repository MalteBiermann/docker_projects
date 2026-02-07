FROM python:3.11.3-slim-bullseye
# FROM ubuntu:noble@sha256:72297848456d5d37d1262630108ab308d3e9ec7ed1c3286a32fe09856619a782

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update
# Install required dependencies
RUN apt-get install -y sudo uild-essential cmake libcurl4-gnutls-dev libnetcdf-dev libgdal-dev git
# Install optional dependencies
RUN apt-get install -y gdal-bin libfftw3-dev libpcre3-dev liblapack-dev libblas-dev libglib2.0-dev ghostscript
# to enable movie-making
RUN apt-get install -y graphicsmagick ffmpeg
# to enable document viewing via gmt docs
RUN apt-get install -y xdg-utils
# to enable testing
RUN apt-get install -y graphicsmagick
# to build the documentation
RUN apt-get install -y python3-sphinx

RUN apt-get clean -y \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*


RUN git clone --depth 50 https://github.com/GenericMappingTools/gmt.git
# RUN ["set", "(CMAKE_INSTALL_PREFIX '/opt/gmt')"]
WORKDIR /gmt
RUN mkdir build && cd build && cmake ..
WORKDIR /gmt/build
RUN cmake --build .
RUN cmake --build . --target install

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
RUN pip install --upgrade pip
RUN pip install pygmt

WORKDIR $WS
# COPY app.py .

CMD ["/bin/bash"]