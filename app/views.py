from app import app
from app.models import Table
import json
from flask import render_template, flash, redirect, url_for

@app.route("/query_backend", methods=["GET", "POST"])
def index():
    results = [elem.row for elem in Table.query.all()]
    return json.dumps(results)

@app.route("/", methods=["GET", "POST"])
def testing():
    return render_template("index.html")
