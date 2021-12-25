import main

calculation_to_hours = 24
calculation_to_minutes = 24 * 60
calculation_to_seconds = 24 * 60 * 60
name_of_unit = "seconds"


def days_to_minutes(num_of_days):
    return f"{num_of_days} days are {num_of_days * calculation_to_minutes} minutes"


def days_to_hours(num_of_days):
    return f"{num_of_days} days are {num_of_days * calculation_to_hours} hours"


def days_to_units(num_of_days, conversion_unit):
    if conversion_unit == "hours":
        return f"{num_of_days} days are {num_of_days * calculation_to_hours} {conversion_unit}"
    elif conversion_unit == "minutes":
        return f"{num_of_days} days are {num_of_days * calculation_to_minutes} {conversion_unit}"
    else:
        return "unsupported unit"


def scope_check(num_of_days):
    print(name_of_unit)
    print(num_of_days)


#
# scope_check(20)
# days_to_minutes(35)
def validate_and_execute(days_and_unit_dictionary):
    try:
        user_input_number = int(main.days_and_unit_dictionary["days"])
        # we want to do conversion only for positive integrate
        if user_input_number > 0:
            calculated_value = days_to_units(user_input_number, main.days_and_unit_dictionary["unit"])
            print(calculated_value)
            # print(days_to_hours(user_input_number))
        elif user_input_number == 0:
            print("you entered a 0, please enter positive number")
        else:
            print("you entered a negative, no conversion for you!")

    except ValueError:
        print("your input is not a number. Don't ruin my program!")


user_input_message = "Enter a number of days and conversion unit!\n"
