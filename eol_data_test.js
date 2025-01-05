// Write your code here
// Write your code here
let pet = {
    petName: "Woofie",
    petSpecies: "dog",
    owner: "Malte",
    lengthOfStay: 21,
    activities: ["playing with the ball", "playing in the garden", "jumping"]
};

let numOfActivities = pet.activities.length;
let favActivities = pet.activities.sort()[numOfActivities -1];
let speciesCapitalized = pet.petSpecies[0].toUpperCase() + pet.petSpecies.slice(1);

// console.log(pet);
// console.log(numOfActivities);
// console.log(favActivities);
// console.log(speciesCapitalized);
// console.log(pet);





// Report message to update
let report = `Dear ${pet.owner},

${pet.petName} stayed at the Paws & Purrfection Palace for ${pet.lengthOfStay} days.
While they were with us, we did ${numOfActivities} activities with them. 
Their favourite activity was ${favActivities}. 

They won ${speciesCapitalized} of the Week while they were with us, and we'd love to have them stay again.

We hope you had a pawsome time while you were away, and you and PET NAME will visit us again soon!

Isabella Whiskerwell
Paws & Purrfection Palace
`;

console.log(report);