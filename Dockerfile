# docker build . -t huey_lab:1.0.0
# docker run -it -p 8989:8989 huey_lab:1.0.0
FROM python:3.8.12-slim-buster

ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8

# Python Code
ADD . /root/HUEY
RUN pip install -r /root/HUEY/requirements.txt
WORKDIR /root/HUEY

EXPOSE 8989

CMD gunicorn --bind :8989 -w 1 --thread 10 main:app --timeout 3600 --access-logfile - & huey_consumer -w 1 huey_task.task.huey

