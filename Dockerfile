# base image
FROM python:3.9.7-buster

# options
ENV PYTHONUNBUFFERED 1

# Set working directory
RUN mkdir core
# set the working directory
COPY . /core/
# coppy commands
WORKDIR /core

# update docker-iamage packages
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y netcat-openbsd gcc && \
    apt-get clean

# update pip


# install python packages
RUN pip3 install -r requirements.pip
# create static directory

RUN python3 manage.py migrate

RUN python3 manage.py loaddata api/fixtures/datadump.json

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]