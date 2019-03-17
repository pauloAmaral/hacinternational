FROM ubuntu:18.04

ENV PROJECT_DIR /hacinternational
ENV PYTHONPATH $PROJECT_DIR
ENV PYTHONVERSION 3.7.2
ENV DEBIAN_FRONTEND noninteractive

RUN apt -y update && apt -y upgrade && \
    apt install -y make build-essential libssl-dev zlib1g-dev \
                   libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm  \
                   libncurses5-dev libncursesw5-dev xz-utils tk-dev \
                   libffi-dev liblzma-dev python-openssl git ruby-sass

# Setup appuser with the correct permissions
RUN groupadd -g 1000 -r appuser && \
    useradd -u 1000 -r appuser -g appuser

# Build the project directory
RUN mkdir -p $PROJECT_DIR
COPY ./ $PROJECT_DIR
RUN chown -R appuser:appuser $PROJECT_DIR

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

WORKDIR $PROJECT_DIR
