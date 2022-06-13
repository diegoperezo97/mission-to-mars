# import necessary libraries
from flask import Flask, render_template

# @TODO: Initialize your Flask app here
app = Flask(__name__)

# @TODO:  Create a route and view function that takes in a string and renders index.html template
@app.route("/")
def index(name="Diego Pérez Ortega", hobby="Coding"):
    return render_template("index.html", name=name, hobby=hobby)

@app.route("/SecondActivity")
def bonus(name="Norma P Ortega Ortega", hobby="Python"):
    return render_template("bonus.html", name=name, hobby=hobby)

if __name__ == "__main__":
    app.run(debug=True)
