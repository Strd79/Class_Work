// Named Function Declarations

// function sayHello(greeting, name = "World"){
//     return `${greeting} ${name}!`;
// }

// console.log("sayHello Message:", sayHello("Hi", "David"));



// Anonymous Function Expressions

// var add = function(firstNumber, secondNumber){
//     return firstNumber + secondNumber;
// };

// console.log("1 + 3 with add:", add(1, 3));


// function totalAmount(numbersArray){
//     var total = 0;
//     for (number of numbersArray){
//         total += number;
//     }
//     return total;
// }

// console.log("Total amount:", totalAmount([1, 2, 3, 9]))

// var isItTrueOrFalse = function(object, string){
//     for (var key in object){
//         if (key === string){
//             return true;
//         }
//     }
//     return false;
// };

// var person = {
//     name: "David",
//     age: 41
// }

// console.log(isItTrueOrFalse(person, "banana"));


// Arrow Functions

var multiply = (firstNumber, secondNumber) => firstNumber * secondNumber;

console.log("Multiply 2 by 5:", multiply(2, 5));

