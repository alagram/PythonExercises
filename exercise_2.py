print """
>>> ======================================== RESTART =============================================
>>>
"""
while True:
    try:
        user_input = float(raw_input("Please enter the number of gallons of gasoline: "))


        print "Original number of gallons is: %s" % user_input
        print "%s gallons is the equivalent of %s liters" % (user_input, (user_input * 3.7854))
        print "%s gallons of gasoline requires %s barrels of oil" % (user_input, (user_input / 19.5))
        print "%s gallons of gasoline produces %s pounds of CO2" % (user_input, (user_input * 20))
        print "%s gallons of gasoline is energy equivalent to %s gallons of ethanol" % (user_input, user_input * (115 / 75.7))
        print "%s gallons of gasoline requires %s US dollars" % (user_input, user_input * 4)
        print "Thanks for playing"
        break
    except ValueError:
        print "Please enter a number."
