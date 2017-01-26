from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

home_blueprint = Blueprint('home', __name__, static_folder='static', static_url_path='/static/home',
                      template_folder='./templates')

@home_blueprint.route("/")
def home():
    try:
        error = None
        return render_template('index.html')
    except TemplateNotFound:
        abort(404)



