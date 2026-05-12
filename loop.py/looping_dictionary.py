"""
SOVEREIGN DEFINITION: DICTIONARY ITERATION
Logic: Accessing high-fidelity inventory data structures.
Architect: Fazal Abbas (Clerk_Agentic_AI_Engineer)
Location: loop.py/looping_dictionary.py
"""

# THE DATASET: A small-scale version of your Level-1 Warehouse
pharmacy_inventory = {
    "Adrenaline": 20000,
    "Morphine": 15000,
    "Atropine": 8000
}

# =================================================================
# 1. LOOPING THROUGH KEYS (.keys())
# =================================================================
# Logic: Use this when you only need the NAME of the medicine.
# Note: Iterating over the dict itself defaults to keys.

print("--- [MODULE 1: MEDICINE NAME SCAN] ---")
for med_name in pharmacy_inventory.keys():
    print(f"Inventory Item: {med_name}")


# =================================================================
# 2. LOOPING THROUGH VALUES (.values())
# =================================================================
# Logic: Use this when you only care about the QUANTITY, not the name.

print("\n--- [MODULE 2: STOCK VOLUME AUDIT] ---")
for stock_qty in pharmacy_inventory.values():
    print(f"Units Found: {stock_qty:,}")


# =================================================================
# 3. LOOPING THROUGH BOTH (.items()) — THE ARCHITECT'S CHOICE
# =================================================================
# Logic: This is the most used in your 560-line engine. 
# It unpacks the Key and Value simultaneously.

print("\n--- [MODULE 3: COMPREHENSIVE RECONCILIATION] ---")
for name, qty in pharmacy_inventory.items():
    status = "SECURE" if qty > 10000 else "REORDER"
    print(f"Report: {name:<10} | Stock: {qty:>6,} | Status: {status}")


print("\n--- DICTIONARY SCAN COMPLETE ---")