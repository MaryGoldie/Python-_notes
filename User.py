# USER
calculation_to_units = 24
name_of_unit = "hours"


def days_to_units(num_of_days):
    return f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}"


# my_var = days_to_units(2)  # returns some value
# print(my_var)

# New line using \ or \n
# input("Hey user , enter a number of days, and I will convert it to hours!\n")


user_input = input("Hey user, enter a number of days and I will convert it to hours!\n")
user_input_number = int(user_input)  # # do casting ( str, int, float ) to make it a number

calculated_value = days_to_units(user_input_number)
print(calculated_value)

# error occur , ten numbers has been printed 24 times
# do casting ( str, int, float )
