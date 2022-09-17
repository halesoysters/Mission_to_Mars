from flask import Flask, render_template, redirect, url_for
from flask_pymongo import PyMongo
import scraping

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

#create route that renders index.html template
@app.route("/")
def index():
   mars = mongo.db.mars.find_one()
   return render_template("index.html", mars=mars)

#create scraping route
@app.route("/")
def index():
    mars = mongo.db.mars
    mars_data = scraping.scarap_all()
    mars.update_one({}, {"$set":mars_data}, upsert=True)
    return redirect('/', code = 302)

if __name__ == "__main__":
   app.run()