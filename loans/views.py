from flask import Blueprint, render_template, abort, request, redirect, url_for, flash
from jinja2 import TemplateNotFound
from flask_login import login_required, current_user
from collections import OrderedDict
from decimal import Decimal
from re import sub

from .forms import AddForm, EditForm

loans_blueprint = Blueprint('loans', __name__, static_folder='static', static_url_path='/static/loans',
                      template_folder='./templates')

@loans_blueprint.route("/loans/", methods=['GET'])
@login_required
def loans():
    from customers.models import Customer
    try:
        sort = request.query_string.split('=')
        columns = [('name','Name'),('amount','Amount'),('interest','Interest'),('tpayable','Total Payable'),('tpayment','Total Payment'),('outbal','Outstanding Balance')]
        columns = OrderedDict(columns)
        if len(sort) == 2:
            query_loans = sorting(sort[0], sort[1])
            sort_order = sort[1]
        else:
            query_loans = get_list_order_by(Customer.name, 'asc')
            sort_order = None

        return render_template('loans.html', query_loans=query_loans, sort_order=sort_order, columns=columns)
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
    return db.session.query(Loan).join(Loan.customer).order_by(order_by).all()

@loans_blueprint.route("/loans/new/", methods=['POST','GET'])
@login_required
def newloans():
    from coinage import db
    from customers.models import Customer
    from models import Interest, Loan
    try:
        if not current_user.can_create:
            return redirect(url_for('loans.loans'))
        form = AddForm()
        _customer = Customer.query.with_entities(Customer.id, Customer.name).order_by(Customer.name)
        interest = Interest.query.order_by(Interest.value)
        form.customer_name.choices = form.comaker_name.choices = [(g.id, g.name) for g in _customer]
        form.interest.choices = [(g.value, g.name) for g in interest]
        if request.method == 'GET':
            form.interest.data = 5
            form.payment.data = 0
            form.total_payment.data = 0
        if request.method == 'POST':
            if form.validate_on_submit():
                try:
                    loan = Loan()
                    loan.customer_id = form.customer_name.data
                    loan.date_release = request.form['date_rel']
                    loan.amount = Decimal(form.amount.data.replace(',', ''))
                    loan.date_due = request.form['date_due']
                    loan.interest = form.interest.data
                    loan.total_payable = Decimal(form.total_payable.data.replace(',', ''))
                    loan.payment = Decimal(form.payment.data.replace(',', ''))
                    loan.total_payment = Decimal(form.total_payment.data.replace(',', ''))
                    loan.outstanding_balance = Decimal(form.outstanding_balance.data.replace(',', ''))
                    db.session.add(loan)
                    db.session.commit()
                    flash(u'Record was successfully created.', 'success')
                    return redirect(url_for('loans.loans'))
                except Exception as e:
                    flash(e.message, 'danger')
            else:
                flash(form.errors, 'danger')

        return render_template("addloan.html", form=form)
    except TemplateNotFound:
        abort(404)


@loans_blueprint.route("/loans/edit/<id>/", methods=['GET', 'POST'])
@login_required
def editloans(id):
    from coinage import db
    from models import Loan, Interest
    from customers.models import Customer

    if not current_user.can_update:
        return redirect(url_for('loans.loans'))
    form = EditForm(request.form)
    loan = Loan.query.filter_by(id=id).first()
    if loan is None:
        flash(u'Cannot find loan.', 'danger')
        return redirect(url_for('loans.loans'))
    _customer = Customer.query.with_entities(Customer.id, Customer.name).order_by(Customer.name)
    interest = Interest.query.order_by(Interest.value)
    form.customer_name.choices = form.comaker_name.choices = [(g.id, g.name) for g in _customer]
    form.interest.choices = [(g.value, g.name) for g in interest]
    if request.method == 'POST':

        if form.validate_on_submit():
            try:
                loan.customer_id = request.form['customer_name']
                loan.date_release = request.form['date_rel']
                loan.amount = Decimal(request.form['amount'].replace(',', ''))
                loan.date_due = request.form['date_due']
                loan.interest = request.form['interest']
                loan.total_payable = Decimal(request.form['total_payable'].replace(',', ''))
                loan.payment = Decimal(request.form['payment'].replace(',', ''))
                loan.fully_paid_on = request.form['date_fullypaid']
                loan.total_payment = Decimal(request.form['total_payment'].replace(',', ''))
                loan.outstanding_balance = Decimal(float(request.form['outstanding_balance'].replace(',', '')))
                db.session.commit()
                flash(u'Record successfully saved.', 'success')
                return redirect(url_for('loans.loans'))
            except Exception as e:
                flash(e.message, 'danger')
        else:
            flash(form.errors, 'danger')
    elif request.method == 'GET':
        form.customer_name.data = loan.customer_id
        form.date_release.data = loan.date_release
        form.amount.data = "{:,.2f}".format(loan.amount)
        form.date_due.data = loan.date_due
        form.interest.data = loan.interest
        form.total_payable.data = "{:,.2f}".format(loan.total_payable)
        form.payment.data = "{:,.2f}".format(loan.payment)
        form.fully_paid_on.data = loan.fully_paid_on
        form.total_payment.data = loan.total_payment
        form.outstanding_balance.data = "{:,.2f}".format(loan.outstanding_balance)
    return render_template("editloan.html", form=form)

@loans_blueprint.route("/loans/delete/", methods=['POST'])   # pragma: no cover)
@login_required
def deleteloan():
    from coinage import db
    from models import Loan
    if not current_user.can_delete:
        return redirect(url_for('loans.loans'))
    id = request.form['id']
    loan = Loan.query.filter_by(id=id).first()
    if loan is None:
        flash(u'Cannot find loan.', 'danger')
        return redirect(url_for('loans.loans'))
    else:
        db.session.delete(loan)
        db.session.commit()
        flash(u'Record was successfully deleted.', 'success')
        return redirect(url_for('loans.loans'))
