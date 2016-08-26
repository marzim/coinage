from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

loans_blueprint = Blueprint('loans', __name__, static_url_path='/loans/static', static_folder='./static',
                      template_folder='./templates')

@loans_blueprint.route("/loans")
def loans():
    try:
        return render_template('loans.html')
    except TemplateNotFound:
        abort(404)

@loans_blueprint.route("/loans/new")
def newloans():
    try:
        return render_template("newloan.html")
    except TemplateNotFound:
        abort(404)

@loans_blueprint.route("/loans/edit")
def editloans():
    try:
        return render_template("editloan.html")
    except TemplateNotFound:
        abort(404)


