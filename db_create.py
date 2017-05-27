import os
import re

#os.environ['FLASK_DATABASE_URL'] = "mysql+mysqldb://coinage:beer_180JKL:@coinage.mysql.pythonanywhere-services.com/coinage$savings"
#os.environ['FLASK_DATABASE_URL'] = "mysql+mysqldb://root:jasper@localhost:3306/coinage"
os.environ['FLASK_DATABASE_URL'] = "mysql+mysqldb://root:beer_180JKL:@127.0.0.1:3306/coinage"

from datetime import date
from coinage import db
from users.models import User
from customers.models import Customer
from loans.models import Loan, Interest

db.drop_all()
# create the database and the db table
db.create_all()
#insert
user = User(1, 1, 1, "guest","marzim@gmail.com", "jasper")
db.session.add(user)
first_names = [ 'test', 'test2', 'test3', 'test4', 'test5', 'test6', 'test7']
last_names = [ 'ting', 'ting2', 'ting3', 'ting4', 'ting5', 'ting6', 'ting7']

for i in range(len(first_names)):
    c = Customer(first_names[i], last_names[i], i + 1, first_names[i].lower() + "@gmail.com",
                        first_names[i].lower() + " address", "1234567", 0)
    db.session.add(c)
    loan = Loan(customer=c, amount=1000, interest=3, payment=100, total_payable=1030, total_payment=100, outstanding_balance=930, fully_paid_on=date.today().strftime('%m-%d-%Y'), date_release=date.today().strftime('%m-%d-%Y'), date_due=date.today().strftime('%m-%d-%Y'))
    db.session.add(loan)


interest = ['3%','4%','5%','6%','7%','8%','9%','10%']
for i in range(len(interest)):
    _interest = Interest()
    _interest.name = interest[i]
    _interest.value = int(re.search(r'\d+', _interest.name).group())
    db.session.add(_interest)


# commit the changes
db.session.commit()
