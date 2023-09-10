# print_gallons_ounces.py
# This program converts ounces to gallons and ounces.

# Course: CSCI 130 (Introduction to Programming)
# Assignment: 9

# Author: Adam Zieman
# Date: April 29, 2021

def main():
    # total ounces in a list
    list = [1, 58, 128, 209, 256, 258, 433, 512, 555, 724]

    # Go through each list value, finding and printing gallons and ounces.
    for value in list:
        # the first 2 steps of this program calculate 2 variables
        # (that will hold gallons and ounces) to use in the rest of the program
        
        # find (integer) gallons (save in a variable - 1 ASSIGNMENT STATEMENT)
        gallons = value // 128

        # find remaining ounces (save in a variable - 1 ASSIGNMENT STATEMENT)
        ounces = value % 128

        # determine whether to print "gallon" or "gallons", if needed
        if gallons == 1:
            print(gallons, "gallon", end = "")
        elif gallons > 1:
            print(gallons, "gallons", end = "")

        # determine whether to print ","
        # (needed if there are ounces after gallons)
        if gallons > 0:
            if ounces > 0:
                print(", ", end = "")
            else:
                print("", end = "")

        # determine whether to print "ounce" or "ounces", if necessary
        if ounces == 0:
            print("", end = "")
        elif ounces == 1:
            print(ounces, "ounce ", end = "")
        elif ounces > 1:
            print(ounces, "ounces ", end = "")

        # print final phrase (the part in parentheses)
        # i.e., "zero" statements, or "under" statements
        if gallons == 0:
            print("(zero gallons)", end = "")
        elif ounces == 0:
            print(" (zero ounces)", end = "")
        else:
            print("(under", gallons + 1, "gallons)" ,end = "")

        # final print() to end the line for this value
        print()
main()
