# On CMD; C:\path\to\app>set FLASK_APP=hello.py
# On Mac $ export FLASK_APP=hello.py
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/bye")
def bye():
    return "Good Bye!"


if __name__ == "__main__":
    app.run(debug=True)
