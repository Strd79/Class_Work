<template lang="html">
  <div class="game-wrapper">
    <game-card v-for="(game, index) in games" :key="index" :game="game" />
  </div>
</template>

<script>
import { eventBus } from '@/main.js'
import GamesService from '@/services/GamesService.js'
import GameCard from './GameCard'
export default {
  data(){
    return {
      games: []
    };
  },
  mounted(){
    GamesService.getGames()
    .then(games => this.games = games);

    eventBus.$on('game-added', (game) => {
      this.games.push(game)
    })

    eventBus.$on('game-deleted', (id) => {
      let index = this.games.findIndex(game => game._id === id)
      this.games.splice(index, 1)
    })
  },
  components: {
    'game-card': GameCard
  }
}
</script>

<style lang="css" scoped>

.game-wrapper {
  display: flex;
  flex-wrap: wrap;
}
</style>
