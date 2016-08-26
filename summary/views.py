from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

summary_blueprint = Blueprint('summary', __name__, static_url_path='/summary/static', static_folder='./static',
                      template_folder='./templates')

@summary_blueprint.route("/summary")
def summary():
    try:
        return render_template('summary.html')
    except TemplateNotFound:
        abort(404)



