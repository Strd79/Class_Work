<template>
  <div v-if="munro">
      <h3>{{ munro.name }}</h3>
      <p>Height: {{ munro.height }}</p>
      <p>Region: {{ munro.region }}</p>
      <p>Meaning: {{ munro.meaning }}</p>
  </div>
</template>

<script>
export default {
    name: 'munro-detail',
    props: ['munro']
}
</script>

<style>

</style>