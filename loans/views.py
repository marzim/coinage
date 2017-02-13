from flask import Blueprint, render_template, abort, request, redirect, url_for
from jinja2 import TemplateNotFound
from flask_login import login_required


from .forms import AddForm, EditForm

loans_blueprint = Blueprint('loans', __name__, static_folder='static', static_url_path='/static/loans',
                      template_folder='./templates')

@loans_blueprint.route("/loans")
@login_required
def loans():
    from models import Loan
    from coinage import db
    from customers.models import Customer
    try:
        query_loans = db.session.query(Loan, Customer).join(Customer).filter(Loan.customer_id == Customer.id).order_by(Loan.date_due)
        return render_template('loans.html', query_loans=query_loans)
    except TemplateNotFound:
        abort(404)

@loans_blueprint.route("/loans/new", methods=['POST','GET'])
@login_required
def newloans():
    from customers.models import Customer
    from models import Interest
    try:
        form = AddForm()
        if request.method == 'GET':
            customer = Customer.query.with_entities(Customer.id, Customer.name).order_by(Customer.name)
            interest = Interest.query.order_by(Interest.id)
            form.customer_name.choices = [(g.id, g.name) for g in customer]
            form.interest.choices = [(g.id, g.name) for g in interest]
        elif request.method == 'POST':
            if form.validate_on_submit():
                return redirect(url_for('loans.loans'))

        return render_template("addloan.html", form=form)
    except TemplateNotFound:
        abort(404)


@loans_blueprint.route("/loans/edit")
@login_required
def editloans():
    try:
        return render_template("editloan.html")
    except TemplateNotFound:
        abort(404)


