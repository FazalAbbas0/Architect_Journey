"""
PHASE 2: THE SYNTAXERROR (Grammar & Structural Violations)
Logic: You broke the fundamental laws of Python's writing system.
"""

# -----------------------------------------------------------------
# 2.1 THE ILLEGAL START (The Number Rule)
# -----------------------------------------------------------------
# WHY: Variable names cannot start with a digit.
# BREAK:
# 1st_database = "PostgreSQL"

# FIX:
database_01 = "PostgreSQL"


# -----------------------------------------------------------------
# 2.2 THE SPACE BAR TRAP
# -----------------------------------------------------------------
# WHY: Python uses spaces to separate commands; you cannot have them in names.
# BREAK:
# agent name = "NeuralFlow"

# FIX (Use Underscores):
agent_name = "NeuralFlow"


# -----------------------------------------------------------------
# 2.3 THE FORBIDDEN HYPHEN
# -----------------------------------------------------------------
# WHY: Python sees '-' as a minus sign (subtraction), not a connector.
# BREAK:
# saas-project = "BrusselsShield"

# FIX:
saas_project = "BrusselsShield"


# -----------------------------------------------------------------
# 2.4 THE RESERVED KEYWORD HIJACK
# -----------------------------------------------------------------
# WHY: You cannot use "Sovereign" command words as variable names.
# BREAK:
# if = 10
# pass = "Approved"
# class = "Data Science"

# FIX:
if_value = 10
status_pass = "Approved"
course_class = "Data Science"


# -----------------------------------------------------------------
# 2.5 THE UNCLOSED STRING (The "Hungry" Quote)
# -----------------------------------------------------------------
# WHY: Opening a quote but never closing it. Python keeps looking for the end.
# BREAK:
# lecture_title = "Variables and Strings

# FIX:
lecture_title = "Variables and Strings"


# -----------------------------------------------------------------
# 2.6 THE SPECIAL CHARACTER CHAOS
# -----------------------------------------------------------------
# WHY: Symbols like @, $, and % have special meanings and can't be in names.
# BREAK:
# user@email = "fazal@tech.com"
# price$ = 500

# FIX:
user_email = "fazal@tech.com"
price_usd = 500