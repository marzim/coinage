from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
from flask_login import login_required

customers_blueprint = Blueprint('customers', __name__, static_folder='static', static_url_path='/static/customers',
                      template_folder='./templates')

@customers_blueprint.route("/customers")
@login_required
def customers():
    try:
        return render_template('customers.html')
    except TemplateNotFound:
        abort(404)

@customers_blueprint.route("/customers/new")
@login_required
def newcustomer():
    try:
        return render_template("newcustomer.html")
    except TemplateNotFound:
        abort(404)

@customers_blueprint.route("/customers/edit")
@login_required
def editcustomer():
    try:
        return render_template("editcustomer.html")
    except TemplateNotFound:
        abort(404)


