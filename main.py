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

