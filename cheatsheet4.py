# IF/ELSE STATEMENT / FLOW CONTROL
number_02 = int(input("Please enter a number:"))
if number_02 == 5:
    print(f"{number_02} is equal to 5")
else:
    print(f"{number_02} is not equal to 5")


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


# IF/ELSE STATEMENTS BOOLEAN LOGIC
number_01 = int(input("Please enter a number:"))
if number_01 == 5:
    print(f"{number_01} is equal to 5")
else:
    print(f"{number_01} is not equal to 5")



# FLOWCONTROL
#FizzBuzz Game FLOWCONTROL CODE
num = int(input("What number?"))
if num % 3 == 0 and num % 5 == 0: # MODULO Operator checks if there is a rest after division
    print("FizzBuzz")
elif num % 3 == 0: # Only prints im divisable by 3
    print("Fizz")
elif num % 5 == 0: # only prints if divisible by 5
    print("Buzz")
else: # if not divisable by 3 or 5 it prints just the number
    print(num)   


number = int(input("Please enter a number:"))
if number > 5:
    print(f"{number} is greater than 5")
elif number < 5:
    print(f"{number} is less than 5")
else:
    print(f"{number} is not greater than, or less than 5. Therefore, {number} must be equal to 5.")    


day = 'Monday'
if day == 'Monday':
    print("Meeting at 9:00")
elif day == 'Wednesday':
    print("Meeting at 2:00")
elif day == 'Friday':
    print("Meeting at 4:00")
else:
    print("No meetings today")



# NESTED IF/ELSE STATEMENTS
exit_program = True
manual_override = False
critical_systems_shutdown = False
if not exit_program and not critical_systems_shutdown:
    if manual_override:
        print("Shutting system down manually")
    else:
        print("This program will not exit just yet")
elif exit_program and critical_systems_shutdown is not True:
    print("Critical systems must be safely shut down before exiting the program")
else:
    print("This program will now be terminated...")



admin = True
update_required = True
if admin:
    if update_required:
        print("You are authorized to update")
    else:
        print("No update required")
else:
    print("You need admin privileges to do this")