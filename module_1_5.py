immutable_var = (1, 'good', False, ['fruits', 'egetables', 'berries'])
print(immutable_var)
# immutable_var[1] = 'bio'
# Главное свойство кортежа - это невозможность изменить содержимое

mutable_list = ['fruits', 'egetables', 'berries', 1, 2, 3]
print(mutable_list)
mutable_list[1] = 'fast food'
print(mutable_list)