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


// BASIC LOOP 

for (i = 0; i <= 10; i++) {
    console.log(i);
  }