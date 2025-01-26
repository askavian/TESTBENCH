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


#FOR LOOP

my_string = "iterate over this"

for letter in my_string:
    print(letter);

for i, letter in enumerate(my_string):
    print(i, letter)


#ARRAY LIST

fruits = ['apple', 'orange', 'banana', 'pear', 'plum']

# Print all fruits
for fruit in fruits:
    print(fruit)

print()

# Get an item located in a list
second_item = fruits[1]
print(second_item)
print()

# Add an item to the list
fruits.append('cherries')
print(fruits)
print()

# Reverse the list
fruits.reverse()
print(fruits)

# Sort the list alphabetically:
fruits.sort()
print(fruits)

# Access ONE Liste Item
flowers = ["daisy", "bluebell", "buttercup", "rose", "tulip", "daffodil", "orchid", "geranium", "heather", "hydrangea"]
flower = flowers[9]
print(flowers)
print(flower)


#OBJECT/DICTIONARIES

# Create the dictionary
my_dict = {
  'some_number': 12,
  'a_string': 'Hello world!',
  'nested_list': [1, 2, 3],
  'a_boolean': True,
}

# Print its contents one by one
print(my_dict['some_number'])
print(my_dict['a_string'])
print(my_dict['nested_list'])
print(my_dict['a_boolean'])


#SETS

# Create a set
directions = set(['north', 'south', 'east', 'west'])

# Print its members
for direction in directions:
    print(direction)

# Add an item to the set:
directions.add('northwest')

print()
# Print the members again
# Notice the order cannot be relied upon!
for direction in directions:
    print(direction)


#Nested & Multi-dimensional Data Structures

# Create a list of foods by food group
foods = {
  'dairy': ['milk', 'cheese', 'yogurt'],
  'grains': ['oats', 'cereal', 'pasta'],
  'fats_and_sweets': ['chocolate', 'sugar', 'butter'],
  'fruits': ['apples', 'oranges', 'bananas'],
  'vegetables': ['broccoli', 'beans', 'peas']
}

# Print each group
print(foods['dairy'])
print(foods['grains'])
print(foods['fats_and_sweets'])
print(foods['fruits'])
print(foods['vegetables'])


#Navigation & Iteration of Data Structures

# Create a dictionary of food groups
foods = {
  'dairy': ['milk', 'cheese', 'yogurt'],
  'grains': ['oats', 'cereal', 'pasta'],
  'fats_and_sweets': ['chocolate', 'sugar', 'butter'],
  'fruits': ['apples', 'oranges', 'bananas'],
  'vegetables': ['broccoli', 'beans', 'peas']
}

# Print the entire dairy group
print(foods['dairy'])

# Print specific foods from the dairy group
print(foods['dairy'][0]) 
print(foods['dairy'][1])
print(foods['dairy'][2])