from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
from flask_login import login_required

summary_blueprint = Blueprint('summary', __name__, static_folder='static', static_url_path='/static/summary',
                      template_folder='./templates')

@summary_blueprint.route("/summary")
@login_required
def summary():
    try:
        return render_template('summary.html')
    except TemplateNotFound:
        abort(404)



