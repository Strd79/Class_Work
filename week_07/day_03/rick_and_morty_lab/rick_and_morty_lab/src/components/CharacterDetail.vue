<template>
  <div v-if="selectedCharacter" id="detail">
      <h2>Character details:</h2>
      <h3>{{ character.name }}</h3>
      <p> {{ character.status}}</p>
      <p> {{ character.species }}</p>
      <img :src="character.image" class="image">
  </div>
</template>

<script>
export default {
    name: 'character-detail',
    props: ['selectedCharacter'],
}
</script>

<style lang="css" scoped>

</style>