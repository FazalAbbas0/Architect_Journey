"""
PHASE 4.2.2: THE SPECIALIZED MACHINERY (FUNCTIONS)
Logic: Modular, Reusable Code Blocks for Industrial AI.
Architect: Fazal Abbas (Silicon Level-11)
"""

# =================================================================
# MACHINE 1: THE DATA CLEANER (Basic Function)
# Logic: Strips whitespace and forces lowercase for standardization.
# =================================================================
def clean_signal(raw_text):
    """Refines a single string into a Steel-Standard signal."""
    return raw_text.strip().lower()

# =================================================================
# MACHINE 2: THE INVENTORY AUDITOR (Positional & Keyword Arguments)
# Logic: Checks if an item exists and applies a 'Confidence Score'.
# =================================================================
def audit_item(item_name, min_confidence=0.85):
    """
    Simulates a check against the Sovereign Vault.
    Default confidence is 85%—the standard for Industrial RAG.
    """
    status = "VERIFIED" if len(item_name) > 3 else "REJECTED"
    return f"Item: {item_name} | Status: {status} | Confidence: {min_confidence}"

# =================================================================
# MACHINE 3: THE BATCH PROCESSOR (The Master Engine)
# Logic: A function that calls other functions (Composition).
# =================================================================
def run_refinery_v1(data_list, client="EU_Logistics_SME"):
    """
    The main engine you will white-label for Irfan.
    This manages the entire flow from raw data to structured payload.
    """
    refined_vault = []
    
    for entry in data_list:
        # Step 1: Use Machine 1
        clean_entry = clean_signal(entry)
        
        # Step 2: Logic Gate
        if clean_entry != "error":
            refined_vault.append(clean_entry)
            
    # Final Output Construction
    return {
        "client_id": client.upper(),
        "processed_total": len(refined_vault),
        "payload": refined_vault,
        "engine_version": "Silicon-L11-v4.2"
    }

# =================================================================
# THE 18:00 AUDIT HOUR EXECUTION
# =================================================================
raw_data = ["  MASK  ", "GLOVES", "error", "  SYRINGE  "]

print("--- [INITIATING SPECIALIZED MACHINERY] ---")

# Calling the Master Engine
final_result = run_refinery_v1(raw_data, client="Berlin_Medical_Stores")

# Displaying the Structured Payload
print(f"Target Firm: {final_result['client_id']}")
print(f"Refined Data: {final_result['payload']}")
print(f"Status: {final_result['engine_version']} SECURED")

# Testing Individual Machine 2
print("\n--- [INDIVIDUAL COMPONENT CHECK] ---")
print(audit_item("Mask", min_confidence=0.99))