# FUNCTIONS

calculation_to_units = 24 * 60 * 60
name_of_unit = "seconds"


def days_to_units(num_of_days, custom_message):
    print(f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}")


days_to_units(35, "All good!")


def scope_check(num_of_days):
    my_var = "variables inside function"
    # function body
    print(name_of_unit)  # global variable
    print(num_of_days)  # local/internal variable
    print(my_var)  # internal variable


scope_check(20)