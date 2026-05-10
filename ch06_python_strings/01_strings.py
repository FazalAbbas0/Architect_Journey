# Multi-line Strings
# you can assigned many lines strings to a variable but after use of triple quote marks only
agents_power = """
you can solve multiple problems
after use of that agentic ai architect 
system, which would allow to run multiple
agents at once time on multiple tasks"""
# Modify Strings
a = "hello world!"
print(a.upper())
a = "HELLO WORLD!"
print(a.lower())
# Remove Whitespaces
a = "Ahmed Khan"
print(a)
print(a.strip())
# Replace string
print(a.replace("Ahmed", "Ibrar"))
# Split function
# Option 1: Split by space explicitly
print(a.split(" ")) 

# Option 2: Default split (handles any whitespace: spaces, tabs, newlines)
print(a.split())