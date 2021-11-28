hours = [6, 2, 7, 8, 5, 6, 5, 7, 1, 8.5]
print(sum(hours) / len(hours))

print(297 % 3 == 0)

print(2 ** 10)

for elem in [1800, 1900, 1903, 2000, 2002]:
    if elem % 4 == 0 and elem % 100 != 0 or elem % 400 == 0:
        print(f'{elem} is bis sextus year')
