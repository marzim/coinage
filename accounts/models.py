from coinage import db
from users.models import User

association_table = db.Table('association', db.Model.metadata,
    db.Column('account_id', db.Integer, db.ForeignKey('accounts.id')),
    db.Column('user_id', db.Integer, db.ForeignKey('users.id'))
)

class Account(db.Model):
    __tablename__ = "accounts"

    id = db.Column(db.Integer, primary_key=True)
    User = db.relationship('User', secondary=association_table)
    create = db.Column(db.Integer)
    update = db.Column(db.Integer)
    delete = db.Column(db.Integer)

    def __init__(self, userid=None, create=None, update=None, delete=None):
        self.userid = userid
        self.create = create
        self.update = update
        self.delete = delete

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)

    def __repr__(self):
        return '<name - {}>'.format(self.name)


