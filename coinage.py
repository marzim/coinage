
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os

app = Flask(__name__)
bcrypt = Bcrypt(app)
login_manager = LoginManager()
login_manager.init_app(app)
app.config.from_object(os.environ['APP_SETTINGS'])
app.secret_key = os.environ['MYSECRETKEY']
db = SQLAlchemy(app)

from home.views import home_blueprint
from contributions.views import contributions_blueprint

#register our blueprints
app.register_blueprint(contributions_blueprint)
app.register_blueprint(home_blueprint)

if __name__ == "__main__":
    app.run()
