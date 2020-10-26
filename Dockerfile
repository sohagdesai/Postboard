# Specify a base image
FROM python:3.8.6-alpine
WORKDIR /Postboard
COPY wait-for-it.sh .
ADD . /Postboard
RUN apk update && apk add bash
RUN \
 apk add --no-cache postgresql-libs && \
 apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev && \
 pip install -r requirements.txt --no-cache-dir && \
 apk --purge del .build-deps
EXPOSE 5000
CMD ["start.sh"]
