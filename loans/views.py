from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
from flask_login import login_required

loans_blueprint = Blueprint('loans', __name__, static_folder='static', static_url_path='/static/loans',
                      template_folder='./templates')

@loans_blueprint.route("/loans")
@login_required
def loans():
    try:
        return render_template('loans.html')
    except TemplateNotFound:
        abort(404)

@loans_blueprint.route("/loans/new")
@login_required
def newloans():
    try:
        return render_template("newloan.html")
    except TemplateNotFound:
        abort(404)

@loans_blueprint.route("/loans/edit")
@login_required
def editloans():
    try:
        return render_template("editloan.html")
    except TemplateNotFound:
        abort(404)


