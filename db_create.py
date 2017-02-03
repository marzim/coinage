import os

os.environ['FLASK_DATABASE_URL'] = "mysql+mysqldb://coinage:beer_180JKL:@coinage.mysql.pythonanywhere-services.com/coinage$savings"
#os.environ['FLASK_DATABASE_URL'] = "mysql+mysqldb://root:jasper@localhost:3306/coinage"
#os.environ['FLASK_DATABASE_URL'] = "mysql+mysqldb://root:beer_180JKL:@127.0.0.1:3306/coinage"

from coinage import db
from users.models import User

db.drop_all()
# create the database and the db table
db.create_all()
#insert
user = User(False, False, False, "guest2","marzim@gmail.com", "jasper")

db.session.add(user)
# commit the changes
db.session.commit()
