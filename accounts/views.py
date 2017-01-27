from flask import Blueprint, render_template, abort, flash, request, url_for, redirect
from jinja2 import TemplateNotFound
from flask_login import login_user, login_required, logout_user, current_user

from .forms import LoginForm, RegisterForm

accounts_blueprint = Blueprint('accounts', __name__, static_folder='static', static_url_path='/static/accounts',
                      template_folder='./templates')

@accounts_blueprint.route('/login', methods=['GET', 'POST'])   # pragma: no cover
def login():
    from coinage import bcrypt
    from models import Account
    error = None
    form = LoginForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            user = Account.query.filter_by(name=request.form['username']).first()
            if user is not None and bcrypt.check_password_hash(
                user.password, request.form['password']
            ):
                login_user(user)
                next = request.args.get('next')
                if next is not None:
                    return redirect(next)
                else:
                    return redirect(url_for('home.home'))
            else:
                error = 'Invalid username or password.'
    return render_template('login.html', form=form, error=error)


@accounts_blueprint.route('/logout')   # pragma: no cover
@login_required   # pragma: no cover
def logout():
    logout_user()
    return redirect(url_for('accounts.login'))


@accounts_blueprint.route(
    '/register/', methods=['GET', 'POST'])   # pragma: no cover
def register():
    from coinage import db
    from models import Account
    form = RegisterForm()
    error = None
    if form.validate_on_submit():
        account = Account.query.filter_by(name=form.username.data.strip()).first()
        if account is None:
            account = Account(
                name=form.username.data,
                email=form.email.data,
                password=form.password.data
            )
            db.session.add(account)
            db.session.commit()
            login_user(account)
            return redirect(url_for('home.home'))
        else:
            error = 'User name ' + form.username.data + ' is already taken.'
    return render_template('register.html', form=form, error=error, instruction='Please register', title='Register')
