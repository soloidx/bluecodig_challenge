FROM python:3.11.3-slim-buster

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN apt-get update \
&& apt-get install gcc --no-install-recommends -y \
&& apt-get clean \
&& rm -rf /var/lib/apt/lists/*

WORKDIR /app

RUN pip install --upgrade pip
RUN pip install --no-cache-dir poetry

ADD https://github.com/ufoscout/docker-compose-wait/releases/download/2.9.0/wait /wait
RUN chmod +x /wait

COPY pyproject.toml poetry.lock /app/

RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction

EXPOSE 8000

CMD ["manage.py", "runserver"]
