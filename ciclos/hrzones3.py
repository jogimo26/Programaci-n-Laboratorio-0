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

# Initialize a list for the training zones
trainingzoneslist = []
# zonescounterlist = []

# Ask user for their age
age = int(input('Enter your age: '))

# Print estimation of maximum heart rate based on age
print(f'Your max heart rate is {maxHR(age)} bpm')

# Ask user for number of trainings
trainingno = int(input("How many training sessions did you have in total?\n"))

for i in range(1,trainingno+1,1):
    traininghr = int(input(f"What was the heart rate achieved during the #{i} training session?: "))
    print(f"The training zone achieved during training #{i} was {trainingzones(traininghr,maxHR(age))}")
    trainingzoneslist.append(trainingzones(traininghr,maxHR(age)))
    traininghr = 0

# Counters for the amount of times a certain training zone appears inside the list
amountrecovery = trainingzoneslist.count("Recovery")
amountfatburning = trainingzoneslist.count("Fat Burning")
amountaerobic = trainingzoneslist.count("Aerobic")
amountanaerobic = trainingzoneslist.count("Anaerobic")
amountmaximumper = trainingzoneslist.count("Maximum Performance")
amountinvalid = trainingzoneslist.count("Invalid")

# For the % of times that a certain zone appears inside the list
sumsessions = amountrecovery + amountfatburning + amountaerobic + amountanaerobic + amountmaximumper

# cantidad del dato / total de la lista * 100%

if amountrecovery == 0:
    recoverypercentage = 0
elif amountrecovery != 0 :
    recoverypercentage = amountrecovery/sumsessions * 100

if amountfatburning == 0:
    fatburningpercentage = 0
elif amountfatburning != 0:
    fatburningpercentage =  amountfatburning/sumsessions * 100
 
if amountaerobic == 0:
    aerobicpercentage = 0
elif amountaerobic != 0:
    aerobicpercentage = amountaerobic/sumsessions * 100

if amountanaerobic == 0:
    anaerobicpercentage = 0
elif amountanaerobic != 0:
    anaerobicpercentage = amountanaerobic/sumsessions * 100

if amountmaximumper == 0:
    maximumpercentage = 0
elif amountmaximumper != 0:
    maximumpercentage = amountmaximumper/sumsessions * 100

if amountinvalid == 0:
    invalidpercentage = 0
elif amountinvalid != 0:
    invalidpercentage = amountinvalid/sumsessions * 100

# Display the results to the user
print(f"\nOn a percentual basis your trainings were on these zones:\nRecovery Zone: {recoverypercentage}%\nFat Burning Zone: {fatburningpercentage}%\nAerobic Zone: {aerobicpercentage}%\nAnaerobic Zone: {anaerobicpercentage}%\nMaximum Performance Zone: {maximumpercentage}%\nInvalid Inputs: {invalidpercentage}")

# Give the training zone the training was done in to the user
# print(f'Your training was done in the {trainingzones(age,MaxHR(age))} training zone')
