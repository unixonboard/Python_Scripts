# def hello_func():
#     return 'Hello Function'
#
# print(hello_func())
#
# print("Hello,", name)
# print("Hello Python")
# name = input("Your Name? ")
# import sys
#
# print(sys.version)
# print(sys.executable)

import os

if os.getenv('VIRTUAL_ENV'):
    print('Using Virtualenv')
else:
    print('Not using Virtualenv')

def sum(a,b):
    return a+b
n1=input('Enter first Number: ')
n1=int(n1)
n2=input('Enter the second Number: ')
n2=int(n2)
print('Sum is : ', sum(n1,n2))