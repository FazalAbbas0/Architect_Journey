"""
PHASE 6: THE INDENTATIONERROR (The Alignment Failure)
Logic: You violated the physical structure of Python's block system.
"""

# -----------------------------------------------------------------
# 6.1 THE "FLUSH LEFT" VIOLATION
# -----------------------------------------------------------------
# WHY: Standard code (outside of loops/functions) must start at the very beginning of the line.
# BREAK:
#  name = "Fazal" # (Notice the single leading space)

# FIX:
name = "Fazal" # (No space before the variable)


# -----------------------------------------------------------------
# 6.2 THE MISSING BLOCK INDENT
# -----------------------------------------------------------------
# WHY: After a colon (:), Python expects the next line to be indented (usually 4 spaces).
# BREAK:
# if True:
# print("This will fail")

# FIX:
if True:
    print("This is correctly indented")


# -----------------------------------------------------------------
# 6.3 THE TAB VS SPACE CONFLICT
# -----------------------------------------------------------------
# WHY: Mixing 'Tabs' and 'Spaces' in the same file confuses the interpreter.
# Modern VS Code usually prevents this, but old files might have it.
# BREAK:
# def example():
#     print("Indented with spaces")
# 	print("Indented with a tab") # (Looks the same, but different characters)

# FIX:
# In VS Code, click "Spaces: 4" in the bottom right corner 
# and select "Convert Indentation to Spaces."


# -----------------------------------------------------------------
# 6.4 THE UNEXPECTED INDENT
# -----------------------------------------------------------------
# WHY: Indenting a line that has no reason to be indented.
# BREAK:
# name = "Abbas"
#     print(name) # (Why is this indented? There was no colon above it.)

# FIX:
name = "Abbas"
print(name)


# -----------------------------------------------------------------
# 6.5 THE HALF-HEARTED INDENT
# -----------------------------------------------------------------
# WHY: Using an inconsistent number of spaces (e.g., 2 spaces instead of 4).
# BREAK:
# if True:
#   print("Only 2 spaces")
#     print("Now 4 spaces") # (Mismatch!)

# FIX:
if True:
    print("Consistently 4 spaces")
    print("Also 4 spaces")