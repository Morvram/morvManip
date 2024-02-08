# All the functions placed into one file so that they can be imported more easily.



import re

def number_updowngrade (instr, upby):
    #a script that takes a string, identifies numbers within it, and increases or reduces each number by a specified amount
    #INPUT: instr = String in which the numbers will be downgraded. upby = Integer by which to change the numbers.
    #OUTPUT: New string with all the numbers altered by upby.

    #Create list of integers
    res = [int(i) for i in instr.split() if i.isdigit()]

    #Alter each number in the list
    res_old = res.copy()
    for i in range(0, len(res)):
        res[i] = res[i] + upby

    #replace the numbers in the string
    res_old = list(set(res_old))
    res = list(set(res))
    for i in range(0, len(res)):
        instr = instr.replace(str(res_old[i]), str(res[i]))

    return instr

#TODO timeAddition.py