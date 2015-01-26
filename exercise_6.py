def non_existent(some_file):
    with open(some_file, 'r') as f:
        f.read()


def yet_another_func(some_file):
    non_existent(some_file)


def main(some_file):
    try:
        yet_another_func(some_file)
    except FileNotFoundError:
        print("File not found.")

main("goonies.txt")
