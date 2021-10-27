def calculateBMI(height, mass):
    return (mass / height ** 2)

def checkRanges(bmi):
    UNDERWEIGHT = 18
    OVERWEIGHT = 25
    if bmi < UNDERWEIGHT:
        print("It indicates you are underweight")
    elif bmi > OVERWEIGHT:
        print("It indicates you are overweight")
    else:
        print("It indicates you are within normal bounds")

def calculateAverage(bmis_total, bmis_taken):
    return float(bmis_total) / bmis_taken

def main():
    # Make sure these variables are initialised with default values
    loop = False
    bmis_taken = 0
    bmis_total = 0.0

    # Main event loop
    while loop == False:
        # Get user height and mass
        height = float(input("Your height (m): "))
        mass = float(input("Your weight (kg): "))

        # Calculate, print and check BMI
        bmi = calculateBMI(height, mass)
        print("Your BMI is", str(round(bmi, 2)))
        checkRanges(bmi)

        # Add BMI to the total and increment taken count
        bmis_total += bmi
        bmis_taken += 1

        # Check if user wants to input another BMI or stop
        again = (input("Another BMI? y/n: ")).lower()
        if again == 'n':
            # Stop the loop
            loop = True

    # Print the result
    print("There were", bmis_taken, "BMI values generated, of an average of", str(round(calculateAverage(bmis_total, bmis_taken), 2)))

main()