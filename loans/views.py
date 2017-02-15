from flask import Blueprint, render_template, abort, request, redirect, url_for, flash
from jinja2 import TemplateNotFound
from flask_login import login_required


from .forms import AddForm, EditForm

loans_blueprint = Blueprint('loans', __name__, static_folder='static', static_url_path='/static/loans',
                      template_folder='./templates')

@loans_blueprint.route("/loans/", methods=['GET'])
@login_required
def loans():
    from customers.models import Customer
    try:
        sort = request.query_string.split('=')
        if len(sort) == 2:
            query_loans = sorting(sort[0], sort[1])
        else:
            query_loans = get_list_order_by(Customer.name, 'asc')
        return render_template('loans.html', query_loans=query_loans)
    except TemplateNotFound:
        abort(404)

def sorting(column, sort_by):
    from models import Loan
    from customers.models import Customer
    if column == 'name':
        return get_list_order_by(Customer.name, sort_by)
    elif column == 'amount':
        return get_list_order_by(Loan.amount, sort_by)
    elif column == 'interest':
        return get_list_order_by(Loan.interest, sort_by)
    elif column == 'total_payable':
        return get_list_order_by(Loan.total_payable, sort_by)
    elif column == 'total_payment':
        return get_list_order_by(Loan.total_payment, sort_by)
    elif column == 'outstanding_balance':
        return get_list_order_by(Loan.outstanding_balance, sort_by)

def get_list_order_by(field, sort_by):
    if sort_by == 'desc':
        return get_list(field.desc())
    elif sort_by == 'asc':
        return get_list(field.asc())

def get_list(order_by):
    from models import Loan
    from coinage import db
    from customers.models import Customer
    return db.session.query(Loan, Customer).join(Customer).filter(Loan.customer_id == Customer.id).filter(
        Loan.is_dormant == 0).order_by(order_by)

@loans_blueprint.route("/loans/new/", methods=['POST','GET'])
@login_required
def newloans():
    from coinage import db
    from customers.models import Customer
    from models import Interest, Loan
    try:
        form = AddForm(request.form)
        customer = Customer.query.with_entities(Customer.id, Customer.name).order_by(Customer.name)
        interest = Interest.query.order_by(Interest.value)
        form.customer_name.choices = [(g.id, g.name) for g in customer]
        form.interest.choices = [(g.value, g.name) for g in interest]
        if request.method == 'GET':
            form.payment.data = 0
        if request.method == 'POST':
            if form.validate_on_submit():
                loan = Loan()
                loan.customer_id = form.customer_name.data
                loan.date_release = form.date_release.data
                loan.amount = form.amount.data
                loan.date_due = form.date_due.data
                loan.interest = form.interest.data
                loan.total_payable = form.total_payable.data
                loan.payment = form.payment.data
                loan.total_payment = form.total_payment.data
                loan.outstanding_balance = form.outstanding_balance.data
                loan.fully_paid_on = form.fully_paid_on.data
                loan.is_dormant = 0;
                db.session.add(loan)
                db.session.commit()
                flash(u'Record was successfully created.', 'success')
                return redirect(url_for('loans.loans'))

        return render_template("addloan.html", form=form)
    except TemplateNotFound:
        abort(404)


@loans_blueprint.route("/loans/edit/<id>/")
@login_required
def editloans(id):
    try:
        return render_template("editloan.html")
    except TemplateNotFound:
        abort(404)


