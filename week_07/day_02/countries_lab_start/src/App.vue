<template>
  <div id="app">
    <h2>Global population: {{ formatNumber(globalPopulation) }}</h2>

    <label for="country_select">Select a Country:</label>
    <select id="country_select" v-model="selectedCountry">
      <option disabled value="">Select a country</option>
      <option v-for="(country, index) in countries" :value="country" :key="index">{{country.name}}</option>
    </select>

    <country-detail :selectedCountry="selectedCountry" :formatNumber="formatNumber"></country-detail>

    <button v-on:click="addToFavourites">Add Country</button>

    <favourite-countries :favouriteCountries="favouriteCountries"></favourite-countries>
</div>

</template>

<script>
import CountryDetail from './components/CountryDetail.vue';
import FavouriteListItem from './components/FavouriteListItem.vue';

export default {
  name: 'App',
  data() {
    return {
      countries: [],
      selectedCountry: null,
      favouriteCountries: [],
    }
  },
  components: {
    'country-detail': CountryDetail,
    'favourite-countries': FavouriteListItem
  },
    computed: {
      globalPopulation: function() {
        return this.countPopulation();
      },
    },
    mounted(){
      this.fetchCountries();
    },
    methods: {
      fetchCountries: function() {
        const request =  fetch("https://restcountries.eu/rest/v2/all")
        .then(response => response.json())
        .then(data => this.countries = data)
      },
      countPopulation: function() {
        return this.countries.reduce((total, country) => {
          return total += country.population
        }, 0)
      },
      formatNumber: function(num) {
        return num.toString().replace(/(\d)(?=(\d{3})+(?!\d))/g, '$1,')
      },
      addToFavourites: function() {
        this.favouriteCountries.push(this.selectedCountry)
      }
    }
}
</script>

<style>
.small-flag {
  width: 40px
}



</style>
