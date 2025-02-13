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

# Ask user for heart rate during training
hr = int(input('Enter your heart rate during training: '))

# Determine and print training zone
zone = training_zone(hr, max_heart_rate)
print(f'You trained in {zone}')
