a = 1
while a < 9:
    print(a)
    a += 1

print()

# break statement
a = 1
while a < 8:
    print(a)
    if a == 4:
        break
    a += 1

print()

# do not print the particular thing from the list
a = 0
while a < 6:
    a += 1
    if a == 4:
        continue
    print(a)

print()

# else
a = 1
while a < 7:
    print(a)
    a += 1
else:
    print("FIND 7")
