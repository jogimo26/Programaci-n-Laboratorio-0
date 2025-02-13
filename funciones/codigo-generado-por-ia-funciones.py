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

# Function to calculate heart rate range for Z2
def Z2_heart_rate_range(max_hr):
    lower_bound = 0.6 * max_hr
    upper_bound = 0.7 * max_hr
    return lower_bound, upper_bound

# Ask user for age
age = int(input('Enter your age: '))

# Compute maximum heart rate
max_heart_rate = maxHR(age)
print(f'Your max heart rate is {max_heart_rate} bpm')

# Calculate and print Z2 heart rate range
Z2_range = Z2_heart_rate_range(max_heart_rate)
print(f'To train in Z2 (Zona de quema de grasa), maintain a heart rate between {Z2_range[0]:.2f} and {Z2_range[1]:.2f} bpm.')

# Ask user for heart rate during training
hr = int(input('Enter your heart rate during training: '))

# Determine and print training zone
zone = training_zone(hr, max_heart_rate)
print(f'You trained in {zone}')
