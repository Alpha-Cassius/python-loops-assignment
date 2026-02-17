# Name: Vaibhav Pandey
# Roll Number: IITP_AIML_2602282
# Assignment: Python Loops & Automation - Subjective Question

print("===== Task 1: Find Maximum and Minimum =====")
temperatures = [28, 32, 35, 29, 31, 27, 30]

# Initialize highest and lowest 
highest_temp = temperatures[0]
lowest_temp = temperatures[0]

for temp in temperatures:
    # Check for new highest
    if temp > highest_temp:
        highest_temp = temp
    # Check for new lowest
    if temp < lowest_temp:
        lowest_temp = temp

print(f"Highest Temperature: {highest_temp}°C")
print(f"Lowest Temperature: {lowest_temp}°C")


print("\n===== Task 2: Count Hot Days =====")
temperatures = [28, 32, 35, 29, 31, 27, 30]

hot_days_count = 0

for temp in temperatures:
    # Skip days that are not hot (<= 30)
    if temp <= 30:
        continue
    
    # Increment counter for hot days
    hot_days_count += 1

print(f"Hot Days (>30°C): {hot_days_count}")


print("\n===== Task 3: Alert System =====")
temperatures = [28, 32, 35, 40, 31, 33, 30]

hot_days_before_alert = 0
day_counter = 1

for temp in temperatures:
    # Check for extreme temperature first
    if temp >= 40:
        print(f"Hot Days before alert: {hot_days_before_alert}")
        print(f"Alert! Extreme temperature {temp}°C detected on Day {day_counter}")
        break
    
    # Count hot days (> 30)
    if temp > 30:
        hot_days_before_alert += 1
    
    # Increment day counter for the next iteration
    day_counter += 1
