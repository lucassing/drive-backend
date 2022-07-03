FROM python:3.10.5-buster

ENV PYTHONUNBUFFERED=1 \
    POETRY_VERSION=1.1.13

RUN echo $POETRY_VERSION

# System deps:
RUN pip install "poetry==$POETRY_VERSION"

# Copy only requirements to cache them in docker layer
WORKDIR /code
COPY poetry.lock pyproject.toml /code/

#Set workdir to src
WORKDIR /code/src

# Project initialization:
RUN poetry config virtualenvs.create false \
  && poetry install $(test "$YOUR_ENV" == production && echo "--no-dev") --no-interaction --no-ansi