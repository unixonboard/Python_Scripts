# name = input("please enter your name: ")
# age= int(input("enter your age {}".format(name)))
# if age >= 18:
#     print("you are stupid")
#
# x=5.2
# y=6
# print(type(x))

# print(" Please guess a number between 1 to 10 :" )
# num = int(input())
#
# if num <5:
#     print(" please guess higher")
#     num = int(input())
#     if num == 5:
#         print("you have guessed the correct no")
#     else:
#         print(" Sorry you have not guessed a correct num ")
# elif num >5:
#     print("please guess lower")
#     num = int(input())
#     if num == 5:
#         print("you have gussed the correct num")
#     else:
#         print("sorry you have not gussed thec orrect num")
# else:
#     print("you have gussed at the forst time")


# name = input("Please enter you name : ")
# age = int(input(" How old are you {} ? ".format(name)))
#
# if 18<= age <31:
#     print ("welcome to the youth club {} ".format(name))
# else:
#     print("sorry {} this club is explictly for youths\nplease come after {}yrs" .format(name,18-age))

# var = 1400
#
# if var < 2000:
#     print("2000")
#     if var == 1500:
#         print("1500")
#     elif var == 1000:
#         print("1000")
#     elif var == 500:
#         print("500")
#     else:
#         print("200")
# else:
#     print("cound not")
# print("good bye")


# for i in range(1,21):
#     print("i is now {}")
#
# number = "9,223,372,036,854,775,807"
# cleanedNumber = ''
#
# for char in number:
#     if char in '0123456789':
#         cleanedNumber = cleanedNumber + char

# number = "5,552,896,54"
# convert = ''
# mynumber = 0
#
# for i in range(0, len(number)):
#     if number[i] in '58':
#         convert = convert + number[i]
#         mynumber = int(number[i]) + mynumber
#         print("current vale of convert: {}, mynumber {}".format(convert,mynumber))



# import os
#
# curDir = os.getcwd()
# print (curDir)

# def solveMeFirst(a,b):
# # Hint: Type return a+b below
#
#
#     num1 = int(input())
#     num2 = int(input())
#     res = solveMeFirst(num1,num2)
#     print(res)
#
import calendar
print (calendar.calendar(1978,1,1,10))