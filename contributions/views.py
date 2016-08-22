from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound


contributions_blueprint = Blueprint('contributions', __name__, static_url_path='/contributions/static', static_folder='./static',
                      template_folder='./templates')

@contributions_blueprint.route("/contributions")
def contributions():
    try:
        return render_template('contributions.html')
    except TemplateNotFound:
        abort(404)

@contributions_blueprint.route("/contributions/new")
def newcontributions():
    try:
        return render_template("newcontributions.html")
    except TemplateNotFound:
        abort(404)

@contributions_blueprint.route("/contributions/edit")
def editcontributions():
    try:
        return render_template("editcontributions.html")
    except TemplateNotFound:
        abort(404)


