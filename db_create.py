#import os

#os.environ['DATABASE_URL'] = "mysql+mysqldb://coinage:beer_180JKL:@coinage.mysql.pythonanywhere-services.com/coinage$savings"

from coinage import db
from users.models import User

# create the database and the db table
db.create_all()
#insert
#db.session.add(User("marzim","marzim@gmail.com", "mar_180IOP{"))
# commit the changes
db.session.commit()