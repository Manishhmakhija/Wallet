# calling a function


def function():
    print("Hello Project")


function()

print()


# arguments
def function(fname):
    print(fname + " Makhija ")
    print(fname + " Rohra")


function("Manish")

print()


# number of arguments
def function(fname, mname, lname):
    print(fname + "" + mname + "" + lname)


function("Manish", " Rakesh ", " Makhija ")

print()


# default parameter value
def function(country="India"):
    print("I am from " + country)


function()
function("USA")
function("Russia")

print()


# return value
def function(x):
    return 7 * x


print(function(4))
print(function(7))
