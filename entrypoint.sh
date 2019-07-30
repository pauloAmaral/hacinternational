#!/bin/bash
set -e

echo "Apply migrations"
$HOME/.pyenv/shims/python $PROJECT_DIR/manage.py migrate

########################################
#       Production related setup       #
########################################

if [[ "$ENVIRONMENT" = "production" ]]; then
  # Remove default site configuration
  [[ -e /etc/nginx/sites-enabled/default ]] && rm -rf /etc/nginx/sites-enabled/default
  [[ -e /etc/nginx/sites-available/default ]] && rm -rf /etc/nginx/sites-available/default

  # Link app related config file from sites available to sites enabled and
  # restart Nginx
  ln -sf /etc/nginx/sites-available/nginx_hacinternational /etc/nginx/sites-enabled/nginx_hacinternational
  service nginx restart

  # Run uwsgi
  $HOME/.pyenv/shims/uwsgi --ini $PROJECT_DIR/uwsgi.ini

  bash -c "$HOME/.pyenv/shims/python $PROJECT_DIR/manage.py collectstatic --noinput"
fi

eval "$@"
