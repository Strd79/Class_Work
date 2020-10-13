<template>
  <div id="app">
    <h1>{{ greeting }}</h1>
    <button v-on:click="updateGreeting">Change Greeting</button>
  </div>
</template>

<script>

export default {
  name: 'App',
  data() {
    return {
      greeting: "Hello World!"
    }
  },
  methods: {
    updateGreeting: function() {
      this.greeting = "Changed!";
    },
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
