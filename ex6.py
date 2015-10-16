# defing the 1st part of joke as a str:
x = "THere are %d types of people." % 10  # int into str
# defing 2 substrs for 2nd part:
binary = "binary"
do_not = "don't"
# composing 2nd part:
y = "Those, who know %s and those who %s." % (binary, do_not)  # str into str

# printing the joke:
print(x)
print(y)

# repeating ourselves by putting str inside str:
print("I said: %r" % x)  # str into str
print("I also said: '%s'." % y)  # str into str

# defing a var indicating if the joke was successfull
hilarious = False
# composing a str for printing it:
joke_evaluation = "Isn't that joke so funny?! %r"  # str waiting for sg into it

# printing if joke was successful:
print(joke_evaluation % hilarious)  # bool into str waiting for sg

# creating a str for lhs os print-statement:
w = "THis is the left side of..."
# creating a rhs for it:
e = "a string with a right side."

# printing lhs and rhs in one line:
print(w + e)  # extra: connatating 2 strings
