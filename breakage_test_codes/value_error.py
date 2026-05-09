"""
PHASE 7: THE VALUEERROR (The Format Conflict)
Logic: The data type is correct, but the actual value is inappropriate.
"""

# -----------------------------------------------------------------
# 7.1 THE IMPOSSIBLE CONVERSION
# -----------------------------------------------------------------
# WHY: You told Python to turn a string into an integer, but the string has letters.
# BREAK:
# raw_data = "Twelve"
# count = int(raw_data)

# FIX:
raw_data = "12" # String must contain only digits
count = int(raw_data)


# -----------------------------------------------------------------
# 7.2 THE UNPACKING MISMATCH
# -----------------------------------------------------------------
# WHY: You tried to assign multiple values to variables, but the counts don't match.
# BREAK:
# first_name, last_name = "Fazal", "Abbas", "SaaS"

# FIX:
first_name, last_name, role = "Fazal", "Abbas", "SaaS"


# -----------------------------------------------------------------
# 7.3 THE MATH DOMAIN ERROR
# -----------------------------------------------------------------
# WHY: You performed a math operation that is logically impossible for the given value.
# BREAK:
# import math
# print(math.sqrt(-10)) # Cannot square root a negative number in basic math

# FIX:
import math
print(math.sqrt(10))


# -----------------------------------------------------------------
# 7.4 THE DATE/TIME FORMAT CLASH
# -----------------------------------------------------------------
# WHY: You provided a value that doesn't fit the expected format (e.g., month 13).
# (Note: This uses the datetime module which you'll see in later chapters).
# BREAK:
# from datetime import datetime
# invalid_date = datetime(2026, 13, 1) # Month 13 does not exist

# FIX:
from datetime import datetime
valid_date = datetime(2026, 12, 1)


# -----------------------------------------------------------------
# 7.5 THE STRING FIND ERROR (Index method)
# -----------------------------------------------------------------
# WHY: Using .index() to find a word that isn't in the string.
# BREAK:
# text = "Agentic Architecture"
# print(text.index("Legacy"))

# FIX (Use .find() instead, which returns -1 instead of crashing):
text = "Agentic Architecture"
print(text.find("Legacy"))