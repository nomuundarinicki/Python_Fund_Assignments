# Names Assignment
# Practice unpacking lists and dictionaries.

# Part I
STUDENTS = [
    {'first_name':  'Nicki', 'last_name' : 'Bob'},
    {'first_name' : 'Claudiu', 'last_name' : 'Bancilia'},
    {'first_name' : 'HI', 'last_name' : 'BYE'},
    {'first_name' : 'tom', 'last_name' : 'Jerry'}
]

def print_names_from_list(name_list):
    for each in range(0, len(name_list)):
        print name_list[each]['first_name'], name_list[each]['last_name']

print_names_from_list(STUDENTS)

print ''

# Part II
USERS = {
    'Students': [
        {'first_name':  'Nicki', 'last_name' : 'BOBBY'},
        {'first_name' : 'HI', 'last_name' : 'BYE'},
        {'first_name' : 'Claudiu', 'last_name' : 'Bancilia'},
        {'first_name' : 'Tom', 'last_name' : 'JERRY'}
    ],
    'Instructors': [
        {'first_name' : 'Michael', 'last_name' : 'Choi'},
        {'first_name' : 'Martin', 'last_name' : 'Puryear'}
    ]
}

def print_students_and_instructors(matrix):
    for key in matrix:
        print key
        count = 0
        for each in range(0, len(matrix[key])):
            count += 1
            first_name = matrix[key][each]['first_name'].upper()
            last_name = matrix[key][each]['last_name'].upper()
            print (str(count) + ' - ' + first_name + ' ' + last_name + ' - ' +
                   str(len(first_name + last_name)))

print_students_and_instructors(USERS)
