"""
Programmer: Trenton Weller
Date: 10.15.19
Program: This program will nest a for loop inside of another for loop
"""



for i in range(3):
    print("Outer for loop:  " + str(i))
    for l in range(2):
        print("         innner for loop:  " +str(l))



"""
Programmer: Trenton Weller
Date: 10.22.19
Program: Average Test Scores

This program asks for the test score for multiple peeople and 
reports the average test score for each portion

"""




num_people = int(input("How many people are taking the test?: "))
testperperson = int(input("How many tests are going to be averaged?: "))

for i in range(num_people):
    name = input("Enter Name:  ")
    sum = 0
    for j in range(testperperson):
        score = int(input("Enter a score:     "))
        sum = sum + score
    average = float(sum) / testperperson
    print("     Average for " + name + ":  " + str(round(average,  2)))

print("\n****************\n")
"""
Programmer: Trenton
Date: 10.23.19
Program: This program will ask users of an interest to them
theen ask for two items related to that interest

"""

