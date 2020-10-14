<template lang="html">
  <div id="list">
      <h2>Characters list:</h2>
      <label for="character-select">Select a character:</label>
      <select id="character-select" v-on:change="handleClick" v-model="selectedCharacter">
          <option value="" selected disabled>Select a character</option>
          <option v-for="character in characters" :value="character">{{ character.name }}</option>
      </select>
  </div>
</template>

<script>


export default {
    name: 'characters-list',
    data() {
        return {
            selectedCharacter: null
        }
    },
    props: ['characters'],
    methods:{
        handleClick(){
            eventBus.$emit('character-selected', this.selectedCharacter)
        }
    }
}
</script>

<style lang="css" scoped>
</style>