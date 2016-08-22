
from flask import Flask, render_template,abort
from jinja2 import TemplateNotFound

app = Flask(__name__)

from contributions.views import contributions_blueprint

@app.route("/")
def home():
    try:
        return render_template("home.html")
    except TemplateNotFound:
        abort(404)

#register our blueprints
app.register_blueprint(contributions_blueprint)

#if __name__ == "__main__":
#    app.run()
