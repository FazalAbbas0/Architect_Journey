"""
PHASE 4.2.5: THE METADATA MAPPER (DICTIONARY ITERATION)
Logic: High-precision extraction of Key-Value pairs for Industrial RAG.
Architect: Fazal Abbas (Silicon Level-11)
"""

# --- MOCK INDUSTRIAL DATABASE ---
# A complex dictionary representing a European Medical Supply Chain.
medical_inventory = {
    "BATCH-001": {"item": "MRI Scanner", "origin": "Germany", "status": "Secure"},
    "BATCH-002": {"item": "Surgical Kits", "origin": "Pakistan", "status": "In-Transit"},
    "BATCH-003": {"item": "Vaccine Vials", "origin": "Belgium", "status": "Audit_Required"}
}

# =================================================================
# STRATEGY 1: THE KEY SCANNER (.keys())
# Use Case: Just checking which Batch IDs are currently in the system.
# =================================================================
print("--- [STRATEGY 1: SYSTEM ID AUDIT] ---")
for batch_id in medical_inventory.keys():
    print(f"Detected System ID: {batch_id}")


# =================================================================
# STRATEGY 2: THE CONTEXT EXTRACTOR (.values())
# Use Case: Checking the health of the cargo without caring about IDs.
# =================================================================
print("\n--- [STRATEGY 2: GLOBAL STATUS CHECK] ---")
for details in medical_inventory.values():
    if details['status'] == "Audit_Required":
        print(f"!!! WARNING: {details['item']} from {details['origin']} needs attention.")
    else:
        print(f"Status Green: {details['item']} is {details['status']}")


# =================================================================
# STRATEGY 3: THE FULL ARCHITECT SYNC (.items())
# Use Case: The 'Steel-Standard' for building B2B Dashboards.
# =================================================================
print("\n--- [STRATEGY 3: FULL SOVEREIGN SYNC] ---")
# .items() returns both the Key and the Value as a Tuple
for batch_id, info in medical_inventory.items():
    print(f"Processing {batch_id}...")
    print(f"  > Item: {info['item']}")
    print(f"  > Port of Origin: {info['origin']}")
    print(f"  > Logistics State: {info['status']}")
    print("-" * 30)


# =================================================================
# STRATEGY 4: DYNAMIC FILTERING (Dictionary Comprehension)
# Use Case: Instantly creating a sub-vault for a specific client.
# =================================================================
# Goal: Create a new vault only for items from Pakistan.
local_vault = {k: v for k, v in medical_inventory.items() if v['origin'] == "Pakistan"}

print("\n--- [STRATEGY 4: FILTERED SUB-VAULT] ---")
print(f"Pakistan Sourced Data: {local_vault}")

print("\n--- STATUS: METADATA MAPPING COMPLETE ---")