<template lang="html">
  <form class="" v-on:submit="addGame" method="post">
    <label for="name">Name:</label>
    <input type="text" id="name" v-model="name" required/>

    <label for="playingTime">Playing Time:</label>
    <input type="number" id="playingTime" v-model.number="playingTime" required/>

    <label for="minNumPlayers">Min Players:</label>
    <input type="number" id="minNumPlayers" v-model.number="players.min" required/>

    <label for="maxNumPlayers">Max Players:</label>
    <input type="number" id="maxNumPlayers" v-model.number="players.max" required/>

    <input type="submit" value="Save" id="save"/>

  </form>
</template>

<script>
import { eventBus } from '@/main.js'
import GamesService from '@/services/GamesService.js'

export default {
  name: 'game-form',
  data(){
    return {
      name: '',
      playingTime: null,
      players: {
        min: null,
        max: null
      }
    }
  },
  methods: {
    addGame(e){
      e.preventDefault()
      const game = {
        name: this.name,
        playingTime: this.playingTime,
        players: {
          min: this.players.min,
          max: this.players.max
        }
      }
      GamesService.postGame(game)
      .then(res => eventBus.$emit('game-added', res))
    }
  }
}
</script>

<style lang="css" scoped>

form {
  margin-top: 20px;
}

input {
  margin: 0.2em 1.5em 0.2em 0.4em;
}

input[type=number], input[type=text] {
  border-radius: 3px;
  padding: 5px;
  border-style: none;
}

input[type=number] {
  width: 40px;
}

input[type=submit] {
  display: block;
  border-radius: 5px;
  background-color: #9172ff;
  padding: 4px 10px 6px;
  margin: 1em 0;
}
</style>
