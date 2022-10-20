# Import the "random" package from python, so we can get random numbers later
import random

# Create a Person class, so we can create multiple people and make it easier to improve later
class Person:
    def __init__(self, hair, eyes, gender, glasses, hat):
        self.hairColor = hair
        self.eyeColor = eyes
        self.gender = gender
        self.glasses = glasses
        self.hat = hat

# Define a set of options for each attribute a person has, so we can pick them randomly when we generate a person        
hairTypes = ["Black", "Blonde", "Brown"]
eyeTypes = ["Brown", "Blue", "Green"]
genderTypes = ["Male", "Female"]
glassesTypes = ["None", "Red", "Blue"]
hatTypes = ["None", "Green", "Yellow"]
     
# Make a new person object, using randrange to pick a random attribute
# from the lists above for each attribute of our random person
''' 
    How randrange works:
    randrange(0, 3)
    Start at 0, pick a random number less than 3
    Possible options are - 0, 1, 2
'''
randomPerson = Person(
    hairTypes[random.randrange(0, 3)],
    eyeTypes[random.randrange(0, 3)],
    genderTypes[random.randrange(0, 2)],
    glassesTypes[random.randrange(0, 2)],
    hatTypes[random.randrange(0, 2)],
    )

# Takes a person as an input and prints each of their attributes to the console
def PrintPerson(person):
    print(person.hairColor, person.eyeColor, person.gender,
          person.glasses, person.hat)
    
def getInput():
    print("Guess the person:")
    tally = 0

    '''
        For each attribute of our random person, we ask the player to guess what the attribute is
        E.g. guess whether their eyes are blue, or whether their hair is brown
        If the guess is correct, print that they got it right and increment a tally.
        If it's incorrect, print they got it wrong

        At the end of the function check the tally, and if the tally is 5
        (Meaning they got every guess right) then print that the player won
        if they didn't get every tally then print that they lost
    '''

    guess = input("Guess the hair color: ")
    if guess == randomPerson.hairColor:
        print("Correct!")
        tally += 1
    else:
        print("Incorrect")
        
    guess = input("Guess the eye color: ")
    if guess == randomPerson.eyeColor:
        print("Correct!")
        tally += 1
    else:
        print("Incorrect")
    
    guess = input("Guess the gender: ")
    if guess == randomPerson.gender:
        print("Correct!")
        tally += 1
    else:
        print("Incorrect")
        
    guess = input("Guess the glasses color: ")
    if guess == randomPerson.glasses:
        print("Correct!")
        tally += 1
    else:
        print("Incorrect")
            
    guess = input("Guess the hat color: ")
    if guess == randomPerson.hat:
        print("Correct!")
        tally += 1
    else:
        print("Incorrect")
        
    if tally == 5:
        print("Congratulations, you win!")
    else:
        print("Sorry, you lose.")
        
        
# Run our functions we made otherwise our python app won't have any output
PrintPerson(randomPerson)
getInput()

# Used to test printing different attributes of objects instantiated from the same class
'''
person1 = Person("Brown", "Green")
person2 = Person("Blonde", "Brown")
person3 = Person("Ginger", "Blue")

print(person1.hairColor, person1.eyeColor)
print(person2.hairColor, person2.eyeColor)
print(person3.hairColor, person3.eyeColor)
'''