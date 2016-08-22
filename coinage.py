
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

from home.views import home_blueprint
from contributions.views import contributions_blueprint

#register our blueprints
app.register_blueprint(contributions_blueprint)
app.register_blueprint(home_blueprint)

if __name__ == "__main__":
    app.run()
