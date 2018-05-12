from flask import Blueprint, render_template

api = Blueprint('api', __name__)


@api.route("/")
def index():
    return "<h1>hello flask</h1>"


@api.route("/html")
def index_html():
    return render_template('index.html')
