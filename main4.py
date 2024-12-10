# assigning values to class (__init__ function)
class Person:
    def __init__(self, fname, lname, age):
        self.fname = fname
        self.age = age
        self.lname = lname


a1 = Person("Manish", "Makhija", "21")

print(a1.fname)
print(a1.lname)
print(a1.age)

print()


# (__str__ function)
class Person2:
    def __init__(self, fname, lname, age):
        self.fname = fname
        self.lname = lname
        self.age = age

    def __str__(self):
        return f"{self.fname} {self.lname} ({self.age})"


a2 = Person2("Manish", "Makhija", "21")

print(a2)
