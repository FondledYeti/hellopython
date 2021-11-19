#ask for input, set age = input
age = input("How old are you?(years) ")
#ask for input, set height = input and make it an integer
height = int(input("How tall are you?(inches) "))
weight = input("How much do you weigh?(lbs) ")
#convert height in inches to feet, make it an integer to drop the trailing decimals
ft_tall = int(height / 12)
#convert height in inches to feet, take remainder with Mod and print that
in_tall = height % 12


print(f"So, you're {age} years old, {ft_tall}\'{in_tall}\" tall, and {weight} lbs.")
