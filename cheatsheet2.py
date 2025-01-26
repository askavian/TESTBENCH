age = 77 # If below 18 Script ENDS here
if age <= 18:
    raise SystemExit('You must be older than 18!') # raise SystemExit shuts down code when condition is met


print("Hello world!") # SINGLE VALUE
print("Please", "say", "hello", "back!") # MULTIPLE VALUES
print("I am here to learn!") # SINGLE VALUE


my_number = 5 # DECLARING VARIABLES
print(my_number)

num = 42
print(num)


temporary_password = True # Declaring Boolean
print(temporary_password)


def print_message(): # DEF for DECLARING FUNCTIONS
    print("Hello World!") # NOT printed directly to console, because it is part of a Function
print_message()


###REUSABLE FUNCTIONS###
""""
Function syntax example:

The multiplication() function is defined here, the paramaters
passed to it are named num1 and num2. And it returns the value
of the two numbers multiplied.
"""
def multiplication(num1, num2):
    return num1 * num2 
    # code inside a python function is indented by four spaces


""""
here the multiplication() function is called and passed the value of 
2 for num1 and the value of 3 for num2. So the multiplication function
will multiply 2 * 3 and return the value, which is stored in the
result1 variable. 
"""
result1 = multiplication(2, 3)
print(result1)

""""
here the multiplication() function is called and passed the value of 
4 for num1 and the value of 9 for num2. So the multiplication function
will multiply 4 * 9 and return the value, which is stored in the
result2 variable. 
"""
result2 = multiplication(4, 9)
print(result2)

""""
here the multiplication() function is called and passed the value of 
34 for num1 and the value of 99 for num2. So the multiplication function
will multiply 34 * 99 and return the value, which is stored in the
result3 variable. 
"""
result3 = multiplication(34, 99)
print(result3)

"""
Try changing the values passed to the multiplication function to
see the how the value returned from it changes.
"""


# DETERMINING DATA TYPE
print(type("Hello, World!")) # str
print(type(42)) # int
print(type(3.145)) # float
print(type(1j)) # complex
print(type(["egg", "bacon", "spam"])) # list
print(type(("egg", "bacon", "spam"))) # tuple
print(type(range(6))) # range
print(type({"name" : "John", "age" : 80})) # dict
print(type({"egg", "bacon", "spam"})) # set
print(type(True)) # bool
print(isinstance(3.14, int)) # CHECKS WHAT THE TYPE OF A DATAPOINT IS

# USE
itm_one = 10
itm_two = 21.56
itm_three = 'A string of text'
itm_four = True

print(type(10))
print(type(21.56))
print(type('A string of text'))
print(type(True))


# INTERGER vs. FLOAT
num1 = 10 # Integer INT are allways full numbers (incl.0)
num2 = 10.00 # FLOATS are allways numbers with decimals
print(type(num1))
print(type(num2))



# NONE

a = 1
a = None
print(a)
def donothing():
    b = 0
print(donothing())


# COMMON PRACTISE TO DECLARE VALUE WHEN NEEDED IN CODE
age = None
total = None
print(age)
print(total)
age = 20
print(age)
print(total)


# ' OR " QUOTES 
print('Then Mike said "What is that?"') # use different quotes
print("It's a beautiful day")


# INPUT VALUES AND CONVERTIG DATA TYPES
first_number = input("Input your first number:") # by default takes Input ONLY as a string
second_number = input("Input your second number:")
print(first_number + second_number)
first_number = int(input("Input your first number:")) # Converts input to an INTEGER
second_number = int(input("Input your second number:"))
print(first_number + second_number)


my_number = str(5)
my_string = "5"
print(my_string + my_number)


result = 40 + float("2.2")
print(result)
result_two = "The answer to the ultimate question is " + str(42)
print(result_two)



# VARIABLE REASSIGNMENT
my_number = 5
my_number = 10 # Second Var overwrites the first one
print(my_number)



# BASIC MATH
print(2 + 2)
print(4 - 2)
print(2 * 3)
print(9 / 3)
print(2 ** 3)
print(18 % 7)
print(10900 % 60)

num = 5
total = 10 + 20 + num
print(total)

product = 72
total_cost = product + product * 0.21
print(total_cost)



# INCREMENTING & DECREMENTING
variable_one = "hello "
variable_two = "world"
variable_one += variable_two
print(variable_one)
print(variable_two)

x = 2
x *= 3
print(x)

num = 100
print(num)
num //= 50 #  floor assignment operator //=
print(num)

num_b = 100
print(num_b)
num_b %= 3 # MODULO %=
print(num_b)



# STRING FORMATTING F Formatting
name = input("What's your name? ")
# Here we don't need age to be a number as we are not
# going to do any calculations with it so we don't need to wrap the
# input() in the str() method
age = input("What's your age: ")
# The Modern way of formatting a string
print(f"Hello {name}, you are {age} years old")


my_str = "Hello " + "World"
print(my_str)

str_one = "One"
str_two = "Two"
result = str_one + str_two
print(result)

result_one = "John" + str(42)
print(result_one)

num = 33
my_string = f'This is number {num}' # F Method
print(my_string)


name = "Igor"
age = 35
concat_string = name + " is " + str(age) # string concatenation
print(concat_string)
f_string = f"{name} is {age}" # f-string
print(f_string)




# STRING METHODS TRANSFORMATION 

my_string = "HELLO WORLD"
my_string_lower_case = my_string.lower()
print(my_string_lower_case)

my_string_2 = "hElLo WorLD"
my_string_2_upper_case = my_string_2.upper()
print (my_string_2_upper_case)
print (my_string.isalpha())

greetings = my_string.replace("WORLD", "Dave")
print(greetings)

motion = ("jump", "walk", "run")
new_string = "ing ".join(motion)
print(new_string)
print(my_string_2.split(" "))

spaced_string = "     42       "
print(spaced_string.strip())

# lower() / upper() METHOD
str1 = "AbCdEfG"
lower_str = str1.lower()
print(lower_str )       # will print "abcdefg" to the terminal

# replace() METHOD
str = "Hi. Nice to meet you."  
new_str = str.replace(".", "!")
print(new_str)           # would print "Hi! Nice to meet you!"

# split() METHOD
str = "What do you think?"
new_str = str.split()
print(new_str)           # would print ['What', 'do', 'you', 'think?']

str = "Oranges and apples and bananas"
fruit_list = str.split("and")
print(fruit_list)        # would print ['Oranges ', ' apples ', ' bananas ']


dwarves = "Grumpy, Dopey, Doc, Happy, Bashful, Sneezy, Sleepy"
print(dwarves) # Grumpy, Dopey, Doc, Happy, Bashful, Sneezy, Sleepy
lowercase_string = dwarves.lower()
print(lowercase_string) # grumpy, dopey, doc, happy, bashful, sneezy, sleepy
commas_removed = lowercase_string.replace(",", "")
print(commas_removed) # grumpy dopey doc happy bashful sneezy sleepy
split_list = commas_removed.split()
print(split_list) # ['grumpy', 'dopey', 'doc', 'happy', 'bashful', 'sneezy', 'sleepy']
