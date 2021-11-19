# set variables
types_of_people = 10
x = f"There are {types_of_people} types of people."

binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}"

#print x and y
print(x)
print(y)

#string x inside formatted print string:
print(f"I said: {x}") 

#string y inside formatted print string:
print(f"I also said: '{y}'")


#set up 
hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"

#evaluate the joke as = to hilarious = false
print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."

print(w + e)
