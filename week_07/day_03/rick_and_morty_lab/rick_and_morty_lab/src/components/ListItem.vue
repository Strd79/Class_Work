<template lang = "html">
<option selected disabled value="">Select a character</option>
  <option v-on:click="handleClick" :value="character">{{ character.name }}</option>
</template>

<script>
import { eventBus } from '../main.js'
export default {
    name: 'list-item',
    props: ['character'],
    methods:{
        handleClick(){
            eventBus.$emit('character-selected', this.character)
        }
    }
}
</script>

<style lang="css" scoped>
</style>