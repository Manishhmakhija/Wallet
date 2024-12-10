a = 10
b = 20

if a > b:
    print("a is greater than b")
else:
    print("NO")

print()

# printing every item in list
cars = ["BMW", "AUDI", "CRETA"]
for x in cars:
    print(x)

print()

# Exit the loop when x is specified with the value
cars = ["BMW", "AUDI", "CRETA"]
for x in cars:
    print(x)
    if x == "BMW":
        break

print()

# loop through the letters
for x in "CRETA":
    print(x)

print()

# do not print the particular thing from the list
cars = ["BMW", "AUDI", "CRETA"]
for x in cars:
    if x == "BMW":
        continue
    print(x)
