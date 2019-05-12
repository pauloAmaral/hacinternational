#!/bin/bash
set -e

if [[ "$ENVIRONMENT" = "production" ]]; then
  echo "Running production server on port 8001"
  tail -f /var/log/nginx_error.log
else
  echo "Running development server on http://localhost:8001"
  $HOME/.pyenv/shims/python $PROJECT_DIR/manage.py runserver 0:8001
fi
