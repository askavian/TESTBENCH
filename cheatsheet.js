//NUMBERS VARIABLES

let numint = 10;
console.log(numint)

let numFloat = 20.25;
console.log(numFloat)


//STRINGS VARIABLES

let singleQuote = 'A string using single quotes'
console.log(singleQuote)

let doubleQuote = "A string using double quotes"
console.log(doubleQuote)


//BOOLEAN VARIABLES

let admin = true
console.log(admin)

let passwordRequired = false
console.log(passwordRequired)


//If/ELSE If/ELSE

let money, time, vacation, workMore, makeTime;

money = true;
time = false;
if (money && time) {
  vacation = true;
  console.log('Party Time!');
} else if (money && !time) {
  vacation = false;
  makeTime = true;
  console.log('Slack Off More!');
} else if (time && !money) {
  vacation = false;
  workMore = true;
  console.log('Work Harder!');
} else {
  vacation = false;
  workMore = true;
  workMore = true;
  console.log('Good Luck Brother!');
}


//FOR LOOP 

for (i = 0; i <= 10; i++) {
    console.log(i);
  }


//ARRAY LIST

let fruits = ['apple', 'orange', 'banana', 'pear', 'plum'];

// Print all fruits
for (let i = 0; i < fruits.length; i++) {
  console.log(fruits[i]);
}
    
// Reverse the list
fruits.reverse();
console.log(fruits);

// Sort the list alphabetically:
fruits.sort();
console.log(fruits);

// Access ONE Item (Index)
let flowers = ["daisy", "bluebell", "buttercup", "rose", "tulip", "daffodil", "orchid", "geranium", "heather", "hydrangea"];
let flower = flowers[5];
console.log(flowers);
console.log(flower);


//OBJECTS DICTIONARIES

// Create the object
let person = {
    firstName: 'John',
    lastName: 'Smith',
    age: 32,
  };
  
  // Print its properties using dot notation
  console.log(person.firstName);
  console.log(person.lastName);
  console.log(person.age);
  
  // Or using square bracket notation
  console.log(person['firstName']);
  console.log(person['lastName']);
  console.log(person['age']);


//SETS

  // Create a set
let directions = new Set(['north', 'south', 'east', 'west']);

// Display the set
console.log(directions);

// Add an item to the set:
directions.add('northwest');

// Display it again
console.log(directions);


//Nested & Multi-dimensional Data Structures

// Create an array of contact objects
let contacts = [
    {
      name: 'Joe',
      phoneNumber: '123456789'
    },
    {
      name: 'Mary',
      phoneNumber: '456789123'
    },
    {
      name: 'Dad',
      phoneNumber: '789132456'
    },
  ];
  
  // Print each contact using its array index
  console.log(contacts[0]);
  console.log(contacts[1]);
  console.log(contacts[2]);


//Navigation & Iteration of Data Structures

// Create an array of arrays
let controls = [
    ['up', 'down', 'left', 'right'],
    ['a', 'b', 'select', 'start']
  ];
  
  // Log the first sub-array
  console.log(controls[0]);  
  
  // Log the second sub-array
  console.log(controls[1]);
  
  // In the first sub-array (index 0) each item is a direction
  console.log(controls[0][0]);  // logs 'up'
  console.log(controls[0][1]);  // logs 'down'
  console.log(controls[0][2]);  // logs 'left'
  console.log(controls[0][3]);  // logs 'right'
  
  // In the second sub-array (index 1) each item is a button
  console.log(controls[1][0]);  // logs 'a'
  console.log(controls[1][1]);  // logs 'b'
  console.log(controls[1][2]);  // logs 'select'
  console.log(controls[1][3]);  // logs 'start'
