# ============================== LECTURE 1 ==================================================================

#  Define a new class called Employee 
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

print(emp1.email)
print(emp2.email)


# Let's use the fullname method of our Employee class to get full name of emp1

print(emp1.fullname()) # instance.method (instance automatically passed on as method's argument)

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

print(item_1.price)
print(Items.expected_revenue(item_1))
print(item_1.expected_revenue())