from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
from flask_login import login_required

guidelines_blueprint = Blueprint('guidelines', __name__, static_url_path='/guidelines/static', static_folder='./static',
                      template_folder='./templates')

@guidelines_blueprint.route("/guidelines")
@login_required
def guidelines():
    try:
        return render_template('guidelines.html')
    except TemplateNotFound:
        abort(404)

@guidelines_blueprint.route("/guidelines/new")
@login_required
def newguidelines():
    try:
        return render_template("newguidelines.html")
    except TemplateNotFound:
        abort(404)

@guidelines_blueprint.route("/guidelines/edit")
@login_required
def editguidelines():
    try:
        return render_template("editguidelines.html")
    except TemplateNotFound:
        abort(404)


