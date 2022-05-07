FROM python:3.10

RUN python3 -m pip install -U pip wheel poetry
RUN mkdir -p /srv/cisco
WORKDIR /srv/cisco
COPY ../poetry.lock /srv/cisco
COPY ../pyproject.toml /srv/cisco
RUN poetry config virtualenvs.in-project true
RUN poetry install --no-root  --no-dev
# the lines above are usually cached. The ones below will be rebuild everytime.
COPY .. /srv/cisco
RUN poetry install

EXPOSE 8000

ENTRYPOINT ["/srv/cisco/docker/webapp_entrypoint.sh"]