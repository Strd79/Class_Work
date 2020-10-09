const { prototype } = require("mocha");

const Cinema = function (films) {
  this.films = films;
};

Cinema.prototype.listFilmTitles = function() {
  return this.films.map((film) => {
    return film.title;
  });
};

Cinema.prototype.findFilmByTitle = function(title) {
  return this.films.filter((film) => {
    if (film.title === title) {
      return film;
    };
  });
};

Cinema.prototype.filterByGenre = function(genre) {
  return this.films.filter((film) => {
    if (film.genre === genre) {
      return film;
    };
  });
};

Cinema.prototype.weatherFilmsFromParticularYear = function(year) {
  return this.films.some((film) => {
    return film.year === year;
  });
};

Cinema.prototype.allFilmsOverParticularLength = function(length) {
  return this.films.every((film) => {
    return film.length > length;
  });
};

Cinema.prototype.totalRunningTime = function() {
  const total = this.films.reduce((runningTotal, number) => {
    return runningTotal + number.length;
  }, 0);
  return total;
};

module.exports = Cinema;
