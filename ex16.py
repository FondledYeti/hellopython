from sys import argv

script, filename = argv

print(f"We're goint to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")
target = open(filename, 'w')

# print("Truncating the file. Goodbye!")
# target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

# #set up format for target.write below
# formatter = "{}\n{}\n{}\n"
# #This one target.write replaces all 6 below
# target.write(formatter.format(line1, line2, line3))

#alternatively
target.write(f"{line1}\n{line2}\n{line3}")

# target.write(line1)
# target.write("\n")
# target.write(line2)
# target.write("\n")
# target.write(line3)
# target.write("\n")

print("And finally, we close it.")
target.close()

print("Now we'll read it to see what we've done.")

target = open(filename, 'r')
print(target.read())

print("And then we close it again.")
target.close()