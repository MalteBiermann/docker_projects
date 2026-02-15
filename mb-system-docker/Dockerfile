FROM python:3.13.6-bullseye

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Install pip requirements
# COPY requirements.txt .
# RUN python -m pip install -r requirements.txt

# WORKDIR /app
# COPY . /app

# Creates a non-root user with an explicit UID and adds permission to access the /app folder
# For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers
# RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
# USER appuser

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
# CMD ["python", "-m", "app.py"]

RUN apt-get update
# Install required dependencies
RUN apt-get install -y build-essential cmake libcurl4-gnutls-dev libnetcdf-dev libgdal-dev git
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

RUN apt-get clean -y

RUN git clone --depth 50 https://github.com/GenericMappingTools/gmt.git
# RUN ["set", "(CMAKE_INSTALL_PREFIX '/opt/gmt')"]
WORKDIR /gmt
RUN mkdir build && cd build && cmake ..
WORKDIR /gmt/build
RUN cmake --build .
RUN cmake --build . --target install

# mb-system deps
RUN apt-get install -y libx11-dev libxt-dev
RUN apt-get clean -y

WORKDIR /
RUN git clone https://github.com/dwcaress/MB-System.git
WORKDIR /MB-System
RUN ./configure
RUN make

# RUN mkdir /app
# RUN adduser -u 2001 --disabled-password --gecos "" appuser && chown -R appuser /app
# USER appuser
# RUN pip install --upgrade pip
# RUN pip install pygmt

# WORKDIR /app
# COPY app.py .

CMD ["/bin/bash"]