from temperature import *

temp_dict = {
    "Boston": "0 C",
    "Boise": "48 F",
    "Phoenix": "85 F",
    "Miami": "40 C",
    "Riverside": "30 C",
    "Baltimore": "32 F"
}


for key, value in temp_dict.items():
    if "C" in value:
        print("In " + str(key) + " it is " + str(value[:-1]) +
              "degrees Celsius \n \t which is equivalent to "
              + str(c2f(value[:-1])) +
              " degrees Fahrenheit")
    elif "F" in value:
        print("In " + str(key) + " it is " + str(value[:-1]) +
              "degrees Fahrenheit \n \t which is equivalent to "
              + str(f2c(value[:-1])) +
              " degrees Celsius")