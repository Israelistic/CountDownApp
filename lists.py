# Array of list
my_list = ["January", "February", "March"]
print(my_list[2])
my_list.append("April")
print(my_list[3])
for month in my_list:
    print(month)



print("Python programming From zero to a HERO")
calculation_to_hours = 24
calculation_to_minutes = 24 * 60
calculation_to_seconds = 24 * 60 * 60
name_of_unit = "seconds"

print(f"20 days are {20 * calculation_to_minutes} minutes")
print(f"20 days are {20 * calculation_to_seconds} {name_of_unit}")


def days_to_minutes(num_of_days):
    return f"{num_of_days} days are {num_of_days * calculation_to_minutes} minutes"


def days_to_hours(num_of_days):
    return f"{num_of_days} days are {num_of_days * calculation_to_hours} hours"


def scope_check(num_of_days):
    print(name_of_unit)
    print(num_of_days)


#
# scope_check(20)
# days_to_minutes(35)
def validate_and_execute():
    try:
        user_input_number = int(number_of_days_element)
        # we want to do conversion only for positive integrate
        if user_input_number > 0:
            calculated_value = days_to_hours(user_input_number)
            print(calculated_value)
            # print(days_to_hours(user_input_number))
        elif user_input_number == 0:
            print("you entered a 0, please enter positive number")
        else:
            print("you entered a negative, no conversion for you!")

    except ValueError:
        print("your input is not a number. Don't ruin my program!")


user_input = ""
while user_input != "exit":
    user_input = input("Enter a number of days as a comma separated list and I will convert it to hours!\n")
    list_of_days = user_input.split(", ")
    print(list_of_days)
    print(set(list_of_days))

    print(type(list_of_days))
    print(type(set(list_of_days)))

    for number_of_days_element in set(list_of_days):
        validate_and_execute()