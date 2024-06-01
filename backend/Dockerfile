FROM python:3.10-alpine
LABEL author=pk13055 version=1.5
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/usr/lib/python3.10/site-packages

RUN echo "@testing http://dl-cdn.alpinelinux.org/alpine/edge/testing" >> /etc/apk/repositories \
 && apk add --update --no-cache \
 			gcc libffi-dev musl-dev \
			py3-numpy@testing py3-pandas@testing \
 && pip install pip-tools

WORKDIR /app
COPY requirements.in  .
RUN pip-compile requirements.in > requirements.txt \
 && pip3 install -r requirements.txt

COPY . /app
ENTRYPOINT ["./entrypoint.sh"]