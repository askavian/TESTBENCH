# COMPARING VALUES
print('Hello, World!' == 'Hello, World!')
print(2!=2)
print([1,2]<[1,2,3])
print(float(2)>=int(2))
print('a'<'A') #This is False as 'a' is Unicode 97 where 'A' is 65

a = 10
b = 5
print(a == b) # a is equal to b
print(a < b) # a is less than b
print(a <= b) # a is less than or equal to b
print(a > b) # a is greater than b
print(a >= b) # a is greater than or equal to b


# LOGICAL OPERATORS not, and, or
print(True and True) # TRUE
print(True and False) # FALSE
print(True or False) # TRUE
print(not (4 < 5 and 4 < 10)) # FALSE


# Determining Truth With Logical Operators Challenge
tickets = 2
customers = 2
age_person_1 = 21
age_person_2 = 16 

enter = tickets >= customers and age_person_1 >= 18 and age_person_2 >= 18
print(enter)


a = 10
b = 5
result_one = a > b and a > 10 # a is greater than b and a is greater than 10
print(result_one)
result_two = a == 5 or b < 5 # a is equal to 5 or b is less than 5
print(result_two)
result_three = not(result_two) # reverses/negates result_two
print(result_three)


# BOOLEANS
names = [1, 2, 3,]
print(bool(names)) # TRUE

# CHECK IF IT IS A BOOL
a = [1, 2, 3,]
b = "False"
c = "True"
d = 1.23
e = 1
print(bool(a))
print(bool(b))
print(bool(c))
print(bool(d))
print(bool(e))



# EQUALITY VS. IDENTIDY
num = 1
bool = True
print(num == bool) # equality
print(num is bool) # identity

a=1
b=1.0
print(a==b)
print(a is b)
print(id(a))
print(id(b))
# a and b have the same numeric value but a different type
c=b
print(b==c)
print(b is c)
print(id(b))
print(id(c))
# b and c are equal in value and identity

list_a = [10, 20, 30,]
list_b = [10, 20, 30,]
list_c = list_a
print(list_a is list_b) # IS
print(list_a == list_b) # EQUAL
print(list_a is list_c) # IS



# Checking Containment with Containment Operators
print('Program' in 'Programming')
print('spam' in ['spam', 'egg'])
print('sausage' not in ['spam', 'egg'])
print("rat" in "crate")
print("ink" not in "sink")
print("robbie" in ["gary", "howard", "mark", "jason"])