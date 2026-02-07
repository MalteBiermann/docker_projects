#FROM continuumio/miniconda3
#FROM conda-forge/mambaforge-pypy3
FROM mambaorg/micromamba as micromamba

WORKDIR /app

# Create the environment:
COPY --chown=$MAMBA_USER:$MAMBA_USER environment.yml .
#RUN conda update --all
#RUN conda env create -f environment.yml && \
	#conda clean -afy

RUN micromamba install -y -n base -f environment.yml && \
	micromamba clean --all --yes

# Make RUN commands use the new environment:
#SHELL ["conda", "run", "-n", "myenv", "/bin/bash", "-c"]

# The code to run when container is started:
COPY run.py .
#ENTRYPOINT ["conda", "run", "--no-capture-output", "-n", "myenv", "python", "run.py"]

ARG MAMBA_DOCKERFILE_ACTIVATE=1
# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1
# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

#RUN python -u --version 
#ENTRYPOINT ["/usr/local/bin/_entrypoint.sh", "python", "-u", "run.py"]


#COPY --from=micromamba /app /app
#WORKDIR /app
#COPY model.pkl .
#CMD ["python", "-u", "run.py"]
