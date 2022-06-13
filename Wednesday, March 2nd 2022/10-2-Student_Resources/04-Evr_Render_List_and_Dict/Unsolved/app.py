# import necessary libraries
from flask import Flask, render_template

# @TODO: Initialize your Flask app here
app = Flask(__name__)

# @TODO: Create a list of dictionaries
dogs = [{"name": "Cala", "type": "Golden"},
        {"name": "Mita", "type": "Boxer"},
        {"name": "Suzzy", "type": "Terrier"},
        {"name": "Tomato", "type": "Retriever"}]

# @TODO:  Create a route and view function that takes in a dictionary and renders index.html template
@app.route("/")
def index():
    return render_template("index.html", dogs=dogs)

if __name__ == "__main__":
    app.run(debug=True)
