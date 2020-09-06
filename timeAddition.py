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
    #TODO what if it's not a list?

def getTimesByList():
    inp = "0:00"
    allInputs = []
    while len(inp) == len("0:00") and inp[1] == ":":
        allInputs.append(inp)
        inp = input("Enter a time in H:MM format, or anything else to submit.\n")
    return timeAddition(allInputs)

print("Your total time is " + str(getTimesByList()))