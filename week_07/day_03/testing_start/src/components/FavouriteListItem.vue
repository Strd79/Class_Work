<template lang="html">
  <div id="favourite_countries">
    <h2>Favourite Countries</h2>
    <ul>
      <li v-for="favouriteCountry in favouriteCountries">{{favouriteCountry.name}} <img class="small-flag" :src="favouriteCountry.flag"/></li>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'favourite-countries',
  props: ['favouriteCountries']
}
</script>

<style lang="css" scoped>
</style>
