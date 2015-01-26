import operator

def count_words(some_file):
    simple_dict = {}
    with open(some_file, 'r') as f:
        for rand_string in f.read().lower().split():
            if rand_string in simple_dict:
                simple_dict[rand_string] += 1
            else:
                simple_dict[rand_string] = 1
    return simple_dict

def sort_rev(some_dict):
    return sorted(some_dict.items(), key=operator.itemgetter(1), reverse = True)


def pretty_output(some_list):
    for i, (a, b) in enumerate(some_list):
        print(a + " ==> " + str(b), end = "\n")

counted_words = count_words('bible.txt')

pretty_output(sort_rev(counted_words))
