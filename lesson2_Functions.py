#Functions -> concept of DRY (Do Not Repeat Yourself); reusability of code

from math import *
from time import *

#1. function definition:
def hello(name):
    print('Hello', name)
#2. function declaration:
hello('Luciana')

#==============================================================================
#funtion to calculate volume of a cylinder
def vol(r, h):
    # return pi*pow(r, 2)*h
    volume = pi*pow(r, 2)*h
    print('Volume of the cylinder is: ', volume)


#==============================================================================
#input()
name = input('Enter programmer\'s name: ')
print('Your name is: ', name)

#NOTE: input function value is always a string
radius = int(input('Enter cylinder radius: '))
height = int(input('Enter cylinder height: '))
vol(radius, height)
# volume = vol(radius, height)
# print('Volume of the cylinder is: ', volume)

#==============================================================================
#sleep() -> delay measured in seconds
start = time()
for i in range (5):
    print(i)
    sleep(2)
stop = time()
print('Total loop time: ', stop - start)    #stop - start -> used to find the total time taken to run a process

#displaying local time
print(asctime())    #local time
print(time())   #time in seconds
print(gmtime())     #gmt time as struct_time