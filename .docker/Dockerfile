ARG UNAME=app
ARG UID=1000
ARG GID=1000
ARG PYTHON_VERSION=3.9
ARG POETRY_VERSION=1.0.0

FROM python:$PYTHON_VERSION-slim-bullseye
ARG UNAME \
    UID \
    GID \
    POETRY_VERSION

RUN groupadd -g $GID -o $UNAME && \
    useradd -m -u $UID -g $GID -o -s /bin/bash $UNAME

RUN apt-get update \
  && apt-get clean \
  && apt-get -y install curl libpq-dev

WORKDIR /app

RUN pip install poetry==$POETRY_VERSION

COPY poetry.lock pyproject.toml ./

RUN poetry export --dev --without-hashes --format requirements.txt > requirements.txt \
    && pip install --no-cache-dir -r requirements.txt

COPY --chown=app:app . .

USER app
