FROM python:alpine3.7
COPY . /flask_docker_demo
WORKDIR /flask_docker_demo
RUN pip install --upgrade pip; apk add build-base; pip install numpy
RUN pip install -r requirements.txt
EXPOSE 5001
ENTRYPOINT [ "python" ]
CMD [ "app.py" ]