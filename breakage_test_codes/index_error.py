"""
PHASE 4: THE INDEXERROR (The Boundary Breach)
Logic: You tried to access a position in a sequence that is out of range.
"""

# -----------------------------------------------------------------
# 4.1 THE OVER-REACH (Positive Index)
# -----------------------------------------------------------------
# WHY: Python starts counting at 0. A string of length 3 only goes up to index 2.
# BREAK:
# name = "Ali" # indices are: 0('A'), 1('l'), 2('i')
# print(name[3])

# FIX:
name = "Ali"
print(name[2]) # Access the last valid character


# -----------------------------------------------------------------
# 4.2 THE EMPTY STRING TRAP
# -----------------------------------------------------------------
# WHY: An empty string has NO indices. Even index 0 is out of range.
# BREAK:
# status = ""
# print(status[0])

# FIX:
status = ""
if len(status) > 0:
    print(status[0])
else:
    print("Empty string: No index to access.")


# -----------------------------------------------------------------
# 4.3 THE NEGATIVE SLIP (Negative Indexing)
# -----------------------------------------------------------------
# WHY: Negative indices start at -1 (the last char). Over-reaching backwards also fails.
# BREAK:
# tech = "AI" # indices are: -1('I'), -2('A')
# print(tech[-3])

# FIX:
tech = "AI"
print(tech[-1]) # Safely access the last character


# -----------------------------------------------------------------
# 4.4 THE "VIBE" INDEXING (Logic Error)
# -----------------------------------------------------------------
# WHY: Thinking the index is the same as the "Human" count (1-based).
# BREAK:
# msg = "Hello"
# # I want the 5th letter, so I use 5? No.
# print(msg[5]) 

# FIX (The N-1 Rule):
msg = "Hello"
print(msg[4]) # 5th letter is always index 4


# -----------------------------------------------------------------
# 4.5 THE LIST-SPECIFIC INDEX ERROR
# -----------------------------------------------------------------
# WHY: While we are on Strings, this also happens in Lists (which you will learn next).
# BREAK:
# agents = ["Neural", "Flow"]
# print(agents[2])

# FIX:
agents = ["Neural", "Flow"]
print(agents[1])