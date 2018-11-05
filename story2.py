#It's a start...
from getInput import *

def playMadlibs():
    friend1 = getWord("Enter a Name: ")
    numAnimals = getNumber("Enter a number: ", 2, 10)
    animals1 = getWord("Enter a pluaral animal name: ")
    adjective1 = getWord("Enter a thing:")
    verb1 = getWord("Enter a action:")
    
    
    output = ""
    output += "One morning I saw my friend, " + friend1
    output += "
