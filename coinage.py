
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, current_user

app = Flask(__name__)
bcrypt = Bcrypt(app)
login_manager = LoginManager()
login_manager.init_app(app)
app.config.from_object('config.ProductionConfig')
app.config['SQLALCHEMY_POOL_RECYCLE'] = 299
app.config['SQLALCHEMY_POOL_TIMEOUT'] = 20
db = SQLAlchemy(app)

from home.views import home_blueprint
from contributions.views import contributions_blueprint
from summary.views import summary_blueprint
from loans.views import loans_blueprint
from interestearned.views import interestearned_blueprint
from customers.views import customers_blueprint
from notes.views import notes_blueprint
from guidelines.views import guidelines_blueprint
from users.views import users_blueprint

#register our blueprints
app.register_blueprint(contributions_blueprint)
app.register_blueprint(home_blueprint)
app.register_blueprint(summary_blueprint)
app.register_blueprint(loans_blueprint)
app.register_blueprint(interestearned_blueprint)
app.register_blueprint(customers_blueprint)
app.register_blueprint(notes_blueprint)
app.register_blueprint(users_blueprint)
app.register_blueprint(guidelines_blueprint)

login_manager.login_view = "users.login"

@login_manager.user_loader
def load_user(user_id):
    from users.models import User
    return User.query.filter(User.id == int(user_id)).first()


