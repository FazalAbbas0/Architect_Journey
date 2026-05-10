"""
PHASE 3: DATA CLEANING & STRUCTURE (THE SOVEREIGN VAULT)
Logic: Deduplication and Structured Mapping for Database Ingestion.
Architect: Fazal Abbas (Silicon Level-11)
"""

# --- RAW INTAKE FROM THE REFINERY ---
# Messy inventory with duplicates from a manual warehouse log
messy_log = ["Masks", "Gloves", "Masks", "Sanitizer", "Gloves"]

# Paired metadata from a shipping document
shipping_meta = [("zone", "EU-West"), ("priority", "High"), ("carrier", "DHL")]

# =================================================================
# 1. THE DEDUPLICATOR (Signal vs. Noise)
# =================================================================
# set(): Instantly removes all duplicate entries.
# This saves storage space in Supabase and prevents RAG confusion.
unique_inventory = set(messy_log)
print(f"--- [CLEANING LOGIC] ---")
print(f"Original Count: {len(messy_log)} | Cleaned Count: {len(unique_inventory)}")
print(f"Unique Vault Items: {unique_inventory}\n")

# =================================================================
# 2. THE MAPPING ENGINE (Supabase Preparation)
# =================================================================
# dict(): Converts paired data into Key-Value stores.
# This is the "Steel-Standard" format for PostgreSQL/Supabase ingestion.
vault_payload = dict(shipping_meta)

# Adding the cleaned inventory to the payload
vault_payload["inventory_list"] = list(unique_inventory)
print(f"--- [VAULT MAPPING] ---")
print(f"Structured Payload: {vault_payload}\n")

# =================================================================
# 3. BOUNDARY GATES (Quality Control)
# =================================================================
# len(): Verify data volume before pushing to the Sovereign Infrastructure.
if len(vault_payload["inventory_list"]) > 0:
    print("STATUS: Payload contains data. Gate: OPEN.")
else:
    print("ALERT: Null Payload detected. Gate: CLOSED.")

# =================================================================
# 4. ENCODING & SECURITY (The Unique Hash)
# =================================================================
# hex(): Creating a unique, low-level identifier for the transaction.
transaction_id = 45098
vault_id_hash = hex(transaction_id)
print(f"Vault Transaction Hash: {vault_id_hash}")

print("\n--- STATUS: DATA SECURED IN SOVEREIGN VAULT ---")