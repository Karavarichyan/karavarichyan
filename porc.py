x = 0
y = 1
z = 1
for x in range(1, 10, 1):
    for y in range(1, 10, 1):
        z = x * y
        if z < 10:
            print(x, "*", y, "= ", z, end='')
        else:
            print(x, "*", y, "=", z, end='')
    print()
