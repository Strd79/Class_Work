<template>
  <div id="app">
    <h1>My App</h1>
    <p v-if="serverMessaage">The server said: {{ serverMessaage }}</p>
  </div>
</template>

<script>
export default {
  name: 'app',
  mounted(){
    fetch("http://localhost:3000")
    .then(response => response.json())
    .then(data => this.serverMessaage = data.message);
  },
  data () {
    return {
      serverMessaage: ""
    }
  }
}
</script>

<style>

</style>
