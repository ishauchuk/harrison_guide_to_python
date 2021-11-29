names = ['alex', 'darie', 'serg', 'John']
length = 0
for i in range(len(names)):
    length += len(names[i])
print("Average name length is {:.2}".format(length / len(names)))
print(names)

for name in names:
    if name == 'John':
        print('Yes, John is in list!')
    else:
        print('Fail')

my_friends = [
    ('Alex', 'Dukvalov', 29),
    ('Serg', 'Charnukha', 29),
    ('Darie', 'Vasko', 26)
]
years = 0
counter = 0
for i in range(len(my_friends)):
    if my_friends[i][2] is None:
        counter += 1
    else:
        years += my_friends[i][2]
average_years = years / (len(my_friends) - counter)
print(f"{average_years:.0f}")

for i in range(len(my_friends)):
    if my_friends[i][2] > average_years:
        print(my_friends[i][0], 'is old')
    else:
        print(my_friends[i][0], 'is young')