import string

age = 29
old = age > 18
print(True if old else False)

name = 'Ihar'
second_half = list(string.ascii_lowercase)[13:]
print(True if name[0].lower() in second_half else False)


names = [['Alex', 'Daria', 'Serg'], []]
num = 1

for i in names:
    if i:
        print(f"The class {num} has enrollments.")
    else:
        print(f"The class {num} is empty!")
    num += 1

car = None
if not car:
    print("Taxi for you!")
else:
    print("You have a car!")
