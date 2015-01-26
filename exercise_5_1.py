from random import choice
from random import randint
import string


def get_generator():
    my_str = ""
    for i in range(randint(1, 101)):
        my_char = choice(string.ascii_uppercase + string.ascii_lowercase)
        my_str += my_char
    return my_str

with open('project_5.dat', 'w') as f:
    f.write(get_generator())

rand_file = open('project_5.dat', 'r')
read_file = rand_file.read()
rand_file.close()

my_dict = {}

for i in read_file:
    # my_dict[i] = my_dict.get(i, 0) + 1
    if i in my_dict:
        my_dict[i] += 1
    else:
        my_dict[i] = 1

print ("""
****** BEGIN RANDOM STRING ******
\n
""")
print(read_file)
for key in my_dict:
    print(key + " ==> " + str(my_dict[key]), end = ' ')

print ("""
\n
**********************************
""")
