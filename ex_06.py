name = input('Enter your name:\n')
age = int(input('Enter your age:\n'))
print(f'{name} is {age} year old')
print('{} is {:b} years old'.format(name.capitalize(), age))

paragraph = '\n"Python is a great language!", said Fred. "I don`t'' \never remember having this much fun before."'
print(paragraph)

print("\n\u03F4")
print("\N{GREEK CAPITAL THETA SYMBOL}")

item = 'car'
car = 13499.99
print(f"\n{item:<10}{car:>10,.2f}")