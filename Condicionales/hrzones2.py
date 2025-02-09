# Function to compute maximum heart rate
def maxhr(age):
    maxhr = 208-0.7*age
    return maxhr

def trainingzones(age,maxhr):
    hr = int(input("What heart rate did you achieve on your training?\n"))
    if hr >= maxhr*0.5 and hr < maxhr*0.6:
        trainingzone = "Recovery"
    elif hr >= maxhr*0.6 and hr < maxhr*0.7:
        trainingzone = "Fat Burning"
    elif hr >= maxhr*0.7 and hr < maxhr*0.8:
        trainingzone = "Aerobic"
    elif hr >= maxhr*0.8 and hr < maxhr*0.9:
        trainingzone = "Anaerobic"
    elif hr >= maxhr*0.9 and hr <= maxhr:
        trainingzone = "Maximum Performance"
    elif hr > maxhr:
        trainingzone = "Invalid"
    return trainingzone

# Ask user for age
age = int(input('Enter your age: '))

# Print estimation of maximum heart rate based on age
print(f'Your max heart rate is {maxhr(age)} bpm')

# Give the training zone the training was done in to the user
print(f'Your training was done in the {trainingzones(age,maxhr(age))} training zone')
