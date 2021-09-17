# 1. Create a 3x3 matrix that will contain the squares of the numbers from 1-9 using a nested loop.
# Օգտագործելով ցիկլեր, ստեղծել 3x3 մատրից, որը կպարունակի 1-9 թվերի քառակուսիները։

for x in range(1, 10):
    b = x ** 2
    print(b)
# Պետք է մատրից ստեղծենք, այսինքն երկչափանի լիստ, ոչ թե պրինտ։

# 2. Create a 3x3 matrix that will contain the squares of the numbers from 1-9 using a list comprehension.
# Օգտագործելով comprehension, ստեղծել 3x3 մատրից, որը կպարունակի 1-9 թվերի քառակուսիները։


# 4. Count the number of 'b's in the given string. DO NOT use the count() method.
# Հաշվել տրված սթրինգում 'b'-երի քանակը։ Չօգտագործել count() մեթոդը։
nonsense = 'Blinking blindly, brainy Bob brings beautiful beer bottles beneath blue butterflies billowing brilliantly.'
total = 0
for a in nonsense:
    if a == 'b' or a == 'B':
        total += 1
print(total)
# 5. Write a program that will print the factorial of n.
# Գրել ծրագիր, որը կտպի n թվի ֆակտորիալը։
z = int(input("enter number"))
total_1 = 1
for c in range(1, z + 1):
    total_1 *= c
print(total_1)

# Լավ է
