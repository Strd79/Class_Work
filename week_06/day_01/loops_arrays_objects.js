var sports = ['football', 'tennis', 'rugby'];

// var numberOfElements = sports.length;

// console.log("number of elements:", numberOfElements);

// var firstSport = sports[0];
// console.log("first sport:", firstSport);

sports.push('curling');
sports.push('snooker');
sports.push('darts');
// console.log("Sports:", sports);

// sports.pop();
// console.log("Sports:", sports);

// var removed_element = sports.pop();
// console.log(removed_element)

// // var removedSport = sports.shift();


// var removedSport = sports.splice(3, 1);
// console.log(removedSport);
// console.log(sports);

// for (var currentSport of sports){
//     var upperCasedSport = currentSport.toUpperCase();
//     console.log(upperCasedSport);
// }

// for ( initialise counter, condition, increment counter)

// for (var i=0; i < sports.length; i++){
//     var currentSport = sports[i]
//     var upperCasedSport = currentSport.toUpperCase();
//     console.log(upperCasedSport);
// }

var movie = {
    title: "It's a Wonderful Life",
    year: 1946,
    language: "Spanish"
};

movie.cast = ["James Stewart", "Donna Reed"];
movie.language = "English";
movie["subtitle-language"] = "German";

// delete movie.year;

movie.ratings = {
    critic: 94,
    audience: 95
}

var audienceRating = movie.ratings.audience
console.log("Audiance Rating:", audienceRating);

// console.log("Movie:", movie);

for (var key in movie){
    var value = movie[key];
    console.log(`The ${key} is ${value}`);
}

var keys = Object.keys(movie)
console.log("Keys:", keys);