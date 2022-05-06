FROM python:3.10

RUN python3 -m pip install -U pip wheel poetry
RUN mkdir -p /srv/cisco
WORKDIR /srv/cisco
COPY ../poetry.lock /srv/cisco
COPY ../pyproject.toml /srv/cisco
RUN poetry install --no-root
COPY .. /srv/cisco
RUN poetry install

ENTRYPOINT ["/srv/cisco/docker/webapp_entrypoint.sh"]