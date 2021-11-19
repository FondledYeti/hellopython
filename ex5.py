name = 'Oliver C. Reams'
age = 29 # not a lie
height_inches = 70 #inches
height_cm = round(height_inches / 2.54)
weight_lbs = 210 # lbs
weight_kgs = round(weight_lbs / 2.2)
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'


print(f"Let's talk about {name}.")
print(f"He's {height_inches} inches tall.")
print(f"That's {height_cm} centimeters")
print(f"He's {weight_lbs} pounds heavy.")
print(f"Also known as {weight_kgs} kilos.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the tea.")

total = age + height_inches + weight_lbs

print(f"If I add {age}, {height_inches}, and {weight_lbs} I get {total}.")