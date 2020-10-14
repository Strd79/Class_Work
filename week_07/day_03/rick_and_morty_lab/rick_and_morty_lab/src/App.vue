<template>
  <div id="app">
    <h1>Rick & Morty</h1>
    <div class="main-container">
      <characters-list :characters="characters"></characters-list>
      <character-detail :character="character"></character-detail>
    </div>
  </div>
</template>

<script>
import { eventBus } from './main.js';
import CharactersList from './components/CharactersList';
import CharacterDetail from './components/CharacterDetail';

export default {
  name: 'App',
  data() {
    return {
      characters: [],
      selectedCharacter: null
    };
  },
  components: {
    'character-detail': CharacterDetail,
    'characters-list': CharactersList
  },
  mounted(){
    fetch('https://rickandmortyapi.com/api/character/')
    .then(res => res.json())
    .then(characters => this.characters= characters.results)

    eventBus.$on('character-selected', (character) => {
      this.selectedCharacter = character
    })
  }
}
</script>

<style>
.main-container {
  display: flex;
  justify-content: space-around;
}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: left;
  background-color: rgb(06, 43, 44);
  color: white;
  margin-top: 60px;
  background-image: url("static/rick_and_morty.jpg");
}

h1 {
  text-align: center;
  font-size: 50px;
}

#list {
  background-color: rgba(0, 0, 0, 0.6);
  padding: 20px;
}

#detail {
  background-color: rgba(0, 0, 0, 0.6);
  padding: 20px;
}

li {
  list-style: none;
}
</style>
