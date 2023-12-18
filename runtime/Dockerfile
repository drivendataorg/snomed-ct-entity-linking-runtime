FROM --platform=linux/amd64 mambaorg/micromamba:1.5.3-bookworm-slim

USER root

ARG CPU_OR_GPU=gpu

ENV DEBIAN_FRONTEND=noninteractive \
    LANG=C.UTF-8  \
    LC_ALL=C.UTF-8 \
    PYTHONUNBUFFERED=1 \
    SHELL=/bin/bash

COPY apt.txt apt.txt
RUN apt-get update --fix-missing \
    && apt-get install -y apt-utils 2> /dev/null \
    && xargs -a apt.txt apt-get install -y \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /apt.txt

COPY --chown=$MAMBA_USER:$MAMBA_USER conda-lock-${CPU_OR_GPU}.yml /tmp/conda-lock.yml
RUN micromamba install --name base --yes --file /tmp/conda-lock.yml && \
    micromamba clean --all --force-pkgs-dirs --yes

RUN mkdir /code_execution
RUN chown -R ${MAMBA_USER}:${MAMBA_USER} /code_execution

COPY tests /code_execution/tests
COPY entrypoint.sh /entrypoint.sh

WORKDIR /code_execution
USER ${MAMBA_USER}

CMD ["bash", "/entrypoint.sh"]
