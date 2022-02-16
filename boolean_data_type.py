# CONDITIONALS IF / ELSE
calculation_to_units = 24
name_of_unit = "hours"


def days_to_units(num_of_days):
    # print(num_of_days > 0)  # will tell if it's true or false # simple
    # condition_check = num_of_days > 0   # checking data types
    # print(type(condition_check))

    if num_of_days > 0:
        return f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}"
    else:
        return "You entered a negative value, so no conversion for you "


user_input = input("Hey user, enter a number of days and I will convert it to hours!\n")
user_input_number = int(user_input)

calculated_value = days_to_units(user_input_number)
print(calculated_value)

