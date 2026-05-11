"""
PHASE 4.2.1: THE REFINERY LOOP (BATCH PROCESSING)
Logic: Iteration strategies for high-volume data engineering.
Architect: Fazal Abbas (Silicon Level-11)
"""

# --- MOCK INDUSTRIAL DATA ---
raw_cargo_logs = ["Oil", "Steel", "ERROR_404", "Coal", "Steel", "Empty", "Glass"]
sensor_readings = [22.5, 23.1, 999.0, 22.8, 23.5] # 999.0 is a sensor error
storage_vault = []

# =================================================================
# EXAMPLE 1: THE FILTERING LOOP (For-In)
# Logic: Clean duplicates and skip errors in one pass.
# =================================================================
print("--- [STRATEGY 1: CLEANING & DEDUPLICATION] ---")
seen_items = set() # Using a Set for Silicon Level-11 speed

for item in raw_cargo_logs:
    if item == "ERROR_404" or item == "Empty":
        print(f"Skipping Noise: {item}")
        continue # Skip to next iteration
    
    if item not in seen_items:
        storage_vault.append(item)
        seen_items.add(item)
        print(f"Refined & Vaulted: {item}")

# =================================================================
# EXAMPLE 2: THE THRESHOLD GUARD (While Loop)
# Logic: Process data until a specific capacity is reached.
# =================================================================
print("\n--- [STRATEGY 2: CAPACITY MONITORING] ---")
vault_capacity = 0
MAX_CAPACITY = 3
index = 0

while vault_capacity < MAX_CAPACITY and index < len(storage_vault):
    processed_item = storage_vault[index]
    print(f"Loading to Sovereign Server: {processed_item}")
    vault_capacity += 1
    index += 1

# =================================================================
# EXAMPLE 3: THE TRANSFORMATION LOOP (List Comprehension)
# Logic: Perform logic on an entire list in one line.
# =================================================================
# Goal: Filter out the '999.0' error readings from sensors.
clean_readings = [temp for temp in sensor_readings if temp < 100.0]

print("\n--- [STRATEGY 3: FAST TRANSFORMATION] ---")
print(f"Raw Sensors: {sensor_readings}")
print(f"Clean Sensors: {clean_readings}")

# =================================================================
# EXAMPLE 4: ENUMERATED INDEXING
# Logic: Keeping track of the exact row number for audit logs.
# =================================================================
print("\n--- [STRATEGY 4: AUDIT LOGGING] ---")
for rank, item in enumerate(storage_vault, start=1):
    print(f"Audit Record #{rank}: {item} SECURED")

print("\n--- STATUS: BATCH REFINERY OPERATIONAL ---")