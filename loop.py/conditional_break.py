"""
PHASE 4.2.8: THE CONDITIONAL BREAK (THE FAIL-SAFE)
Logic: High-security flow control for the 'Enterprise Brain' refinery.
Architect: Fazal Abbas (Silicon Level-11)
"""

# --- MOCK INDUSTRIAL DATA STREAM ---
# A mix of clean signals, noise, and a critical threat.
data_stream = ["Signal_01", "Noise_Alpha", "Signal_02", "CRITICAL_THREAT", "Signal_03"]

# =================================================================
# STRATEGY 1: THE NOISE FILTER (continue)
# Use Case: Skipping minor errors without stopping the whole engine.
# =================================================================
print("--- [STRATEGY 1: NOISE FILTRATION] ---")
refined_vault = []

for signal in data_stream:
    if "Noise" in signal:
        print(f"[-] Filtered: {signal} (Continuing scan...)")
        continue # Immediately jumps to the next iteration
    
    refined_vault.append(signal)
    print(f"[+] Refined: {signal}")


# =================================================================
# STRATEGY 2: THE EMERGENCY SHUTDOWN (break)
# Use Case: Instantly killing the process when a threat is found.
# =================================================================
print("\n--- [STRATEGY 2: THREAT RESPONSE] ---")

for signal in data_stream:
    if "THREAT" in signal:
        print(f"[!!!] ALERT: {signal} DETECTED!")
        print("SHUTTING DOWN SOVEREIGN PIPELINE TO PROTECT CLIENT DATA...")
        break # Immediately exits the entire loop
    
    print(f"Scanning: {signal} [Safe]")


# =================================================================
# STRATEGY 3: THE SEARCH OPTIMIZER (Find & Exit)
# Use Case: Saving compute costs by stopping once the target is found.
# =================================================================
print("\n--- [STRATEGY 3: COMPUTE OPTIMIZATION] ---")
target_file = "Signal_02"

for i, signal in enumerate(data_stream):
    if signal == target_file:
        print(f"MATCH FOUND: '{target_file}' located at Position {i}.")
        print("Stopping search to save tokens/compute.")
        break


# =================================================================
# STRATEGY 4: THE 'ELSE' COMPLETION GUARD
# Use Case: Confirming a scan finished WITHOUT any 'break' triggers.
# =================================================================
print("\n--- [STRATEGY 4: INTEGRITY VERIFICATION] ---")
clean_batch = ["Part_01", "Part_02", "Part_03"]

for part in clean_batch:
    print(f"Verifying: {part}")
else:
    # This block ONLY runs if the loop finished naturally (no 'break')
    print("SUCCESS: Full batch verified. No threats or interruptions.")

print("\n--- STATUS: FAIL-SAFE PROTOCOLS ARMED ---")