from collections import namedtuple

# The information of the employee
Employee = namedtuple("Employee", ("ID", "name", "Role", "psswdhash"))
# psswdhash (password) = hash which returns the hash value of the given option,
# this gives a good 'randomized' password

Alex = Employee("101", "Alex", "Cashier", psswdhash=hash("I cant remember!"))
Sam = Employee("102", "Sam", "Delivery driver", psswdhash=hash("do you know?"))
Jo = Employee("103", "Jo", "Clerk", psswdhash=hash("i dont know!"))

employees = [Alex, Sam, Jo]

print(employees)
