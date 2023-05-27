FROM python:3.7
COPY . /tmp
RUN pip install -r /tmp/requirements.txt
EXPOSE 8080
CMD [ "python", "/tmp/app.py" ]
