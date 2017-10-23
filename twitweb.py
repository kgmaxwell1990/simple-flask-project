from flask import Flask
from flask import render_template
import os

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("banana.html")

@app.route("/photos/car/<id>")
def get_photos_of_car(id):
    return "You picked photos of car {0}".format(id)

if __name__ == "__main__":
    app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))