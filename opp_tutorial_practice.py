# ============================== LECTURE 1 (Classes and Instances) ==================================================================

#  Define a new class called Employee 
from functools import total_ordering


class Employee():
    # Use a method to define attributes of class Employee 
    # When we create methods within a class, they receive the instance as first argument automatically
    # By convention the first argument of in-class methods/instance is called "self"
    # __init__ initializes attributes of our class by taking instance of class as first argument
    
    def __init__(self, first, last, company, salary):
        self.first  = first
        self.last = last
        self.company = company
        self.email = first + "." + last + f"@{company}.com"
        self.salary = salary
    
    # Let's define a new method in our Employee class to get full names of employess
    def fullname(self):
        return (self.first + " " + self.last)

emp1 = Employee("hussam", "haq", "zembuilders", 800000)
emp2 = Employee("alishan", "soni", "zembuilders", 400000)

#print(emp1.email)
#print(emp2.email)


# Let's use the fullname method of our Employee class to get full name of emp1

#print(emp1.fullname()) # instance.method (instance automatically passed on as method's argument)

# =========== or ===============

print(Employee.fullname(emp1)) #class.method(instance as argument required)
print(Employee.fullname(emp2))
print(emp2.fullname())

# ======================= Lecture 1 Practice =============================================================

# --------------------------------------------------------------------------------------------------------

# Let's make a new class called 'Items' that must have objects representing items of a grocery store.
# Objects/instances of class Items must have four attributes: item name, available quantity, price, and expiry.
# Using any instances two attributes (price and quantity), write an in-class method to compute possible revenue.

class Items():
    def __init__(self, name, quantity, price, expiry):
        self.name  = name
        self.quantity  = quantity
        self.price = price
        self.expiry = expiry

    def expected_revenue(self):
        return self.price*self.quantity

item_1 = Items("Nestle Yougurt", 50, 170,"10th June 2022")

#print(item_1.price)
#print(Items.expected_revenue(item_1))
#print(item_1.expected_revenue())


# ============= Lecture 2 (Class Variables) ===============================================

class Employee():
    raise_amount = 1.04
    total_employees = 0
    
    def __init__(self, first, last, company, salary):
        # self.first is instance variable/attribute of class Employee
        self.first = first
        self.last = last
        self.company = company
        self.mail = first + "." + last + f"@{self.company}.com"
        self.salary = salary
        Employee.total_employees += 1 # here class.class variable is used because no felxibility across instances is required

    def fullname(self):
        return (self.first + " " + self.last)

    def salary_raise(self):
        self.salary = int(self.salary * self.raise_amount) # here instance.class var is used to allow flexibility acorss instances
        return self.salary

# Let's instantiate two object of class Employee

emp3 = Employee("maida", "khan", "zembuilders", 75000)
emp4 = Employee("dua", "fatima", "zembuilders", 45000)
print(emp3.mail)
print(emp4.fullname())
print(emp4.salary)
print(emp4.salary_raise())
print(emp3.salary)
print(emp3.salary_raise())

# namespace check of an instant
# here the instance emp3 of class Employee inherets class var salary raise  = 1.04
print(emp3.__dict__)
# once we assign new value to salary_raise attribute of emp3, the namespace gets updated to reflect the change
# this is the reason we used instance/self.class var instead of class.class var
# use case -- some employee can get more than standard rasie
emp3.salary_raise = 1.10
print(emp3.__dict__)