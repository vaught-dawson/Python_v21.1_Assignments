import string


x = [[5, 2, 3], [10, 8, 9]]
students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'}
]
sports_directory = {
    'basketball': ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer': ['Messi', 'Ronaldo', 'Rooney']
}
z = [{'x': 10, 'y': 20}]

# print(x)
x[1][0] = 15
# print(x)

# print(students)
students[0]['last_name'] = 'Bryant'
# print(students)

# print(sports_directory)
sports_directory['soccer'][0] = 'Andres'
# print(sports_directory)

# print(z)
z[0]['y'] = 30
# print(z)

students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]


def iterateDictionary(name_list):
    for dict in name_list:
        for key in dict:
            print(f'{key} - {dict[key]}, ')


def iterateDictionary2(key_name, some_list):
    for dict in some_list:
        print(dict[key_name])


# iterateDictionary(students)
# iterateDictionary2('first_name', students)
# iterateDictionary2('last_name', students)

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}


def printInfo(some_dict):
    for key in some_dict:
        print(f'{len(some_dict[key])} {key.upper()}')
        for val in some_dict[key]:
            print(val)
        print('')


printInfo(dojo)
