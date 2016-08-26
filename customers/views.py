from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

customers_blueprint = Blueprint('customers', __name__, static_url_path='/customers/static', static_folder='./static',
                      template_folder='./templates')

@customers_blueprint.route("/customers")
def customers():
    try:
        return render_template('customers.html')
    except TemplateNotFound:
        abort(404)

@customers_blueprint.route("/customers/new")
def newcustomer():
    try:
        return render_template("newcustomer.html")
    except TemplateNotFound:
        abort(404)

@customers_blueprint.route("/customers/edit")
def editcustomer():
    try:
        return render_template("editcustomer.html")
    except TemplateNotFound:
        abort(404)


