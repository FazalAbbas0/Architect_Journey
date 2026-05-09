import time

print("----System Start: Weather monitoring agent activated....")   
# Step 1: Decision Diamond 1
is_raining = input("Is it raining right now? (yes/no): ").Lower()
if is_raining == "no":
    # Follow the 'No' path straight to the goal
    print("Action: Go outside.")
else:
    # Follow the 'Yes' path to the next Diamond
    have_umbrella = input("Do you have an umbrella? (yes/no): ").Lower()
    if have_umbrella == "yes":
        # Follow 'Yes' path to Go Outside
        print("Action: Go outside.")
    else:
        # Follow 'No' path to the Loop (Wait a while)
        print("Action: No umbrella found. Waiting...")
        
        # This represents the Loop in the flowchart
        still_raining = "yes"
        while still_raining == "yes":
            time.sleep(2)  # Wait for 2 seconds (simulate time passing)
            print("Checking weather again...")
            still_raining = input("Is it still raining? (yes/no): ").Lower()
            if still_raining == "no":
                print("Action: Finally! The rain stopped. Go outside.")
            else:
                print("Action: Still raining. Waiting more...")
print("--- System End: Mission Accomplished ---")
