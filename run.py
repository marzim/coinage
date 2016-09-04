from coinage import app, db
from users.models import User

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)

