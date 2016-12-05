import os

#os.environ['DATABASE_URL'] = "mysql+mysqldb://coinage:beer_180JKL:@coinage.mysql.pythonanywhere-services.com/coinage$savings"
os.environ['DATABASE_URL'] = "mysql+mysqldb://root:jasper@localhost:3306/coinage"

from coinage import db
from users.models import User

# create the database and the db table
db.create_all()
#insert
db.session.add(User("admin","marzim@gmail.com", "jasper"))
# commit the changes
db.session.commit()
