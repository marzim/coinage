import os

#os.environ['FLASK_DATABASE_URL'] = "mysql+mysqldb://coinage:beer_180JKL:@coinage.mysql.pythonanywhere-services.com/coinage$savings"
#os.environ['FLASK_DATABASE_URL'] = "mysql+mysqldb://root:jasper@localhost:3306/coinage"
os.environ['FLASK_DATABASE_URL'] = "mysql+mysqldb://root:beer_180JKL:@127.0.0.1:3306/coinage"

from coinage import db
from users.models import User
from customers.models import Customer

db.drop_all()
# create the database and the db table
db.create_all()
#insert
user = User(1, 1, 1, "guest","marzim@gmail.com", "jasper")
customer = Customer('marvin','casagnap', 0, 'marzim@gmail.com','liloan','09089685643')
db.session.add(customer)
customer = Customer('marvin2','casagnap2', 5, 'marzim@gmail.com','liloan','09089685643')
db.session.add(customer)
customer = Customer('marvin3','casagnap3', 3, 'marzim@gmail.com','liloan','09089685643')
db.session.add(customer)
db.session.add(user)
# commit the changes
db.session.commit()
