
# https://flask.palletsprojects.com/en/1.1.x/quickstart/#routing

from flask import Flask

app = Flask(__name__)

def make_bold(func):
    def bold_tag():
        return f"<b>{func()}<b>"
    return bold_tag

def make_emphasis(func):
    def wrapper():
        return f"<em>{func()}<em>"
    return wrapper

def make_underlined(func):
    def wrapper():
        return f"<u>{func()}<u>"
    return wrapper

@app.route("/")
def hello():
    return "Hello, People!"

@app.route("/speak")
@make_bold
@make_emphasis
@make_underlined
def speak_up():
    return "Speaking up!"

@app.route("/username/<name>/<int:age>")
def greet(name, age):
    return f"Hello there {name}, you are {age} years old"

# https://flask.palletsprojects.com/en/1.1.x/quickstart/#variable-rules
if __name__ == "__main__":
    app.run(debug=True) # True allows automatic reloading and debugging
