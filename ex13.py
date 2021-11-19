#import argv from the sys module
from sys import argv
#create 4 variables for argv
#script title, and 3 additional arguments to be run when executing the script
script, first, second, third = argv

#ask for two additional inputs, first a string, then an integer
fourth = input("gimme that fourth one ")
fifth = int(input("how long do it be? "))

#print argv values (repr = representation)
print(">>>> argv", repr(argv))

#print it all out
print("The Script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)
print(f"input is {fourth} and it be {fifth} long")