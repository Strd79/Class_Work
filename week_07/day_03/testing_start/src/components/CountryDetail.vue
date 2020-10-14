<template>
  <div id="selected_country">
    <h2> {{country.name}} </h2>
    <p> Population: {{country.population}} </p>
    <img class="lrg-flag" :src="country.flag" />
</div>
</template>

<script>
export default {
    name: 'country-detail',
    props: ['country']
}
</script>

<style scoped>
  .lrg-flag {
  height: 100px
}
</style>
