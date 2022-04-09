FROM python:2.7-onbuild
RUN pip install flask
RUN pip install redis
RUN pip install mysql-python
EXPOSE 5000
CMD [ "python", "app.py" ]
