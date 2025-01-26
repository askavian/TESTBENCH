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