FROM python:3.11-slim as requirements-stage

WORKDIR /tmp

RUN apt-get update  \
    && apt-get install -y gcc pkg-config libxml2-dev libxmlsec1-dev libxmlsec1-openssl g++ \
    && apt-get clean

RUN pip3 install --upgrade pip setuptools wheel

COPY pyproject.toml poetry.lock ./
RUN pip3 install poetry
RUN poetry export -f requirements.txt --output requirements.txt --without-hashes

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN pip3 install -r requirements.txt

FROM python:3.11-slim as production

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update  \
    && apt-get install -y libxmlsec1-openssl \
    && apt-get clean

ENV VIRTUAL_ENV=/opt/venv
COPY --from=requirements-stage $VIRTUAL_ENV $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

COPY app .

