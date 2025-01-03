#NUMBERS VARIABLES

num_int = 10
print(num_int)

num_float = 20.25
print(num_float)


#STRINGS VARIABLES

single_quote = 'A string using single quotes'
print(single_quote)

double_quote = "A string using double quotes"
print(double_quote)


#BOOLEAN VARIABLES

admin = True
print(admin)

password_required = False
print(password_required)


#If/ELSE If/ELSE

money = None
time = None
vacation = None
workMore = None
makeTime = None

money = True
time = False
if money and time:
  vacation = True
  print('Party Time!')
elif money and not time:
  vacation = False
  makeTime = True
  print('Slack Off More!')
elif time and not money:
  vacation = False
  workMore = True
  print('Work Harder!')
else:
  vacation = False
  workMore = True
  workMore = True
  print('Good Luck Brother!')


  #TEST LOOP

my_string = "iterate over this"

for letter in my_string:
    print(letter);

for i, letter in enumerate(my_string):
    print(i, letter)