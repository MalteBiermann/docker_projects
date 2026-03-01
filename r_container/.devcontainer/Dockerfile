# FROM ghcr.io/rocker-org/devcontainer/tidyverse:4.4
# FROM rocker/r-bspm:latest
FROM rocker/r-ver:4.4.3

# RUN mkdir -p /home/rstudio/workspace
# WORKDIR /home/rstudio/workspace
# COPY ./Sediment_Timeseries_clean_current.R .

RUN apt-get update \
	&& apt-get install -y python3-pip \
	build-essential libcurl4-gnutls-dev libxml2-dev libssl-dev \
	libfreetype6-dev libharfbuzz-dev libfribidi-dev fontconfig-config \
	&& rm -rf /var/lib/apt/lists/*

# ENV PASSWORD='rstudio'

RUN pip install --break-system-packages radian
RUN R -e "install.packages('renv', repos = c(CRAN = 'https://cloud.r-project.org'))"
RUN R -e "install.packages('httpgd', repos = c('https://community.r-multiverse.org', 'https://cloud.r-project.org'))"
RUN R -e "install.packages('languageserver', repos = 'https://cloud.r-project.org')"

# EXPOSE 8787
CMD ["/bin/bash"]