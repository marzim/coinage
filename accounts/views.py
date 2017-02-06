from flask import Blueprint, render_template, abort, flash, request, url_for, redirect
from jinja2 import TemplateNotFound
from flask_login import login_user, login_required, logout_user, current_user

from .forms import LoginForm, RegisterForm, SettingForm

accounts_blueprint = Blueprint('accounts', __name__, static_folder='static', static_url_path='/static/accounts',
                      template_folder='./templates')

@accounts_blueprint.route('/login', methods=['GET', 'POST'])   # pragma: no cover
def login():
    from coinage import bcrypt
    from users.models import User
    error = None
    form = LoginForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            user = User.query.filter_by(name=request.form['username']).first()
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
    from users.models import User
    form = RegisterForm()
    error = None
    if form.validate_on_submit():
        user = User.query.filter_by(name=form.username.data.strip()).first()
        if user is None:
            user = User(
                name=form.username.data,
                email=form.email.data,
                password=form.password.data
            )

            rights = 1 if user.name == 'admin' else 0;
            user.can_delete = rights
            user.can_update = rights
            user.can_create = rights
            db.session.add(user)
            db.session.commit()
            login_user(user)

            return redirect(url_for('home.home'))
        else:
            error = 'User name ' + form.username.data + ' is already taken.'
    return render_template('register.html', form=form, error=error, instruction='Please register', title='Register')

@accounts_blueprint.route(
    '/setting/', methods=['GET', 'POST'])   # pragma: no cover
@login_required
def setting():
    from coinage import bcrypt
    from coinage import db
    from users.models import User
    user = User.query.filter_by(id=current_user.id).first()
    form = SettingForm()
    form.username.data = user.name
    form.email.data = user.email
    error = None
    if request.method == 'POST':
        equalPassword = bcrypt.check_password_hash(user.password, request.form['password']);
        if not equalPassword:
            form.password.errors = ['Password does not match with the current password.'];
        else:
            if form.validate_on_submit():
                form = SettingForm(request.form)
                current_user.set_property(
                    can_create=int(user.can_create),
                    can_update=int(user.can_update),
                    can_delete=int(user.can_delete),
                    name=user.name,
                    email=form.email.data,
                    password=form.newpassword.data
                )
                db.session.commit()
                return redirect(url_for('accounts.logout'))
    return render_template('setting.html', form=form, error=error)
