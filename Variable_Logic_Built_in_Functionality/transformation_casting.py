"""
PHASE 2: TRANSFORMATION & CASTING (THE REFINERY)
Logic: Converting "Messy Species" into "Operational Standards."
Architect: Fazal Abbas (Silicon Level-11)
"""

# --- RAW INTAKE FROM SECURITY GATE ---
raw_id = "1050"              # String species
raw_price = "450.75"         # String species
raw_inventory = ("Masks",)    # Immutable Tuple
raw_status = 1               # Integer representation of Boolean

# =================================================================
# 1. NUMERIC REFINING (The Calculation Logic)
# =================================================================
# int(): Casting string to integer for database IDs.
refined_id = int(raw_id) 
print(f"Refined ID: {refined_id} | New Species: {type(refined_id)}")

# float(): Casting string to float for financial precision.
refined_price = float(raw_price)
print(f"Refined Price: {refined_price} | New Species: {type(refined_price)}")

# =================================================================
# 2. STRING SERIALIZATION (The Reporting Logic)
# =================================================================
# str(): Converting numeric data into strings for PDF labels or LLM prompts.
# This is crucial for your "Agentic Cinema" or Reporting pipelines.
report_id = "ID_LABEL_" + str(refined_id)
print(f"Report Label: {report_id}")

# =================================================================
# 3. COLLECTION MUTATION (The Memory Logic)
# =================================================================
# list(): Converting an immutable Tuple into a mutable List.
# Essential for updating "Short-Term Memory" in LangGraph agents.
mutable_inventory = list(raw_inventory)
mutable_inventory.append("Gloves") # We can now add data
print(f"Updated Memory: {mutable_inventory}")

# =================================================================
# 4. TRUTH VALIDATION (The Decision Gate)
# =================================================================
# bool(): Converting integers or strings into True/False.
# In many legacy systems, 1 = True and 0 = False.
is_active = bool(raw_status)
print(f"System Active Status: {is_active}")

# =================================================================
# 5. DATA PACKAGING (The Supabase Payload)
# =================================================================
# dict(): Creating a structured payload from refined variables.
supabase_payload = dict(
    record_id=refined_id,
    unit_price=refined_price,
    inventory=mutable_inventory,
    active=is_active
)

print("\n--- [REFINERY OUTPUT] ---")
print(supabase_payload)
print("--- STATUS: DATA READY FOR SOVEREIGN VAULT ---")