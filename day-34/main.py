# Declare a variable without setting value, but hinting the type.
# age: int
# name: str
# height: float
# is_human: bool
#
# age = 12

# -> specifies output type of function.
def police_check(age: int) -> bool:
    return age > 18


if police_check(12):
    print("you may pass")
else:
    print("Pay a fine.")
