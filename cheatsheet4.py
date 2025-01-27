# IF/ELSE STATEMENT / FLOW CONTROL
number = int(input("Please enter a number:"))
if number == 5:
    print(f"{number} is equal to 5")
else:
    print(f"{number} is not equal to 5")

hunger = str(input("Hat der Adam Hunger?"))
if hunger == "ja":
    print("Dann kann der Adam noch nicht ins Bett gehen und muss etwas essen!")
else:
    print("Dann ab in die Kiste und SCHLAFEN!")

a = 10
b = 20
result = None
if a == b:
    result = 'a has the same value as b'
else:
    result = 'a has not got the same value as b'
print(result)



# TERNARY EXPRESSIONS IN PYTHON (shorthand version of if/else)
my_boolean = False # if True switches to "Hello"
my_string = "Hello" if my_boolean else "World" # SHORT IF/ELSE
print(my_string)

full_access = True
result_01 = True if full_access else False
print(result_01)
