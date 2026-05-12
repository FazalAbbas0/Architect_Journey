"""
SOVEREIGN DEFINITION: PYTHON FUNCTIONS
Logic: Encapsulating industrial operations for high-speed reuse.
Architect: Fazal Abbas (Clerk_Agentic_AI_Engineer)
Location: loop.py/python_functions.py
"""

# =================================================================
# 1. THE BASIC COMMAND (No Parameters, No Return)
# =================================================================
# Logic: A simple trigger for repetitive tasks like printing headers.

def initiate_audit_banner():
    print("=" * 65)
    print("      PHARMACY WAREHOUSE AUDIT SYSTEM — v2.0.0")
    print("=" * 65)


# =================================================================
# 2. THE PARAMETERIZED TOOL (Input required)
# =================================================================
# Logic: Takes data (arguments) and performs a specific action.

def scan_rack(rack_id):
    print(f" ► [SCANNING] Currently auditing Rack: {rack_id}")


# =================================================================
# 3. THE CALCULATION ENGINE (Returns a Value)
# =================================================================
# Logic: Processes data and gives back a result. 
# This is how you will calculate the 20% Adaptive Variance.

def calculate_variance(prev_usage, current_retain):
    variance = abs(prev_usage - current_retain) / current_retain * 100
    return variance


# =================================================================
# 4. THE DEFAULT PARAMETER GATE (Optional Input)
# =================================================================
# Logic: Sets a default value unless you specifically change it.

def check_expiry(days_left, threshold=300):
    if days_left < threshold:
        return "⚠ ALERT: NEAR EXPIRY"
    return "SECURE ✓"


# =================================================================
# EXECUTION: PUTTING THE VAULTS TO WORK
# =================================================================

initiate_audit_banner()

# Scanning a specific rack
scan_rack("R-A1-S1")

# Calculating variance for Morphine (usage: 2500, retain: 2000)
morphine_var = calculate_variance(2500, 2000)
print(f"Morphine Variance: {morphine_var}%")

# Checking expiry with a default 300-day threshold
print(f"Status: {check_expiry(150)}")

# Checking expiry with a custom 90-day threshold (Purchase Return)
print(f"Status: {check_expiry(80, 90)}")