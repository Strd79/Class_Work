<template lang="html">
<div class="game-card">
  <h3>{{ game.name }}</h3>
  <p>Playing time: {{ game.playingTime }}</p>
  <p>Players: {{ game.players.min }} - {{ game.players.max }}</p>
  <button type="button" class="delete-btn" v-on:click="deleteGame"></button>
</div>
</template>

<script>
import { eventBus } from '@/main.js'
import GamesService from '@/services/GamesService.js'

export default {
  name: 'game-card',
  props: ['game'],
  methods: {
    deleteGame(){
      GamesService.deleteGame(this.game._id)
      .then(() => eventBus.$emit('game-deleted', this.game._id))
    }
  }
}
</script>

<style lang="css" scoped>
 .game-card {
   background-color: #9172ff;
   border: 1px solid black;
   border-radius: 5px;
   padding: 20px;
   margin: 10px;
 }

 .delete-btn {
   width: 30px;
   height: 30px;
   background: url(../assets/delete.png);
   background-size: 30px;
   border: none;
   padding: 0;
   border-radius: 5px;
 }
</style>
