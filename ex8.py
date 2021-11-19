
#define the format
formatter = "{} {} {} {}"

#use the formatter to organize arguments in formatter.format
print(formatter.format(1,2,3,4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "Roses are red",
    "Violets are blue",
    "You smell like poo",
    "wow you really don't smell good"
))