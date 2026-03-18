readings = list(map(int, input("Enter energy readings: ").split()))

categories = {
    "efficient": [],
    "moderate": [],
    "high": [],
    "invalid": []
}

for e in readings:
    if e < 0:
        categories["invalid"].append(e)
    elif e <= 50:
        categories["efficient"].append(e)
    elif e <= 150:
        categories["moderate"].append(e)
    else:
        categories["high"].append(e)

valid_readings = [x for x in readings if x >= 0]

total_consumption = sum(valid_readings)
num_buildings = len(readings)

overconsumption = len(categories["high"]) > 3
balanced = abs(len(categories["efficient"]) - len(categories["moderate"])) <= 1
energy_waste = total_consumption > 600

summary = (total_consumption, num_buildings)

if energy_waste:
    result = "Energy Waste Detected"
elif overconsumption:
    result = "Moderate Usage"
elif balanced:
    result = "Efficient Campus"
else:
    result = "Moderate Usage"

print("\n--- Report ---")
print("Categories:", categories)
print("Total Consumption:", summary[0])
print("Buildings:", summary[1])
print("Result:", result)