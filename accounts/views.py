from flask import Blueprint, render_template, abort, flash, request, url_for, redirect
from jinja2 import TemplateNotFound
from flask_login import login_user, login_required, logout_user, current_user

from .forms import LoginForm, RegisterForm, EditPasswordForm, EditEmailForm

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
    '/editpassword/', methods=['GET', 'POST'])   # pragma: no cover
@login_required
def editpassword():
    from coinage import bcrypt
    from coinage import db
    from users.models import User
    user = User.query.filter_by(id=current_user.id).first()
    form = EditPasswordForm(request.form)
    error = None
    if request.method == 'POST':
        equalPassword = bcrypt.check_password_hash(user.password, request.form['password'])
        if form.validate_on_submit():
            if equalPassword:
                form = EditPasswordForm(request.form)
                user.password=bcrypt.generate_password_hash(form.newpassword.data)
                db.session.commit()
                flash(u'Successfully changed password.', 'success')
                flash(u'Please log out and log in using your new password.', 'info')
            else:
                form.password.errors.append('Password does not match with the current password.')
    return render_template('editpassword.html', form=form, error=error)

@accounts_blueprint.route(
    '/editemail/', methods=['GET', 'POST'])   # pragma: no cover
@login_required
def editemail():
    from coinage import db
    from users.models import User
    user = User.query.filter_by(id=current_user.id).first()
    form = EditEmailForm(request.form)
    form.email.data = user.email
    if request.method == 'POST':
        if form.validate_on_submit():
            form = EditEmailForm(request.form)
            user.email=form.newemail.data
            db.session.commit()
            flash(u'Successfully changed email address.','success')

    return render_template('editemail.html', form=form)