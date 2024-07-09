FROM python:3.11.9-alpine3.20

COPY . /app

WORKDIR /app

RUN apk add --no-cache bash gcc musl-dev libffi-dev openssl-dev \
    mariadb-dev \
    mysql-client \
    pkgconfig \
    && pip install --upgrade pip && pip install -r requirements.txt

COPY . /app

ENTRYPOINT [ "python" ]

CMD ["app.py" ]
