from flask import Flask, request
from flask import render_template
import os

app = Flask(__name__)

previous_searches = set()

fake_news = ["fakenews1", "fakenews2", "fakenews3"]

@app.route("/")
def index():
    return render_template("search.html")

@app.route("/search")
def do_search():
    q = request.args.get('query')
    previous_searches.add(q)
    return render_template("results.html", searched_for=q, headlines=fake_news)

@app.route("/previous")
def show_prev():
    return render_template("previous.html", search_terms = previous_searches)


# @app.route("/photos/car/<id>")
# def get_photos_of_car(id):
#     return "You picked photos of car {0}".format(id)

if __name__ == "__main__":
    app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))