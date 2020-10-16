<template lang="html">
  <div id="beerDropdown">
    <label for="beer-list">Pick a beer punk!</label>
    <select v-on:change="handleSelection" v-model="selectedBeer" id="beer-list">
        <option value="" disabled>Pick a beer punk!</option>
        <option v-for="beer in beers" :value="beer">{{ beer.name }}</option>
    </select>
  </div>
</template>

<script>
import { eventBus } from '../main.js'

export default {
    name: 'beers-dropdown-list',
    props: ['beers'],
    data() {
        return {
            'selectedBeer': {}
        }
    },
    methods: {
        handleSelection() {
            eventBus.$emit('selected-beer', this.selectedBeer)
        }
    },
}
</script>

<style>

#beerDropdown {
    display: flex;
    flex-direction: column;
}

select {
    width: 20%;
    margin: auto;
}

label {
    margin-bottom: 10px;
}

</style>