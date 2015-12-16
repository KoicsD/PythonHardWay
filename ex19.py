from sys import argv

# defining function that prints text to the screen
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print("You have %d cheeses!" % cheese_count)
    print("You have %d boxes of crackers!" % boxes_of_crackers)
    print("Man that's enough for a party!")
    print("Get a blanket!\n")


# my function
def my_fun(arg1, arg2):
    print("arg1: %s, arg2: %s" % (arg1, arg2))
    print("arg1 + arg2: %s\n" % (arg1 + arg2))

# my function with args
def my_fun_with_args(*args):
    print(type(*args))
    arg1, arg2 = args
    print("arg1: %s, arg2: %s" % (arg1, arg2))
    print("arg1 + arg2: %s\n" % (arg1 + arg2))


print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)


print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)


print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)


print("Now let's call my own function with 5 and 6:")
my_fun(5, 6)

print("Now let's store 5 and 6 in a variable and use them:")
my_var1 = "My name is "
my_var2 = "Daniel"
my_fun(my_var1, my_var2)

print("Now let's use the '*args' version of my function:")
my_fun_with_args(my_var1, my_var2)

print("Have you given exactly 2 command line arguments after the name of this script?")
if len(argv) != 3:
    print("No, you haven't.")
else:
    print("Yes, you have. Well, let's use the value of them for my_var1 and my_var2:")
    script_name, my_var1, my_var2 = argv
    my_fun_with_args(my_var1, my_var2)
    
    print("What if we gave these arguments to our function as a list with *?")
    my_fun_with_args(*[my_var1, my_var2])
    
    print("Well, we don't need to unpack the argv list to do this:")
    my_fun_with_args(*argv[1:])
