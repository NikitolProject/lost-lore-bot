FROM python:3.9

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apt-get update \
    && apt-get install -y postgresql-server-dev-all gcc python3-dev musl-dev

# create directory for the app user
RUN mkdir -p /home/admin

# create the app user
RUN addgroup --system admin && adduser --system admin && adduser admin admin

# create the appropriate directories
ENV HOME=/home/admin
ENV APP_HOME=/home/admin/web
RUN mkdir $APP_HOME
RUN mkdir $HOME/static
WORKDIR $APP_HOME

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt
