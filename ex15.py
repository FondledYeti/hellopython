#import argv from system module
from sys import argv

#name the arguments given when running the script
script, filename = argv

#set txt variable to open the file called when running the script
txt = open(filename)

#print message, then read the contents of the file and print them
print(f"Here's your file {filename}:")
print(txt.read())

#prompt for the file name again and show a '>' as prompt, set input as new variable 'file_again'
print("Type the filename again:")
file_again = input("> ")

#set new variable to open the file as read in the previous line
txt_again = open(file_again)

#print the variable that was set before, print the document specified in input.
print(txt_again.read())