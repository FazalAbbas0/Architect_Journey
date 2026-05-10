"""
PHASE 4.1: LOGIC & BOUNDARY GATES (THE DECISION ENGINE)
Logic: Implementation of AND, OR, NOT for Autonomous Filtering.
Architect: Fazal Abbas (Silicon Level-11)
"""

# --- MOCK DATA FROM THE REFINERY ---
file_type = "pdf"
file_size_mb = 4
is_gdpr_compliant = True
has_pii_leak = False  # PII = Personally Identifiable Information

# =================================================================
# 1. THE 'AND' OPERATOR (The Strict Gate)
# =================================================================
# Logic: Returns True ONLY if BOTH conditions are True.
# Use Case: Strict validation for high-security industrial data.
is_safe_to_upload = (file_size_mb < 5) and is_gdpr_compliant

print("--- [AND OPERATOR: STRICT GATE] ---")
print(f"Is file size < 5MB AND GDPR compliant? {is_safe_to_upload}")
# Result: True (Both conditions met)

# =================================================================
# 2. THE 'OR' OPERATOR (The Flexible Gate)
# =================================================================
# Logic: Returns True if AT LEAST ONE condition is True.
# Use Case: Routing data to different storage tiers.
needs_manual_audit = (file_type == "csv") or (file_size_mb > 10)

print("\n--- [OR OPERATOR: FLEXIBLE GATE] ---")
print(f"Is it a CSV OR larger than 10MB? {needs_manual_audit}")
# Result: False (Neither is true)

# =================================================================
# 3. THE 'NOT' OPERATOR (The Inverter)
# =================================================================
# Logic: Reverses the Boolean state (True becomes False, False becomes True).
# Use Case: Blocking "leaky" data or unauthorized access.
is_clean_signal = not has_pii_leak

print("\n--- [NOT OPERATOR: THE INVERTER] ---")
print(f"No PII Leak detected? {is_clean_signal}")
# Result: True (Because has_pii_leak was False)

# =================================================================
# 4. MASTER ARCHITECT LOGIC (Complex Boundary Gate)
# =================================================================
# Combining all three to create an Agency-Grade Filter.
# Goal: Allow ingestion if (Safe size AND GDPR) AND (NOT Leaky).
final_decision = (is_safe_to_upload) and (not has_pii_leak)

if final_decision:
    print("\n--- STATUS: CLEAR FOR SOVEREIGN VAULT INGESTION ---")
else:
    print("\n--- STATUS: REJECTED. NOISE DETECTED. ---")