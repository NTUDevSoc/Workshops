loop = False
bmis_taken = 0
bmis_total = 0.0
bmi_average = 0.0
while loop == False:
    height = float(input("Your height (m): "))
    if height <= 0:
        print("Please reinput your height")
    else:
        mass = float(input("Your weight (kg): "))
        if mass <= 0:
            print("Please reinput your height")
        else:
            bmi = (mass / height ** 2)
            bmis_total += bmi
            print("Your BMI is", str(round(bmi, 2)))
            if bmi < 18:
                print("It indicates you are underweight")
            elif bmi > 25:
                print("It indicates you are overweight")
            else:
                print("It indicates you are within normal bounds")

            bmis_taken += 1

            again = (input("Another BMI? y/n: ")).lower()
            if again == 'n':
                loop = True

bmi_average = float(bmis_total) / bmis_taken
print("There were", bmis_taken, "BMI values generated, of an average of", str(round(bmi_average, 2)))