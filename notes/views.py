from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
from flask_login import login_required

notes_blueprint = Blueprint('notes', __name__, static_url_path='/notes/static', static_folder='./static',
                      template_folder='./templates')

@notes_blueprint.route("/notes")
@login_required
def notes():
    try:
        return render_template('notes.html')
    except TemplateNotFound:
        abort(404)

@notes_blueprint.route("/notes/new")
@login_required
def newnote():
    try:
        return render_template("newnote.html")
    except TemplateNotFound:
        abort(404)

@notes_blueprint.route("/notes/edit")
@login_required
def editnote():
    try:
        return render_template("editnote.html")
    except TemplateNotFound:
        abort(404)


