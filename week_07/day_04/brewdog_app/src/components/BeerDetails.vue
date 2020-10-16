<template>
  <div id="beerDetails">
      <div>
        <h2>Get to know: "{{ beer.name }}"</h2>
        <p class="tagline">"{{ beer.tagline }}"</p>
        <p>ABV: <strong>{{ beer.abv }}</strong><span v-if="beer.abv > 5 && beer.abv <=10">, It's a strong one!</span><span v-if="beer.abv > 10">, It's a <u>REALLY</u> strong one!</span></p>
        <p>First brewed: {{ beer.first_brewed }}</p>
        <p id="description">Description: {{ beer.description }}</p>
        <p><strong>{{ beer.name }}</strong> goes well with the following foods:</p>
        <ul>
            <li v-for="(food, index) of beer.food_pairing" :key="index">{{ food }}</li>
        </ul>
      </div>
      <div>
        <img :src="beer.image_url" :alt="beer.name" class="large_image"><br>
        <button v-if="favouriteBeers.indexOf(beer) == -1" v-on:click="handleClick">Add to favourites</button>
        <p v-if="favouriteBeers.indexOf(beer) !== -1">One of your favourites!</p>
      </div>
  </div>
</template>

<script>
import { eventBus } from '../main.js'

export default {
    name: 'beer-details',
    props: ['beer', 'favouriteBeers'],
    methods: {
        handleClick() {
            eventBus.$emit('favourite-beer', this.beer)
        }
    },
}
</script>

<style>
li {
    list-style: none;
}

.large_image {
    height: 300px;
}

#beerDetails {
    display: flex;
    justify-content: space-evenly;
}

#description {
max-width: 500px;
}

</style>