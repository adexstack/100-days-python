from random import randint

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return '<h1 style="text-align: center">Guess a number between 0 and 9</h1>' \
           '<p></>' \
           '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" width=200>'

@app.route("/<int:entered>")
def check_guess(entered):
    random_number = randint(1, 9)
    print(random_number)
    if entered == random_number:
        return '<h1 style= "color: green">Well Done. You found me!</h1>' \
               '<p></>' \
               '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">'
    elif entered < random_number:
        return '<h1 style= "color: purple">Too Low, Try Again</h1>' \
               '<p></>' \
               '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">'
    else:
        return '<h1 style= "color: red">Too High, Try Again</h1>' \
               '<p></>' \
               '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">'


if __name__ == "__main__":
    app.run(debug=True)
