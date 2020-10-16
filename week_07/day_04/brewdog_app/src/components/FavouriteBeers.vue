<template>
  <div v-if="beers.length > 0">
      <h2>Favourite beers:</h2>
      <ul>
          <li v-for="(beer, index) in beers" :key="index">
              <h3>{{ beer.name }}</h3>
              <img :src="beer.image_url" :alt="beer.name" class="small_image"><br>
              <button v-on:click="handleClick(beer)">Delete this beer</button>
          </li>
      </ul>
  </div>
</template>

<script>
import { eventBus } from '../main.js'

export default {
    name: 'favourite-beers',
    data() {
        return {
            deletedBeer: null
        }
    },
    props: ['beers'],
    methods: {
        handleClick(beer){
            eventBus.$emit('deleted-beer', beer)
        }
    }
}
</script>

<style>
.small_image {
    height: 50px;
}

button {
    margin-left: 10px;
}
</style>