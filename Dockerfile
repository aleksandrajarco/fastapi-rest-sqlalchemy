from alpine:latest

RUN apk add --no-cache python3-dev \
    && pip3 install --upgrade pip

WORKDIR /app

COPY . /app

#RUN pip3 install psycopg2-binary
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev make
RUN pip3 --no-cache-dir install -r requirements.txt

EXPOSE 5001


CMD [ "python3", "./app.py" ]
