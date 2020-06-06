# Build with:
#     docker build --tag=andremiras/gitpop2 .
#
# Run e.g. tests with:
#     docker run -it --rm andremiras/gitpop2 /bin/sh -c 'make test'
#
# Or for interactive shell:
#     docker run -it --rm andremiras/gitpop2

FROM python:3.8-slim

ENV USER="user"
ENV HOME_DIR="/home/${USER}"
ENV WORK_DIR="${HOME_DIR}" \
    PATH="${HOME_DIR}/.local/bin:${PATH}"

# install dependencies and configure locale
RUN apt update -qq > /dev/null && apt --yes install -qq --no-install-recommends \
    curl \
    locales \
    make \
    sudo \
    && locale-gen en_US.UTF-8 \
    && apt --yes autoremove && apt --yes clean

ENV LANG="en_US.UTF-8" \
    LANGUAGE="en_US.UTF-8" \
    LC_ALL="en_US.UTF-8"

# prepare non root env
RUN useradd --create-home --shell /bin/bash ${USER}

# with sudo access and no password
RUN usermod -append --groups sudo ${USER}
RUN echo "%sudo ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers

WORKDIR ${WORK_DIR}
COPY --chown=user:user . ${WORK_DIR}
USER ${USER}

# setup virtualenv
RUN make virtualenv

CMD venv/bin/gunicorn gitpop2.wsgi:application --bind 0.0.0.0:$PORT
