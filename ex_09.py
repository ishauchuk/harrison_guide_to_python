year = int(input("Enter year:\n"))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(f'{year} is bis sextus year')

number = int(input("Enter number:\n"))
if number % 2 == 0:
    print(f"'{number}' is even number")