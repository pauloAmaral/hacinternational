FROM ubuntu:18.04

ENV PROJECT_DIR /hacinternational
ENV PYTHONPATH $PROJECT_DIR
ENV PYTHONVERSION 3.7.2
ENV DEBIAN_FRONTEND noninteractive

RUN apt -y update && apt -y upgrade && \
    apt install -y make build-essential zlib1g-dev \
                   libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm  \
                   libncurses5-dev libncursesw5-dev xz-utils tk-dev \
                   libffi-dev liblzma-dev python-openssl git ruby-sass \
                   nodejs-dev node-gyp libssl1.0-dev npm software-properties-common
RUN npm install -g yuglify

# Fetch latest stable version of Nginx from the official Nginx ppa and install it
RUN add-apt-repository -y ppa:nginx/stable && apt-get update && apt-get -y install nginx

# Setup appuser with the correct permissions
RUN groupadd -g 1000 -r appuser && \
    useradd -u 1000 -r appuser -g appuser

# Build the project directory
RUN mkdir -p $PROJECT_DIR
COPY ./ $PROJECT_DIR
RUN chown -R appuser:appuser $PROJECT_DIR

# Make sure appuser's home directory exists and it has the correct permissions
RUN mkdir -p /home/appuser
RUN chown -R appuser:appuser /home/appuser

RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

USER appuser

# Install pyenv
RUN curl -L https://pyenv.run | bash && \
    echo  'export PATH="$HOME/.pyenv/bin:$PATH" \n\
           eval "$(pyenv init -)" \n\
           eval "$(pyenv virtualenv-init -)"' > /home/appuser/.bashrc

# Install python
RUN /home/appuser/.pyenv/bin/pyenv install $PYTHONVERSION
RUN /home/appuser/.pyenv/bin/pyenv global $PYTHONVERSION
RUN /home/appuser/.pyenv/bin/pyenv rehash

# Install and activate virtualenv
RUN /home/appuser/.pyenv/bin/pyenv virtualenv $PYTHONVERSION appenv
RUN /home/appuser/.pyenv/bin/pyenv global appenv

# Install python requirements
COPY ./requirements.txt $PROJECT_DIR/requirements.txt
RUN /home/appuser/.pyenv/shims/pip install --upgrade pip
RUN /home/appuser/.pyenv/shims/pip install -r $PROJECT_DIR/requirements.txt

# Production related setup
RUN cp $PROJECT_DIR/nginx.conf /etc/nginx/nginx.conf && \
    cp $PROJECT_DIR/nginx_hacinternational /etc/nginx/sites-available/

EXPOSE 8001
ENTRYPOINT ["/hacinternational/entrypoint.sh"]
CMD ["$PROJECT_DIR/run.sh"]

WORKDIR $PROJECT_DIR
