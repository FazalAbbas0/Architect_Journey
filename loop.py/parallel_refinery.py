"""
PHASE 4.2.6: THE PARALLEL REFINERY (ZIP ITERATION)
Logic: Synchronizing multiple industrial data streams for Sovereign RAG.
Architect: Fazal Abbas (Silicon Level-11)
"""

# --- MOCK INDUSTRIAL DATA STREAMS ---
# Imagine these are pulled from three different Excel files or APIs
batch_ids = ["B-992", "B-441", "B-102", "B-885"]
product_names = ["Surgical Masks", "MRI Fluid", "Oxygen Tanks", "Stethoscopes"]
stock_levels = [15000, 420, 85, 1200]
warehouse_zones = ["Zone-A", "Zone-C", "Zone-B", "Zone-A"]

# =================================================================
# STRATEGY 1: THE BASIC SYNC (Zipping 2 Streams)
# Use Case: Matching IDs to Names for a quick inventory audit.
# =================================================================
print("--- [STRATEGY 1: BASIC INVENTORY SYNC] ---")
for batch, name in zip(batch_ids, product_names):
    print(f"ID: {batch} | Product: {name}")


# =================================================================
# STRATEGY 2: THE MULTI-STREAM REFINERY (Zipping 4 Streams)
# Use Case: Building a 'Concrete' Industrial Log.
# =================================================================
print("\n--- [STRATEGY 2: FULL DATA-STREAM INTEGRATION] ---")
master_inventory_log = []

for bid, name, qty, zone in zip(batch_ids, product_names, stock_levels, warehouse_zones):
    log_entry = f"ALERT: Low Stock of {name} in {zone}" if qty < 100 else f"Normal: {name} secured."
    print(f"[{bid}] {log_entry}")
    
    # Building a Sovereign Payload for the European Client
    master_inventory_log.append({
        "id": bid,
        "item": name,
        "quantity": qty,
        "location": zone
    })


# =================================================================
# STRATEGY 3: THE UNZIP PROTOCOL (Zip + *)
# Use Case: Reversing the sync to send data back to separate CSV columns.
# =================================================================
print("\n--- [STRATEGY 3: THE DE-COUPLING PROTOCOL] ---")
# If you have a list of paired tuples and need the original lists back
pairs = [("ID_01", "Client_A"), ("ID_02", "Client_B")]
ids, clients = zip(*pairs) # This 'unzips' the data

print(f"Extracted IDs: {ids}")
print(f"Extracted Clients: {clients}")


# =================================================================
# STRATEGY 4: THE DICTIONARY CONVERTER
# Use Case: Instantly creating a lookup map from two lists.
# =================================================================
# Faster than any manual loop for building high-speed RAG lookups.
id_to_zone_map = dict(zip(batch_ids, warehouse_zones))

print("\n--- [STRATEGY 4: INSTANT LOOKUP MAP] ---")
print(f"Zone Map Created: {id_to_zone_map}")

print("\n--- STATUS: PARALLEL REFINERY OPERATIONAL ---")