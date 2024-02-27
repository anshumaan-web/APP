!pip install flask

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>Hello World!</h1>"

@app.route("/test")
def test():
    return "<h1>Hello Test</h1>"

if __name__ == '__main__':
    app.run()
