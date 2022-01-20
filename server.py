from distutils.log import debug
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/play")
def play():
    return render_template("index.html", quantity = 3, color = "#a6c4f4")

@app.route("/play/<int:quantity>")
def playq(quantity):
    return render_template("index.html", quantity = quantity, color = "#a6c4f4")

@app.route("/play/<int:quantity>/<string:color>")
def playqc(quantity, color):
    return render_template("index.html", quantity = quantity, color = color)

if __name__ == "__main__": # This should be run directly
    app.run(debug = True)