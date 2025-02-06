# Function to compute maximum heart rate
def maxHR(age):
    MaxHR = 208-0.7*age
    return MaxHR

def trainingzones(hr,MaxHR):
    # hr = int(input("What heart rate did you achieve on your training?: "))
    if hr >= MaxHR*0.5 and hr < MaxHR*0.6:
        trainingzone = "Recovery"
    elif hr >= MaxHR*0.6 and hr < MaxHR*0.7:
        trainingzone = "Fat Burning"
    elif hr >= MaxHR*0.7 and hr < MaxHR*0.8:
        trainingzone = "Aerobic"
    elif hr >= MaxHR*0.8 and hr < MaxHR*0.9:
        trainingzone = "Anaerobic"
    elif hr >= MaxHR*0.9 and hr <= MaxHR:
        trainingzone = "Maximum Performance"
    elif hr > MaxHR or hr < MaxHR*0.5:
        trainingzone = "Invalid"
    return trainingzone

# Ask user for their age
age = int(input('Enter your age: '))

# Print estimation of maximum heart rate based on age
print(f'Your max heart rate is {maxHR(age)} bpm')

# Ask user for number of trainings
trainingno = int(input("How many training sessions did you have in total?\n"))

for i in range(1,trainingno+1,1):
    trainingzoneslist = []
    traininghr = int(input(f"What was the heart rate achieved during the #{i} training session?: "))
    print(f"The training zone achieved during training #{i} was {trainingzones(traininghr,maxHR(age))}")
    trainingzoneslist.append(trainingzones(traininghr,maxHR(age)))
    traininghr = 0

# Give the training zone the training was done in to the user
# print(f'Your training was done in the {trainingzones(age,MaxHR(age))} training zone')