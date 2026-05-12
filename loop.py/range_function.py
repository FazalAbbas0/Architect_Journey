"""
SOVEREIGN DEFINITION: THE RANGE ENGINE
Logic: Generating precise sequences for industrial auditing.
Architect: Fazal Abbas (Clerk_Agentic_AI_Engineer)
Location: loop.py/range_function.py
"""

# =================================================================
# PATTERN 1: THE SIMPLE COUNTER (Start at 0, Stop before 10)
# =================================================================
# Logic: Generates 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
# Use: When you need to repeat a task a fixed number of times.

print("--- [MODULE 1: SEQUENTIAL SCAN] ---")
for i in range(10):
    print(f"Scanned Shelves: {i}")


# =================================================================
# PATTERN 2: THE DEFINED BOUNDARY (Start at 10, Stop before 15)
# =================================================================
# Logic: Generates 10, 11, 12, 13, 14
# Use: Auditing a specific "Block" of records in the database.

print("\n--- [MODULE 2: BLOCK AUDIT] ---")
for record_id in range(10, 15):
    print(f"Auditing Record: {record_id}")


# =================================================================
# PATTERN 3: THE STEP FILTER (Start 0, Stop 10, Jump by 2)
# =================================================================
# Logic: Generates 0, 2, 4, 6, 8
# Use: High-speed scanning (skipping every second shelf).

print("\n--- [MODULE 3: FAST-TRACK SCAN] ---")
for shelf in range(0, 10, 2):
    print(f"Fast-Scanning Shelf: {shelf}")


# =================================================================
# PATTERN 4: THE REVERSE COUNTDOWN (Start 5, Stop 0, Step -1)
# =================================================================
# Logic: Generates 5, 4, 3, 2, 1
# Use: Safety protocols, system timeouts, or emergency shutdowns.

print("\n--- [MODULE 4: EMERGENCY LOCKDOWN] ---")
for seconds in range(5, 0, -1):
    print(f"System Lockdown in {seconds}...")


print("\n--- RANGE ENGINE OPERATIONS COMPLETE ---")