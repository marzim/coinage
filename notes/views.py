from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

notes_blueprint = Blueprint('notes', __name__, static_url_path='/notes/static', static_folder='./static',
                      template_folder='./templates')

@notes_blueprint.route("/notes")
def notes():
    try:
        return render_template('notes.html')
    except TemplateNotFound:
        abort(404)

@notes_blueprint.route("/notes/new")
def newnote():
    try:
        return render_template("newnote.html")
    except TemplateNotFound:
        abort(404)

@notes_blueprint.route("/notes/edit")
def editnote():
    try:
        return render_template("editnote.html")
    except TemplateNotFound:
        abort(404)


