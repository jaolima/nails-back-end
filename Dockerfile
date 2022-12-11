# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Use an official lightweight Python image.
# https://hub.docker.com/_/python
FROM python:3.9-buster

ENV APP_HOME /app
ENV PORT 8080
WORKDIR $APP_HOME

# Removes output stream buffering, allowing for more efficient logging
ENV PYTHONUNBUFFERED 1

# Install system requirements
RUN apt update -y

# Install python pip requirements
RUN python -m pip install --upgrade pip

# Install dependencies
COPY requirements /requirements/

RUN pip install --no-cache-dir -r /requirements/requirements.txt

# Run the web service on container startup.
# Here we use the python manage.py webserver,
CMD python manage.py makemigrations --no-input && python manage.py migrate && python manage.py runserver 0.0.0.0:$PORT
