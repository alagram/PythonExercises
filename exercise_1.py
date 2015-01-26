print """
<<<===================================== RESTART ==============================
>>>
"""
while True:
    try:
        first_number = int(raw_input("Please enter your first number: "))
        second_number = int(raw_input("Please enter your second number: "))
        add = first_number + second_number
        diff = first_number - second_number
        prod = str(first_number * second_number)
        quo_mod = divmod(first_number, second_number)
        print "The sum of %s and %s is %s." % (first_number, second_number, add)
        print "The difference of %s and %s is %s." % (first_number, second_number, diff)
        print "The product of %s and %s is %s." % (first_number, second_number, prod)
        print "The quotient of %s and %s is: %s with a remainder: %s" % (first_number, second_number, quo_mod[0], quo_mod[1])
        break
    except ZeroDivisionError:
        print "Cannot divide a number by zero. Please try again..."
    except ValueError:
        print "Please enter a number. Please try again..."