from app import app
from app.models import URLs
import json
from flask import render_template, flash, redirect, url_for, request
import code

@app.route("/query_backend", methods=["GET", "POST"])
def query_backend():
    results = [elem.row for elem in URLs.query.all()]
    return json.dumps(results)

@app.route("/search", methods=["GET", "POST"])
def search():
    keyword = request.form["search"]
    results = URLs.query.filter_by(keyword=keyword).all()
    return render_template("results.html", results=results)
               
@app.route("/", methods=["GET", "POST"])
def index():
    # TODO: figure out the ORM way to do this
    keywords = list(set([elem.keyword for elem in URLs.query.all()]))
    return render_template("index.html", keywords=keywords)
