const Pet = require('./pet.js');
const Person = require('./person.js');


const scooby = new Pet('Scooby Doo', 'Dog');
// scooby.eat('scooby snack');

const shaggy = new Person('Shaggy Rogers', scooby);
// shaggy.greet();

// console.log("Shaggy:", shaggy);

shaggy.feedPet("Scooby Snack");