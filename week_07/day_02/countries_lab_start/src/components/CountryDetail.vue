<template lang="html">
  <div v-if="selectedCountry" id="selected_country">
    <h2> {{ selectedCountry.name }} </h2>
    <p> Population:  {{ formatNumber(selectedCountry.population) }} </p>
    <p> Region: {{ selectedCountry.region }}</p>
    <img class="lrg-flag" :src="selectedCountry.flag"/>

    <neighbouring-countries>
    </neighbouring-countries>

</div>
</template>

<script>
import NeighbourCountry from './NeighbourCountry.vue';
export default {
  name: 'country-detail',
  props: ["selectedCountry", "formatNumber"],
  components: {
    'neighbouring-countries': NeighbourCountry
  }
}
</script>

<style lang="css" scoped>

.lrg-flag {
  height: 100px
}

</style>
