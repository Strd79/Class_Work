<template>
<div>
  <h1>Countries</h1>

   <label for="country_select">Select a Country:</label>
    <select id="country_select" v-model="selectedCountry">
      <option disabled value="">Select a country</option>
      <option v-for="(country, index) in countries" :key="index" :value="country">{{country.name}}</option>
    </select>

  <div>
      <country-details v-if="selectedCountry" :country="selectedCountry"></country-details>
  </div>

  <button v-if="!favouriteCountries.includes(selectedCountry)" v-on:click="addToFavourites">Add Country</button>

  <favourite-countries :favouriteCountries="favouriteCountries"></favourite-countries>
  </div>
</template>

<script>

import CountryDetail from './components/CountryDetail.vue';
import FavouriteListItem from './components/FavouriteListItem.vue';

export default {
  name: 'app',
  data(){
    return {
      countries: [],
      selectedCountry: null,
      favouriteCountries: []
    }
  },
  components: {
    'country-details': CountryDetail,
    'favourite-countries': FavouriteListItem
  },
  methods: {
    fetchData(){
    fetch("https://restcountries.eu/rest/v2/all")
    .then(response => response.json())
    .then(data => this.countries = data)
     },
    addToFavourites(){
        this.favouriteCountries.push(this.selectedCountry)
      }
  },
  mounted(){
    this.fetchData()
  }
}
</script>

<style>
.small-flag {
  height: 20px
}
</style>
