from flask import Flask
import os

app = Flask(__name__)
@app.route('/')

def hello():
    return('Hello from container..This is my first docker container\n')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
