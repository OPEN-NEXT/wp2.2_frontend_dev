# SPDX-FileCopyrightText: 2021 Pen-Yuan Hsing
# SPDX-License-Identifier: AGPL-3.0-or-later

# Container image following Heroku recommendations: 
# https://devcenter.heroku.com/articles/container-registry-and-runtime#testing-an-image-locally

FROM python:3.10-bullseye

WORKDIR /opt/app

# COPY ./requirements.txt /tmp/requirements.txt

# RUN apt-get update && apt-get install -y \
#     gcc \
#     python-dev \
#     && rm -rf /var/lib/apt/lists*

COPY ./ /opt/app

RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Create and use a non-root user (required by Heroku)
# RUN adduser --disabled-password myuser
# USER myuser

# CMD mercury run repos.ipynb 0.0.0.0:$PORT
CMD mercury run repos.ipynb 0.0.0.0