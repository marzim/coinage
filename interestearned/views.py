from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
from flask_login import login_required

interestearned_blueprint = Blueprint('interestearned', __name__, static_folder='static', static_url_path='/static/interestearned',
                      template_folder='./templates')

@interestearned_blueprint.route("/interestearned")
@login_required
def interestearned():
    try:
        return render_template('interestearned.html')
    except TemplateNotFound:
        abort(404)



