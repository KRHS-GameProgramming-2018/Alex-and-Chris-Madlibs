from getInput import *

def playMadlibs():
    friend1 = getWord("Enter a Name: ")
    numAnimals = getNumber("Enter a number: ", 2, 10)
    animals1 = getWord("Enter a pluaral animal name: ")
    adjective1 = getWord("Enter a thing:")
    verb1 = getWord("Enter a action:")
    
    output = ""
    output += "One day I was walking with my friend, " + friend1
    output += "And I saw a huge " + adjective1
    output += "I started to run away but it " + verb1
    output += "after it was done it started to" + verb1
    output += "the" + adjective1
    
    
    
    return output
