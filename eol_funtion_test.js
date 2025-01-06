/**
 * Select a meal and drink
 */
function whatsForDinner() {
    const mealOptions = [
        "Spagetti",
        "Fish and Chips",
        "Currywurst",
        "Burger",
        "Kebap"
        ];
        // console.log(mealOptions);
    const randomMealInt = Math.floor(Math.random() * mealOptions.length);
    // console.log(randomMealInt);
    const chosenMeal = mealOptions[randomMealInt];
    //console.log(chosenMeal);
    
    const drinkOptions = [
        "Beer",
        "Coca Cola",
        "Wine",
        "Juice",
        "Springwater"
        ];
        // console.log(drinkOptions);
    const randomDrinkInt = Math.floor(Math.random() * drinkOptions.length);
    // console.log(randomDrinkInt);
    const chosenDrink = drinkOptions[randomDrinkInt];
    // console.log(chosenDrink);

    const message = `Enjoy your ${chosenMeal} and ${chosenDrink}!`;
    console.log(message);
}

whatsForDinner();