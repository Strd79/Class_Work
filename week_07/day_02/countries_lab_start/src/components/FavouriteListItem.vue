<template lang="html">
  <div id="favourite_countries">
    <h2>Favourite Countries</h2>
    <ul>
      <li v-for="(country, index) in favouriteCountries" :key="index">
        <img class="small-flag" :src="country.flag" />
        {{ country.name }}
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'favourite-countries',
  props: ["favouriteCountries"]
}
</script>

<style lang="css" scoped>
</style>
