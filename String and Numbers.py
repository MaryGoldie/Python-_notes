# STRING AND NUMBERS
print("Have a good day!")  # string
print(200)  # integer
print(3.5)  # float

# Simple calculation on how many minutes in 20days
print("20days are " + str(20 * 24 * 60) + " minutes")  # string concatenation # common way
print(20 * 24 * 60)  # days,hrs,minutes

print(f"20 days are {20 * 24 * 60} minutes")  # elegant way to add non-textual value / only works for latest version
# f stands for format

# calculating seconds
print("20 days are " + str(20 + 24 + 60 + 60) + " seconds")
print(f"20 days are {20 + 24 +60 +60} seconds")