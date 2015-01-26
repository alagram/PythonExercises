while True:
    from sys import exit
    print("""
    ******************************************
    EXERCISE 4 - MENU
    ******************************************
    1. Write input to file
    2. Write to screen
    3. Quit
    ******************************************
    """)


    user_choice = input("Enter your choice [1-3] : ")

    if user_choice in ["1", "2"]:
        if user_choice == "1":
            user_input = input("Enter a phrase or sentence: ")
            with open('user_text.txt', 'a+') as f:
                f.write(user_input)
        elif user_choice == "2":
            user_input = input("Enter a phrase: ")
            print(user_input)
    else:
        exit("Shuting down...Bye!")
