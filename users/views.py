from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

users_blueprint = Blueprint('users', __name__, static_url_path='/users/static', static_folder='./static',
                      template_folder='./templates')

@users_blueprint.route("/users")
def users():
    try:
        return render_template('users.html')
    except TemplateNotFound:
        abort(404)

@users_blueprint.route("/users/new")
def newuser():
    try:
        return render_template("newuser.html")
    except TemplateNotFound:
        abort(404)

@users_blueprint.route("/users/edit")
def edituser():
    try:
        return render_template("edituser.html")
    except TemplateNotFound:
        abort(404)


