FROM python:3.10-slim-buster


# setting work directory
WORKDIR /usr/src/app


# env variables
# prevents py from writing pyc files to disk
ENV PYTHONUNBUFFERED 1
# prevents buffering of stdout and stderror
ENV PYTHONDONTWEITEBYTECODE 1


# install psycopg dependencies
# RUN apt-get update && apt-get install -y \
#     build-essential \
#     libpq-dev \
#     && rm -rf /var/lib/apt/lists/*


# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . .
