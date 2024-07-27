# Работа со словарями:

my_dict = {'Alex': 2000, 'Olga': 1999, 'Oksana': 1995}
print('Dict:', my_dict)

print('Existing value:', my_dict['Olga'])

print('Not existing value:', my_dict.get('Igor', 'Такого ключа нет.'))

my_dict.update({'Irina': 2005,
                'Zoya': 1986})
print(my_dict)

o = my_dict.pop(('Olga'))
print('Deleted value:', o)
print('Modified dictionary:', my_dict)

# Работа с множествами:

my_set = {1, 1, 1, 'a', (0, 2, 4), True}
print('Set:', my_set)
my_set.update([6, 5])
my_set.discard(1)
print('Modified set:', my_set)
