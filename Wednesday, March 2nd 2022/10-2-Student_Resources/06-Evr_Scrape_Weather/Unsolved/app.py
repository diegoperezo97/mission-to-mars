from flask import Flask, render_template, redirect, request
from flask_pymongo import PyMongo
import scrape_costa

# Create an instance of Flask
app = Flask(__name__)

# Use PyMongo to establish Mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/weather_app")


# Route to render index.html template using data from Mongo
@app.route("/")
def home():

    # Find one record of data from the mongo database
    destination_data = mongo.db.collection.find_one()

    # Return template and data
    return render_template("index.html", vacation=destination_data)


# Route that will trigger the scrape function
@app.route("/scrape")
def scrape(img_num=2):
    img_num = request.args.get("img_num")
    # Run the scrape function and save the results to a variable
    data = scrape_costa.scrape_info(int(img_num))

    # Update the Mongo database using update and upsert=True
    mongo.db.collection.update_one({}, {"$set": data}, upsert=True)

    # Redirect back to home page
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)
