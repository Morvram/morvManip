import time
import csv

#Takes a set of times in the format of H:MM, and adds them together.

def timeAddList(times):
    #Assumes input is in list form, as a list of strings, with format H:MM
    totalHours = 0
    for item in times:
        x = int(item[0])
        totalHours += x
        y = int(item[2:4])
        totalHours += y / 60
    return totalHours #as int
    

def timeAddition(times):
    if type(times) == type([]):
        #We're dealing with list input.
        return timeAddList(times)
    if type(times) == type(""):
        #If it's a string input, try comma separated or space separated.
        if ", " in times:
            return timeAddList(times.split(", "))
        else if "," in times:
            return timeAddList(times.split(","))
        else if " " in times:
            return timeAddList(times.split(" "))
        else:
            x = times[4]
            return timeAddList(times.split(x))
            #I'm not sure if this will work correctly, because theoretically you could have a construct like "3:00 | 4:00". But how do I address that.


def getTimesByList():
    inp = "0:00"
    allInputs = []
    while len(inp) == len("0:00"):
        allInputs.append(inp)
        inp = input("Enter a time in H:MM format, or hit enter to submit.\n")
    return timeAddition(allInputs)

print("Your total time is " + str(getTimesByList()))
input("Press enter to end the program.")