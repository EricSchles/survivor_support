from app import app
from app.models import URLs
import json
from flask import render_template, flash, redirect, url_for, request

@app.route("/query_backend", methods=["GET", "POST"])
def index():
    results = [elem.row for elem in Table.query.all()]
    return json.dumps(results)

@app.route("/search", methods=["GET", "POST"])
def search():
    keyword = request.form["search"]
    results = [elem.url
               for elem in URLs.query.filter_by(keyword=keyword).all()]
    return render_template("results.html", results=results)
               
@app.route("/", methods=["GET", "POST"])
def testing():
    return render_template("index.html")
