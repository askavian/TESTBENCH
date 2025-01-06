// TERNARY EXPRESSION

let weather = "raining";
let weatherStatus = weather === "raining" ? "Take an umbrella!" : "Enjoy the sunshine!";
console.log(weatherStatus);



let numApples = 0;

let appleText = numApples === 1 ? "apple" : "apples";
console.log(`You have ${numApples} ${appleText}.`);



// ARROW FUNCTIONS

const addTwoNums = (numOne, numTwo) => numOne + numTwo;
let result1 = addTwoNums(5, 6);
console.log(result1);


/*PRE ARROW FUNCTION
function introduceMe(fName, lName) {
    return `${lName}, ${fName} ${lName}`;
}
console.log(introduceMe("James", "Bond"));


function circleCircumference(radius) {
    return Math.PI * radius * 2;
}
console.log(circleCircumference(5));


function multilingualGoodbye() {
    let goodbyes = ["auf Wiedersehen", "goodbye", "adieu", "ciao", "adios"];
    let randomIndex = Math.floor(Math.random() * goodbyes.length);
    return goodbyes[randomIndex];
}
console.log(multilingualGoodbye());


function createPersonObject(fName, age) {
    let personObject = {
        fName: fName,
        age: age
    };
    return personObject;
}
let finn = createPersonObject("Finn", 13);
console.log(finn);// Write the arrow functions here
*/

// PORST ARROW FUNCTION

const introduceMe = (fName, lName) => `${lName}, ${fName} ${lName}`;
console.log(introduceMe("James", "Bond"));


const circleCircumference = radius => Math.PI * radius * 2;
console.log(circleCircumference(5));


const multilingualGoodbye = () => {
    let goodbyes = ["auf Wiedersehen", "goodbye", "adieu", "ciao", "adios"];
    let randomIndex = Math.floor(Math.random() * goodbyes.length);
    return goodbyes[randomIndex];
};
console.log(multilingualGoodbye());


const createPersonObject = (fName, age) => ({fName: fName, age: age});
let finn = createPersonObject("Finn", 13);
console.log(finn);







// Guess the number game!

let secretNumber = 7; // Change this number to set the secret number
let guessedNumber = 7; // Change this number to guess the secret number

if (guessedNumber === secretNumber) {
    console.log("Congratulations! You guessed the secret number!");
} else {
    console.log("Oops! That's not the secret number. Try again!");
}


//DECLARING VARIANBLES LET AND CONST

// Part 1: Declare your variables here
let myFavouriteBook = "Lord of the Rings";
const myBirthYear = 1982;

console.log(myFavouriteBook);
console.log(myBirthYear);

// Part 2: Adjust your favourite book here
myFavouriteBook = "The Hitchhiker's Guide to the Galaxy";

console.log(myFavouriteBook);
console.log(myBirthYear);


let userName = "Alice";
let greeting = "Hello " + userName;
console.log(greeting);

let firstName = "Parvati";
let lastName = "Patil";
console.log(firstName + " " + lastName);


//TYPEOF 

let var1 = "To be, or not to be";
let var2 = false;
let var3 = "728";
let var4 = 'true';
let var5 = 172;

console.log(typeof var1);
console.log(typeof var2);
console.log(typeof var3);
console.log(typeof var4);
console.log(typeof var5);


// DIFFERENT QUOTATION MARKS ' OR "
// Write your code here
let string1 = "'Twas the best of times, 'twas the worst of times.";
let string2 = 'Shakespeare wrote, "To be, or not to be: that is the question".';

console.log(string1)
console.log(string2)


// LITTERAL

let fullName = "Elrond";
let home = "Rivendell";

console.log(`${fullName} lives at ${home}`);


// TRIMING REPLACING 

let fullName1 = "       JaNe DoE       ";
let email = "@email.com";
let fullEmail = fullName1.toLowerCase().trim().replace(" ", "") + email;

console.log(fullName1);
console.log(email);
console.log(fullEmail);


console.log(fullName1);
fullName = fullName1.trim();
console.log(fullName1);

fullName = fullName1.toLowerCase().replace(" ", "");
console.log(fullName1);

fullEmail = fullName1 + email;
console.log(fullEmail);
console.log(fullEmail.includes("@"));

console.log(fullName1.toUpperCase());


const specialWord = "Supercalifragilisticexpialidocious";

console.log(specialWord.length)
console.log(specialWord.slice(9,20))

//OR

console.log(specialWord.length);
let indexOfF = specialWord.indexOf('f');
let indexOfLastE = specialWord.lastIndexOf('e');
console.log(specialWord.slice(indexOfF, indexOfLastE));



//BOOLEANS AND FLIPPING BANG

let isAdult = true;

let fullPrice = isAdult;
let getChildDiscount = !isAdult;

console.log(fullPrice);
console.log(getChildDiscount);



// ARRAYS DATA LIST

let person = {
  firstName: "Siobhan",
  lastName: "Finnegan",
  age: 30,
  country: "USA",
  alive: true
};

console.log(person.age);

person.age = 42;
console.log(person.age);

delete person.alive;
console.log(person);

person.country = "Ireland";
console.log(person);


//MODIFYING LISTS AND ARRAYS

let car = {
  make: "Ford",
  colour: "silver",
  mileage: 30000,
  manufactureYear: 2022, 
  fueled: true
};
console.log(car);

car.colour = "blue";

delete car.manufactureYear;

console.log(car);

car.price = 43000;

console.log(car);


//NESTING ARRAYS AND LISTS

let company = {
  name: 'Apple',
  founded: 1976,
  financials: {
    incomeStatement: {
      years: [1991, 1990, 1989],
      revenue: [125, 120, 115],
      costs: [100, 100, 100],
      profit: [25, 20, 15]
    },
    balanceSheet: {
      years: [1991, 1990, 1989],
      assets: [200, 190, 180],
      liabilities: [100, 95, 90],
      equity: [100, 95, 90]
    },
    cashFlow: {
      years: [1991, 1990, 1989],
      operating: [75, 65, 55],
      investing: [22, 20, 18],
      financing: [-94, -80, -75]    
    }
  },
  competitors: ['Microsoft', 'Amazon', 'Samsung']
};

console.log(company.name);
console.log(company.competitors);
console.log(company.competitors[0]);
console.log(company.financials.incomeStatement.years);
console.log(company.financials.incomeStatement.revenue[0]);




// METHODS MAGIC

const car = {
  whereabouts: "garage",
  ignition: "off",
  fueled: true,
  start() {
    console.log("Vroom Vroom");
    this.ignition = "on";
  }
};

console.log(car.ignition);
car.start();
console.log(car.ignition);


// OPTIONAL ARGUMENTS

let myString = "To be or not to be, that is the question!";

console.log(myString.indexOf('be'));
console.log(myString.indexOf('be', 4));

let firstIndexOfBe = myString.indexOf('be');
console.log(firstIndexOfBe);
console.log(myString.indexOf('be', firstIndexOfBe + 1));




































//NUMBERS VARIABLES

let numint = 10;
console.log(numint)

let numFloat = 20.25;
console.log(numFloat)


let myInt = '10.568163';
let myFloat = '1.2758237364';

// Write your code here
myInt = parseInt(myInt);
myFloat = parseFloat(myFloat);

let result = myInt + myFloat;

let resultFixed = result.toFixed(2);
console.log(resultFixed);
console.log(typeof resultFixed);

let resultFixedNum = Number(resultFixed);
console.log(resultFixedNum);
console.log(typeof resultFixedNum);


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
