import helper

#from helper import *
#import as h
#from helper import validate_and_execute
print("Python programming From zero to a HERO")


print(f"20 days are {20 * helper.calculation_to_minutes} minutes")
print(f"20 days are {20 * helper.calculation_to_seconds} {helper.name_of_unit}")



user_input = ""
while user_input != "exit":
    user_input = input(helper.user_input_message)
    days_and_unit = user_input.split(":")
    print(days_and_unit)
    days_and_unit_dictionary = {"days": days_and_unit[0], "unit": days_and_unit[1]}
    print(days_and_unit_dictionary)
    helper.validate_and_execute()
    print(type(days_and_unit_dictionary))

# "2, 3".split()
# "test".upper()
# [1, 2, 3].count()
