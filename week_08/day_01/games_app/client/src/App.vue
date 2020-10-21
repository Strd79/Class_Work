<template>
  <section>
    <game-form />
    <games-grid />
  </section>
</template>

<script>
import GameForm from '@/components/GameForm';
import GamesGrid from '@/components/GamesGrid';

export default {
  name: 'app',
  components: {
    'games-grid': GamesGrid,
    'game-form': GameForm
  }
}
</script>

<style>

body {
  font-family: 'Source Serif Pro', serif;
  background-color: #e2dee8;
  width: 80%;
  margin: 0 auto;
  color: #0E0B16;
}

h1, h2, h3 {
  color: #A239CA;
  font-family: 'Skranji', cursive;
}
</style>
