FROM python:3.7
COPY . /tmp
RUN pip install flask
EXPOSE 8080
CMD ["python", "/tmp/myapp.py"]
