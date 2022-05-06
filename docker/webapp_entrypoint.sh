#!/bin/bash

set -euxo pipefail

# In production this would be at least a number of uwsgi/gunicorn processes
# behind a proxy like nginx or haproxy.
poetry run gunicorn -b 0.0.0.0:8000 -w 4 coins.wsgi:application