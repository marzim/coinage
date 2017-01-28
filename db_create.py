import os

#os.environ['DATABASE_URL'] = "mysql+mysqldb://coinage:beer_180JKL:@coinage.mysql.pythonanywhere-services.com/coinage$savings"
#os.environ['DATABASE_URL'] = "mysql+mysqldb://root:jasper@localhost:3306/coinage"
os.environ['FLASK_DATABASE_URL'] = "mysql+mysqldb://root:beer_180JKL:@127.0.0.1:3306/coinage"

from coinage import db
from accounts.models import Account
from users.models import User

# create the database and the db table
db.create_all()
#insert
user = User("guest","marzim@gmail.com", "jasper")
account = Account()
account.User.append(user)
account.create = 0
account.delete = 0
account.update = 0

db.session.add(account)
# commit the changes
db.session.commit()
