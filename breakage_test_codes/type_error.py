"""
PHASE 3: THE TYPEERROR (Species Conflict)
Logic: You tried to perform an operation on data that doesn't support it.
"""

# -----------------------------------------------------------------
# 3.1 THE STRING + INTEGER CLASH (Concatenation)
# -----------------------------------------------------------------
# WHY: You cannot 'add' a mathematical number to a piece of text.
# BREAK:
# score = 95
# print("Your score is: " + score)

# FIX (The Typecasting Method):
score = 95
print("Your score is: " + str(score))


# -----------------------------------------------------------------
# 3.2 THE MATH ON TEXT TRAP
# -----------------------------------------------------------------
# WHY: You cannot perform math (like subtraction or division) on strings.
# BREAK:
# price = "500"
# total = price / 2

# FIX (Convert to Float or Int first):
price = "500"
total = int(price) / 2


# -----------------------------------------------------------------
# 3.3 THE UNSUPPORTED CALL (Non-Callable)
# -----------------------------------------------------------------
# WHY: You treated a variable (like an integer) as if it were a function.
# BREAK:
# count = 10
# count() # Trying to 'call' a number like a command

# FIX:
count = 10
print(count) # Just use the variable normally


# -----------------------------------------------------------------
# 3.4 THE ITERATION ERROR
# -----------------------------------------------------------------
# WHY: You tried to "loop" through or "count" a number. Only strings/lists can be counted.
# BREAK:
# phone_number = 923000000
# print(len(phone_number))

# FIX:
phone_number = 923000000
print(len(str(phone_number))) # Convert to string to count the digits


# -----------------------------------------------------------------
# 3.5 THE MIXED LIST SORTING
# -----------------------------------------------------------------
# WHY: Python cannot compare 'apples and oranges' when sorting or comparing.
# BREAK:
# result = 10 > "5"

# FIX:
result = 10 > int("5") # Ensure both sides are the same species