// BASIC FUNCTIONS AND CALLING

function addTwoAndFive() {
    console.log("This function adds 2 and 5");
    console.log(2 + 5);
}

addTwoAndFive();

function showMessage() {
    console.log('Hello world!');
    console.log('Welcome to your first function!');
}

showMessage();
console.log("End of Program");


// DIFFERENT & MULTIPLE PARAMETERS

function sayHello(firstName) {
    let message = `Hello ${firstName}`;
    console.log(message);
}

sayHello("Ronan");
sayHello("Elisa");


function logFullName(firstName, lastName) {
    console.log("Hello,", firstName);
    console.log(`Your name is: ${lastName}, ${firstName}`);
}

logFullName("Frida", "Kahlo");
logFullName("Barack", "Obama");


// RETURN DATA

function addTwo(num1, num2) {
    let total = num1 + num2;
    return total;
    // console.log("Ending the function");
}

let sum = addTwo(3, 5);
console.log(sum);


// Write your code here
function createEmailSignOff(firstName, lastName, title, company) {
    return `Sincerely,

${firstName} ${lastName}
${title}
${company}`;
}

const myEmailSignOff = createEmailSignOff("Filius", "Flitwick", "Charms Professor", "Hogwarts");
console.log(myEmailSignOff);

const myEmailSignOff2 = createEmailSignOff("Jo", "Heyndels", "Content creator", "Code Institute");
console.log(myEmailSignOff2);



// UPDATE VALUE WITH FUNCTION

// Write your code here
let myFavouriteNumber = 7;

function updateFavouriteNumber() {
    const successMessage = "You have updated your favorite number.";
    myFavouriteNumber = 42;
    console.log(successMessage);
}

console.log(myFavouriteNumber);
updateFavouriteNumber();
console.log(myFavouriteNumber);


