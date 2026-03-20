name=input("enter your name:")

birthyear_str=input("enter your birth year:")


birthyear=int(birthyear_str)

age=2026-birthyear


print(f"\nType of 'name': {type(name)}")
print(f"Type of 'birthyear_str': {type(birthyear_str)}")
print(f"Type of 'birthyear' (after casting): {type(birthyear)}")
print(f"Type of 'age': {type(age)}")

print(f"\nhey {name} you are {age} yearsold")

# Without casting, this would cause a TypeError:
# age = 2026 - birthyear_str  # TypeError: unsupported operand type(s) for -: 'int' and 'str'
# You cannot subtract a string from an integer directly