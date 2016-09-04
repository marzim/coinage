from coinage import app, db
from users.models import User

if __name__ == '__main__':
    db.create_all()
    admin = User('matt','matt@ncr.com','test')
    db.session.add(admin)
    db.session.commit()
    app.run(debug=True)

