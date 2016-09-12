from flask import Blueprint, render_template, abort, flash, request, url_for, redirect
from jinja2 import TemplateNotFound
from flask_login import login_user, login_required, logout_user

from .forms import LoginForm, RegisterForm

users_blueprint = Blueprint('users', __name__, static_url_path='/users/static', static_folder='./static',
                      template_folder='./templates')

@users_blueprint.route("/users")
@login_required
def users():
    try:
        return render_template('users.html')
    except TemplateNotFound:
        abort(404)

@users_blueprint.route("/users/edit")
@login_required
def edituser():
    try:
        return render_template("edituser.html")
    except TemplateNotFound:
        abort(404)

@users_blueprint.route('/login', methods=['GET', 'POST'])   # pragma: no cover
def login():
    from coinage import bcrypt
    from models import User
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


@users_blueprint.route('/logout')   # pragma: no cover
@login_required   # pragma: no cover
def logout():
    logout_user()
    return redirect(url_for('users.login'))


@users_blueprint.route(
    '/register/', methods=['GET', 'POST'])   # pragma: no cover
def register():
    from coinage import db
    from models import User
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
            db.session.add(user)
            db.session.commit()
            login_user(user)
            return redirect(url_for('home.home'))
        else:
            error = 'User name ' + form.username.data + ' is already taken.'
    return render_template('register.html', form=form, error=error)
