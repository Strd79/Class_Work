<template>
  <div id="app">
    <nav>
      <router-link :to="{name: 'home'}">Home</router-link>
      <router-link :to="{name: 'about'}">About</router-link>
      <router-link :to="{name: 'contact'}">Contact</router-link>
    </nav>
    <router-view id="view"></router-view>
  </div>
</template>

<script>
export default {
  name: 'app'
}
</script>

<style lang="css" scoped>

nav {
  display: flex;
  justify-content: center;
  width: 50vw;
  margin: 0 auto;
}

#view {
  width: 50vw;
  margin: 0 auto;
}

a{
  margin: 0 20px;
}

</style>
