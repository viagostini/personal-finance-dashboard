FROM tiangolo/uvicorn-gunicorn:python3.7-alpine3.8

WORKDIR /app
COPY . .

RUN apk add --no-cache gcc musl-dev linux-headers

RUN pip install -r requirements.txt