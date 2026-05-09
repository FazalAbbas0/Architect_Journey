"""
PHASE 1: THE NAMEERROR (Identity Failures)
Logic: Python cannot find the 'label' you are trying to use.
"""

# -----------------------------------------------------------------
# 1.1 THE FORGOTTEN ASSIGNMENT
# -----------------------------------------------------------------
# WHY: Trying to print or use a variable before you have created it.
# BREAK:
# print(agent_salary) 

# FIX:
agent_salary = 5000 
print(agent_salary)


# -----------------------------------------------------------------
# 1.2 THE STRING QUOTE SLIP
# -----------------------------------------------------------------
# WHY: Forgetting quotes around text. Python thinks the text is a variable.
# BREAK:
# city = Lahore 

# FIX:
city = "Lahore"


# -----------------------------------------------------------------
# 1.3 THE SPELLING MISMATCH (Case Sensitivity)
# -----------------------------------------------------------------
# WHY: Python is case-sensitive. 'User' is not the same as 'user'.
# BREAK:
# Full_Name = "Fazal"
# print(full_name) # 'f' is lowercase here, but uppercase above.

# FIX:
full_name = "Fazal"
print(full_name)


# -----------------------------------------------------------------
# 1.4 THE BOOLEAN LOWERCASE TRAP
# -----------------------------------------------------------------
# WHY: 'True' and 'False' are reserved keywords and MUST be capitalized.
# BREAK:
# is_agent_active = true 

# FIX:
is_agent_active = True


# -----------------------------------------------------------------
# 1.5 THE SCOPE GAP (Local vs. Global)
# -----------------------------------------------------------------
# WHY: A variable created inside a "Function" cannot be seen outside it.
# (Note: You will learn Functions later, but this is a major NameError source).
# BREAK:
# def my_function():
#     secret_code = "XYZ"
#
# print(secret_code) # Error: 'secret_code' only exists inside the function.

# FIX:
secret_code = "XYZ" # Define it globally (outside)
print(secret_code)


# -----------------------------------------------------------------
# 1.6 THE MODULE MISS (ImportError / NameError)
# -----------------------------------------------------------------
# WHY: Trying to use a tool (like 'math' or 'os') without importing it first.
# BREAK:
# print(math.sqrt(16))

# FIX:
import math
print(math.sqrt(16))