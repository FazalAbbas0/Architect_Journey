"""
PHASE 4.2.7: THE MULTI-LEVEL SORT (NESTED LOOPS)
Logic: Deep-scanning hierarchical industrial data structures.
Architect: Fazal Abbas (Silicon Level-11)
"""

# --- MOCK HIERARCHICAL DATA ---
# A 'Concrete' structure: Warehouse Blocks -> Storage Racks -> Specific Items
industrial_site = {
    "Block_A": ["Turbines", "Compressors"],
    "Block_B": ["Generators", "Coolants", "Lubricants"],
    "Block_C": ["Wiring", "Control_Panels"]
}

# =================================================================
# STRATEGY 1: THE HIERARCHICAL SCAN (Nested For Loops)
# Use Case: Inventorying every item across all warehouse blocks.
# =================================================================
print("--- [STRATEGY 1: FULL SITE INVENTORY] ---")
total_item_count = 0

for block, items in industrial_site.items():
    print(f"Entering {block}...")
    for item in items:
        total_item_count += 1
        print(f"  > Scanning Item #{total_item_count}: {item}")
    print(f"Block {block} Scan Complete.\n")


# =================================================================
# STRATEGY 2: THE ANOMALY DETECTOR (Nested Loop + Logic)
# Use Case: Finding a specific high-friction item in a deep stack.
# =================================================================
print("--- [STRATEGY 2: TARGETED SEARCH PROTOCOL] ---")
target_item = "Generators"
found = False

for block, items in industrial_site.items():
    # Inner loop scans the items inside the current block
    for item in items:
        if item == target_item:
            print(f"SUCCESS: {target_item} located in {block}. Locking coordinates.")
            found = True
            break # Breaks the inner loop
    if found:
        break # Breaks the outer loop to save compute power (Silicon L-11 Efficiency)


# =================================================================
# STRATEGY 3: THE MATRIX SCANNER (Coordinate-Based)
# Use Case: Scanning a physical grid (Rows and Columns) of sensor data.
# =================================================================
sensor_grid = [
    [22, 23, 22], # Row 0
    [25, 88, 24], # Row 1 (88 is an anomaly)
    [21, 22, 21]  # Row 2
]

print("\n--- [STRATEGY 3: SENSOR GRID AUDIT] ---")
for r_idx, row in enumerate(sensor_grid):
    for c_idx, val in enumerate(row):
        if val > 30:
            print(f"!!! CRITICAL ANOMALY at Grid[{r_idx}][{c_idx}]: {val}°C")


# =================================================================
# STRATEGY 4: THE FLATTENING PROTOCOL (Nested List Comprehension)
# Use Case: Converting a deep hierarchy into a single 'Steel-Standard' list.
# =================================================================
# 'For every block in the site, and for every item in that block...'
all_items_flat = [item for items in industrial_site.values() for item in items]

print("\n--- [STRATEGY 4: ARCHITECT'S FLATTENING] ---")
print(f"Flattened Global Inventory: {all_items_flat}")

print("\n--- STATUS: MULTI-LEVEL SORT OPERATIONAL ---")