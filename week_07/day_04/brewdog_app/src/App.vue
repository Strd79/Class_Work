<template>
  <div id="app">
    <div id="header">
      <img id ="logo" alt="BrewDog logo" src="./assets/brewdog_logo.jpeg">
      <h1>Brewdog Beers App</h1>
    </div>
    <div id="dropdown">
      <beers-dropdown-list :beers='beers'></beers-dropdown-list>
      <beer-details :beer='selectedBeer' :favouriteBeers='favouriteBeers'></beer-details>
      <favourite-beers :beers='favouriteBeers'></favourite-beers>
    </div>
  </div>
</template>

<script>
import { eventBus } from './main.js';
import BeersDropdownList from './components/BeersDropdownList.vue';
import BeerDetails from './components/BeerDetails.vue';
import FavouriteBeers from './components/FavouriteBeers.vue';

export default {
  name: 'App',
  data() {
    return {
      beers: [],
      selectedBeer: null,
      favouriteBeers: []
    }
  },
  mounted() {
    fetch('https://api.punkapi.com/v2/beers?page=2&per_page=80')
    .then(responce => responce.json())
    .then(beers => this.beers = beers)

    eventBus.$on('selected-beer', (beer) => {
      this.selectedBeer = beer
    })

    eventBus.$on('favourite-beer', (favBeer) => {
      this.favouriteBeers.push(favBeer)
    })

    eventBus.$on('deleted-beer', (deletedBeer) => {
      let index = this.favouriteBeers.indexOf(deletedBeer)
      let removed = this.favouriteBeers.splice(index, 1)
      // console.log(index);
    })
  },
  components: {
    'beers-dropdown-list': BeersDropdownList,
    'beer-details': BeerDetails,
    'favourite-beers': FavouriteBeers
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

  #beerDetails {
    margin-top: 50px;
  }

  #header {
    display: flex;
    justify-content: space-evenly;
  }

  #logo {
    height: 140px;
  }

</style>
