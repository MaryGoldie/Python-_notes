# PRACTICE FOR STRING,NUMBERS,VARIABLES,FUNCTIONS

calculation_of_unit = 24
number_of_units = "hours"

print(f"1 days are {1 * calculation_of_unit} {number_of_units}")


def days_to_units(number_of_days):
    print(f"1 day are {number_of_days * calculation_of_unit} {number_of_units}")


days_to_units(1)


def days_to_units(num_of_days):
    print(f"{num_of_days} day are {num_of_days * calculation_of_unit} {number_of_units}")


days_to_units(10)