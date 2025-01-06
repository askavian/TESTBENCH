// INCREMENTING ++ DECREMENTING--

let myNum1 = 5;
let myNum2 = 10;

// prefix
console.log("myNum1", myNum1);
console.log("prefix", ++myNum1);
console.log("myNum1", myNum1);

console.log(); // logs a blank line

// postfix
console.log("myNum2", myNum2);
console.log("postfix", myNum2++);
console.log("myNum2", myNum2);


let score = 0;
let scoreDisplayValue = ++score; // assigns 1

let participants = 100;
let participantsBeforeYou = participants++; // assigns 100

console.log(score);
console.log(participants);


let currentScore = 0;
console.log(currentScore);
// Adjust the current score values below by prefixing or postfixing the increment or decrement operators.
// The first example has been completed for you.
console.log(++currentScore);
console.log(++currentScore);
console.log(currentScore++);
console.log(currentScore++);
console.log(++currentScore);
console.log(--currentScore);
console.log(currentScore--);
console.log(++currentScore);



// WHILE LOOP

let myNumber = 10;
while (myNumber >= 0) {
    console.log(myNumber);
    myNumber--;
}
console.log("And we have lift-off!");


let fruits = ['apples', 'oranges', 'bananas', 'lychees', 'cherries']; // with Array
let index = 0;
while (fruits[index] !== 'lychees') {
    console.log(`I love ${fruits[index]}`);
    index++;
}
console.log(`Yuck, I hate ${fruits[index]}!`);



// FOR LOOP

console.log('Code starts');
for (let i = 0; i < 4; i++) {
    console.log("i =", i);
}
console.log('Code Ends');


function runCountdown(numTurns) {
    console.log("Starting countdown");

    for (let i = numTurns; i >= 0; i--) {
        console.log(i);
    }

    console.log("And we have lift-off!");
}
runCountdown(10);



// NESTED ITERATION

for (let i = 0; i < 3; i++) {
    for (let j = 0; j < 3; j++) {
        let point = [i, j];
        console.log(point);
    }
    console.log("-----");
}


// Write your code here
function logTables() {
    for (let i = 1; i <= 3; i++) {
        console.log(`${i} times table`);
        for (let j = 1; j <= 4; j++) {
            console.log(`${i} x ${j} = ${i * j}`);
        }
        console.log("----");
    }
}

logTables();



// BREAK AND CONTINUE

for (let i = 0; i < 10; i++) {
    if (i === 3) {
        break; // logged KEINE 3 mehr
        // continue;
    }
    console.log(i);
}
console.log("Code Ends");


let myArray = ['John',  7, 'Omar', 'Duc', true, 'Bill'];
for (let i = 0; i < myArray.length; i++) {
    if (typeof myArray[i] === "number") {
        continue;
    } else if (typeof myArray[i] === "boolean") {
        break;
    } else {
        console.log(myArray[i]);
    }
}
console.log("Code Ends");



// ITERATING DATA STRUCTURES FOR...OF LOOP

let students = ["Nikita", "Sandeep", "Muammar", "Aaron", "Yoni", "Cliodna"];
for (let i = 0; i < students.length; i++) { // FOR LOOP
    console.log(students[i]);
}
console.log();
for (let student of students) { // FOR ... OF LOOP
     console.log(student);
 }

// FOR ... OF LOOP USE
 let favouriteBooks = ["The Secret Garden", "Pride and Prejudice", "The Hunger Games"];
 for (let book of favouriteBooks) {
     let myString = `${book} is one of my favourite books!`
     console.log(myString)
 }

 // REGULAR LOOP
 let names = ["Katniss", "Peeta", "Finnick", "Primrose"];
console.log(names);
for (let i = 0; i < names.length; i++) {
    names[i] = names[i].toLowerCase();
}
console.log(names);


const numbers = [43, 2, 90, 12, 14];
for (let number of numbers) {
    console.log(number * 2);
}

for (let i = 0; i < numbers.length; i++) {
    numbers[i] = numbers[i] / 2;   
}
console.log(numbers);




// ITERATING DATA STRUCTURES OBJECTS

const ringbearer = {
    name: "Frodo Baggins",
    age: 50,
    home: "Bag End",
    species: "Hobbit"
};
for (let key in ringbearer) {
    console.log(key);
    
    console.log("-----------");
}


let myPet = {
    name: "Dana",
    species: "dog",
    breed: "labrador",
};
for (let key in myPet) {
   myPet[key] = myPet[key].toUpperCase();
}
console.log(myPet);
// Output: { name: 'DANA', species: 'DOG', breed: 'LABRADOR' }


let players = {
    playerOne: "AECH",
    playerTwo: "Parzival",
    playerThree: "art3mis",
    playerFour: "iRock",
};
// player key + value UND erstellt email adressen
for (let key in players) {
    console.log(key, players[key]);
    players[key] = players[key].toLowerCase() + "@theoasis.com";
}
console.log(players);
