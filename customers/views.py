from flask import Blueprint, render_template, abort, url_for, redirect, flash, request
from jinja2 import TemplateNotFound
from flask_login import login_required, current_user

from .forms import AddForm, EditForm

customers_blueprint = Blueprint('customers', __name__, static_folder='static', static_url_path='/static/customers',
                      template_folder='./templates')

@customers_blueprint.route("/customers", methods=['GET'])
@login_required
def customers():
    from models import Customer
    try:
        query_customers = Customer.query.order_by(Customer.first_name)
        return render_template('customers.html', query_customers=query_customers)
    except TemplateNotFound:
        abort(404)

@customers_blueprint.route("/customers/new", methods=['GET', 'POST'])
@login_required
def newcustomer():
    from coinage import db
    from models import Customer
    try:
        if not current_user.can_create:
            return redirect(url_for('customers.customers'))
        form = AddForm()
        error = None
        if form.validate_on_submit():
            customer = Customer.query.filter_by(first_name=form.first_name.data.strip()).first()
            if customer is None:
                customer = Customer(
                    first_name=form.first_name.data.strip(),
                    last_name=form.last_name.data.strip(),
                    number_shares=form.number_shares.data,
                    email=form.email.data.strip(),
                    address=form.address.data.strip(),
                    mobile_phone=form.mobile_phone.data.strip()
                )
                db.session.add(customer)
                db.session.commit()
                flash(u'Record was successfully created.', 'success')
                return redirect(url_for('customers.customers'))
            else:
                form.first_name.errors.append('First name ' + form.first_name.data + ' is already taken.')
        return render_template('newcustomer.html', form=form, error=error)
    except TemplateNotFound:
        abort(404)

@customers_blueprint.route("/customers/edit/<id>", methods=['GET', 'POST'])
@login_required
def editcustomer(id):
    from coinage import db
    from models import Customer
    try:
        if not current_user.can_update:
            return redirect(url_for('customers.customers'))
        customer = Customer.query.filter_by(id=id).first()
        form = EditForm()
        form.first_name.data = customer.first_name
        form.last_name.data = customer.last_name
        form.number_shares.data = customer.number_shares
        form.email.data = customer.email
        form.address.data = customer.address
        form.mobile_phone.data = customer.mobile_phone
        if request.method == 'POST':
            if form.validate_on_submit():
                customer.number_shares = int(request.form['number_shares'])
                customer.email = request.form['email']
                customer.address = request.form['address']
                customer.mobile_phone = request.form['mobile_phone']
                db.session.commit()
                flash(u'Record successfully saved.', 'success')
                return redirect(url_for('customers.customers'))
        return render_template('editcustomer.html', form=form)
    except TemplateNotFound:
        abort(404)


