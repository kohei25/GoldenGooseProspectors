FROM python:3.12.2-bullseye

WORKDIR /app

RUN apt update &&\
    rm -rf ~/.cache &&\
    apt clean all

RUN pip install --upgrade pip
RUN curl -sSL https://install.python-poetry.org | POETRY_VERSION=1.8.0 python3 -

ENV PATH /root/.local/bin:$PATH
RUN poetry config virtualenvs.create false

COPY pyproject.toml poetry.lock ./
RUN poetry install

COPY . .
