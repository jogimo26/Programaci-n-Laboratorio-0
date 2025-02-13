# Este código fue generado por la IA generativa microsoft copilot

# Function to compute maximum heart rate
def maxHR(age):
    return 208 - 0.7 * age

# Function to determine training zone
def training_zone(hr, max_hr):
    if hr < 0.5 * max_hr:
        return "Below Z1"
    elif hr < 0.6 * max_hr:
        return "Z1 (Zona de recuperación)"
    elif hr < 0.7 * max_hr:
        return "Z2 (Zona de quema de grasa)"
    elif hr < 0.8 * max_hr:
        return "Z3 (Zona aeróbica)"
    elif hr < 0.9 * max_hr:
        return "Z4 (Zona de umbral anaeróbico)"
    else:
        return "Z5 (Zona de esfuerzo máximo)"

# Ask user for age
age = int(input('Enter your age: '))

# Compute maximum heart rate
max_heart_rate = maxHR(age)
print(f'Your max heart rate is {max_heart_rate} bpm')

# Ask user for number of trainings
num_trainings = int(input('Enter the number of trainings: '))

# Initialize a dictionary to count zones
zone_counts = {
    "Z1": 0,
    "Z2": 0,
    "Z3": 0,
    "Z4": 0,
    "Z5": 0,
}

# Loop through each training to get heart rate and calculate zone
for i in range(num_trainings):
    hr = int(input(f'Enter your average heart rate for training {i+1}: '))
    zone = training_zone(hr, max_heart_rate)
    print(f'Training {i+1} was in {zone}')
    if "Z1" in zone:
        zone_counts["Z1"] += 1
    elif "Z2" in zone:
        zone_counts["Z2"] += 1
    elif "Z3" in zone:
        zone_counts["Z3"] += 1
    elif "Z4" in zone:
        zone_counts["Z4"] += 1
    elif "Z5" in zone:
        zone_counts["Z5"] += 1

# Calculate and print percentage of trainings in each zone
print("\nPercentage of trainings in each zone:")
for zone, count in zone_counts.items():
    percentage = (count / num_trainings) * 100
    print(f'{zone}: {percentage:.2f}%')