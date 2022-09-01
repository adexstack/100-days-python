from flask import Flask, render_template

app = Flask(__name__)  #getting current directory

@app.route("/")
def say_hello():
    return render_template("seyi-cv.html")


if __name__ == '__main__':
    app.run(debug=True)