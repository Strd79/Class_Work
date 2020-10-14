<template lang="html">
  <li v-on:click="handleClick">{{munro.name}}</li>
</template>

<script>
import { eventBus } from "../main.js"

export default {
  name: 'list-item',
  props: ['munro'],
  methods: {
    handleClick() {
      eventBus.$emit("munro-selected", this.munro)
    }
  }
}
</script>

<style lang="css" scoped>
</style>
