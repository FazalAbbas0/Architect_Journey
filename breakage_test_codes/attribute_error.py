"""
PHASE 5: THE ATTRIBUTEERROR (The Tool Mismatch)
Logic: You tried to use a method or property that does not exist for that data type.
"""

# -----------------------------------------------------------------
# 5.1 THE STRING METHOD ON NUMBER TRAP
# -----------------------------------------------------------------
# WHY: Methods like .upper(), .lower(), or .title() only exist for Strings.
# BREAK:
# user_id = 786
# print(user_id.upper())

# FIX:
user_id = 786
print(str(user_id).upper()) # Convert to string first to use string tools


# -----------------------------------------------------------------
# 5.2 THE "NONE" OBJECT DISASTER
# -----------------------------------------------------------------
# WHY: If a variable is empty (None), it has no tools at all. 
# This is common in "vibe coding" when a search returns nothing.
# BREAK:
# search_result = None
# print(search_result.strip())

# FIX:
search_result = None
if search_result is not None:
    print(search_result.strip())
else:
    print("Attribute Protection: Result is None, skipping tools.")


# -----------------------------------------------------------------
# 5.3 THE INTEGER DECIMAL MISTAKE
# -----------------------------------------------------------------
# WHY: Trying to use .is_integer() (a Float tool) on a regular Integer.
# BREAK:
# points = 10
# print(points.is_integer())

# FIX:
points = 10.0 # Make it a float species
print(points.is_integer())


# -----------------------------------------------------------------
# 5.4 THE SPELLING SLIP (Method Names)
# -----------------------------------------------------------------
# WHY: You called a tool that doesn't exist because of a typo.
# BREAK:
# text = "Agentic"
# print(text.upperr()) # Extra 'r'

# FIX:
text = "Agentic"
print(text.upper())


# -----------------------------------------------------------------
# 5.5 THE CASE SENSITIVITY IN TOOLS
# -----------------------------------------------------------------
# WHY: Method names are also case-sensitive.
# BREAK:
# word = "tokushu"
# print(word.Upper()) # Should be lowercase .upper()

# FIX:
word = "tokushu"
print(word.upper())