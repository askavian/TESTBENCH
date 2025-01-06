// EQUALITY

console.log(42 === "42");
console.log(1 == "1");

console.log(0 !== "0");
console.log(1 != true);

//EQUALITY TRANSFORMATION

let oldPassword = "myPassword";
let newPassword = "HelloWorld";
let code = "5678";

code = Number(code);
console.log(code === 5678);
console.log(oldPassword !== newPassword);



// IF STATEMENTS

let myString = "JavaScript is powerful!";

if (myString === "JavaScript is powerful!") {
    console.log("Understanding JavaScript unlocks so many possibilities.");
}

console.log("Code Ends");


let studentName = "Malte";

if (studentName === "Malte") {
    console.log(`Welcome, ${studentName}!`);
} else {
    console.log("Incorrect!");       
    }

console.log("Student check complete.")


// IFELSE STATEMENT


let tildaNote = 1;
if (tildaNote > 4) {
    console.log("Du machst, dass meine Augen regnen!");
} else {
    console.log("Da ist der Vater aber sehr stolz! Du bekommst ein neues iPhone!")
}


let productInStock = false;
if (productInStock === true) {
    console.log("Product in stock!")
} else {
    console.log("Product out of stock.")
}


let password = 5678;
if (password === 1234) {
    console.log("Well done! You entered the correct password");
} else {
    console.log("Please enter your password");
}
console.log("Code Ends");


// ELSEIF STATEMENT

function dressCode(weather) {
    if (weather === "rainy") {
        return "Take an umbrella!";
    } else if (weather === "sunny") {
        return "Wear sunglasses!";
    } else {
        return "Check the weather forecast again!";
    }
}

let clothesChoice = dressCode("sunny");
console.log(clothesChoice);



// BETWEEM TWO TIMES
function greeting(time) {
    let greetingMessage = "Time must be a positive integer between 0 and 23 (inclusive).";

    if (0 <= time && time <= 6) {
        greetingMessage = "Good Night!";
    } else if (7 <= time && time <= 11) {
        greetingMessage = "Good Morning!";
    } else if (12 <= time && time <= 18) {
        greetingMessage = "Good Afternoon!";
    } else if (19 <= time && time <= 23) {
        greetingMessage = "Good Evening!";
    }

    return greetingMessage;
}

console.log(greeting(6));




// NESTED IF ELSE STATEMENTS

let user = "Johann";
let emailVerified = false;

if (user === "Johann"){
    if (emailVerified) {
        console.log("Welcome to our website");
    } else {
        console.log("Please verify your email");
    }
} else {
    console.log("You need to be a user to visit this page");
}



function whatShouldIDo(weekend, raining) {
    let result = "";
    
    if (weekend) {
        if (raining) {
            result = "Watch a movie.";
        } else {
            result = "Go for a hike.";
        }
    } else {
        result = "Do your homework!";
    }
    
    return result;
}

let toDo = whatShouldIDo(false, true);
console.log(toDo);



// VARIABLE SCOPE (DO NOT use variables when possible)

function checkScope(){
    if (true) {
        var myVar = 10;
        let myLet = 2;
        console.log("myLet inside the if statement:", myLet);
    }
    
    console.log(myVar);
    // console.log(myLet);
}
checkScope();
// console.log(myVar); // SYNTAX ERROR BECAUSE ITS IN THE FUNCTION



// SWITCH STATEMENTS

let wday = '';
let dayNumber = 0;
switch (dayNumber) {
    case 0:
        wday = 'Sunday';
        break; // BREAK tells the computer to exit the switch statement. Without it, each case would run in turn until a break statement is found,
    case 1:
        wday = 'Monday';
        break;
    case 2:
        wday = 'Tuesday';
        break;
    case 3:
        wday = 'Wednesday';
        break;
    case 4:
        wday = 'Thursday';
        break;
    case 5:
        wday = 'Friday';
        break;
    case 6:
        wday = 'Saturday';
        break;
    default:
        wday = 'Invalid day number';
}
console.log(wday);







let day = "Monday";
switch (day) {
    case "Saturday":
    case "Sunday":
        console.log("It is the weekend!");
        break;
    case "Monday":
    case "Tuesday":
    case "Wednesday":
    case "Thursday":
    case "Friday":
        console.log("It's a weekday.");
        break;
    default:
        console.log("I don't know what day it is!");
}




// TRUTHY FALSY

console.log(Boolean(true));
console.log(Boolean(false));
console.log(Boolean(0));
console.log(Boolean(112));
console.log(Boolean(""));
console.log(Boolean("nonEmptyString"));
console.log(Boolean("    ")); 
console.log(Boolean(-42.247));
console.log(Boolean([])); 
console.log(Boolean({
     firstName: "Aml",
     lastName: "Ameen",
 }));
console.log(Boolean(undefined));

let participants = 100;
if (participants) {
    console.log("Let's get the party started!");
}


// COMPARISON OPERATORS

console.log(21 > 34);
console.log(21 < 34);
console.log(21 >= 21);

console.log(true && false); // &&:AND
console.log(true || false); // ||: OR
console.log(!false);  // !: NOT


let haveKeys = true;
let havePhone = false;
if (haveKeys && havePhone) {
    console.log("I'm ready to go out!");
} else {
    console.log("I forgot something...");
}


function canRideRollercoaster(heightInCm) {
    let message = "Sorry, you are not tall enough to ride this rollercoaster.";
    // Write your code below
    if (heightInCm > 120) {
        message = "Enjoy your ride!"
    }
    // Do not change the code below this line
    console.log(message);
}
canRideRollercoaster(119); // Change the argument to test your code


// TRUTH OR FALSE WITH LOGICAL OPERATORS

function whatToDo(isWeekend, haveFreeTime) {
    if (isWeekend || haveFreeTime) {
        return "Time for some JavaScript!";
    } else {
        return "Back to the grind.";
    }
}
console.log(whatToDo(true, false))




// FINAL TEST GIFT GENERATOR

function giftGenerator(name, age) {
    let gift = "gift description";
    if (name !== "Charlie") {
        if (age < 5) {
            gift = "a soft toy";
        } else if (age < 12) {
            gift = "a fiction book";
        } else if (age < 18) {
            gift = "a new mobile phone";
        } else {
            gift = "some money, so you can buy whatever you like";
        }
    } else {
        gift = "a bar of chocolate with a golden ticket to Willy Wonka's Chocolate Factory";
    }
    return `${name}, your gift is ${gift}. Hope you like it!`;
}

console.log(giftGenerator("Jill", 3)); // should get a soft toy
console.log(giftGenerator("Bob", 11)); // should get a book
console.log(giftGenerator("Jane", 15)); // should get a mobile phone
console.log(giftGenerator("Minh", "I don't know")); // should get money
console.log(giftGenerator("Charlie", 12)); // should get a bar of chocolate