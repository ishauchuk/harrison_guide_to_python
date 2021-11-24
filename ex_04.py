number = 7.0
print([id(number), type(number), number], sep=',', end='\n\n')
number += 20
print([id(number), type(number), number], sep=',', end='\n\n')

empty_list = []
print([id(number), empty_list], sep=',', end='\n\n')
empty_list.append(200)
print([id(number), empty_list], sep=',', end='\n\n')
