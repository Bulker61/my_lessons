my_dict = {'Artem' : [1998],'Natalia' : [2000],'Lyks' : [2020],'Rokki' : [2023]}
print(my_dict)
print(my_dict['Artem'])
print(my_dict.get('Roman'))
my_dict.update({'Daniil': 1991,
                'Bari': 1978})
del_znac = my_dict.pop('Natalia')
print(del_znac)
print(my_dict)

my_set = {1, 1, 3,5,6,3, 4, 2, 'milk', 'ten', str, (1, 2, 3, 4, 5), 'ten'}
print(my_set)
my_set.add('milf')
my_set.add(9)
my_set.remove(4)
print(my_set)