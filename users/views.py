from flask import Blueprint, render_template, abort, flash, request, url_for, redirect
from jinja2 import TemplateNotFound
from flask_login import login_user, login_required, logout_user, current_user

from .forms import AddForm, EditForm

users_blueprint = Blueprint('users', __name__, static_folder='static', static_url_path='/static/users',
                      template_folder='./templates')

@users_blueprint.route("/users", methods=['GET'])   # pragma: no cover
@login_required
def users():
    from models import User
    try:
        query_users = User.query.order_by(User.name)
        return render_template('users.html', query_users=query_users)
    except TemplateNotFound:
        abort(404)

@users_blueprint.route("/users/edit/<id>", methods=['GET', 'POST'])   # pragma: no cover)
@login_required
def edituser(id):
    from coinage import db
    from models import User
    if not current_user.can_update:
        return redirect(url_for('users.users'))
    user = User.query.filter_by(id=id).first()
    form = EditForm()
    form.username.data = user.name
    form.email.data = user.email
    form.can_create.data = user.can_create
    form.can_delete.data = user.can_delete
    form.can_update.data = user.can_update
    error = None
    if request.method == 'POST':
        if form.validate_on_submit():
            if user is None:
                error = 'User name ' + form.username.data + ' cannot be found.'
            else:
                # TODO: update records doesn't work
                user.set_property(
                    can_create=form.can_create.data,
                    can_update=form.can_update.data,
                    can_delete=form.can_delete.data,
                    name=form.username.data,
                    email=form.email.data,
                    password=form.password.data
                )
                db.session.merge(user)
                db.session.commit()
                return redirect(url_for('users.users'))
    return render_template('edit.html', form=form, error=error)

@users_blueprint.route("/users/delete", methods=['POST'])   # pragma: no cover)
@login_required
def deleteuser():
    from coinage import db
    from models import User
    if not current_user.can_delete:
        return redirect(url_for('users.users'))
    id = request.form['userid']
    user = User.query.filter_by(id=id).first()
    if not user is None:
        db.session.delete(user)
        db.session.commit()
        return redirect(url_for('users.users'))

@users_blueprint.route(
    '/users/create', methods=['GET', 'POST'])   # pragma: no cover
def add():
    from coinage import db
    from models import User
    if not current_user.can_create:
        return redirect(url_for('users.users'))
    form = AddForm()
    error = None
    if form.validate_on_submit():
        user = User.query.filter_by(name=form.username.data.strip()).first()
        if user is None:
            user = User(
                name=form.username.data,
                email=form.email.data,
                password=form.password.data,
                can_create=form.can_create.data,
                can_update=form.can_update.data,
                can_delete=form.can_delete.data
            )
            # if request.method == 'POST':
            #     user.can_create = int(request.form.get('can_create_hv', 0))
            #     user.can_delete = int(request.form.get('can_delete_hv', 0))
            #     user.can_update = int(request.form.get('can_update_hv', 0))
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('users.users'))
        else:
            error = 'User name ' + form.username.data + ' is already taken.'
    return render_template('add.html', form=form, error=error)
