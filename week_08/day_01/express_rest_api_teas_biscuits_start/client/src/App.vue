<template>
  <div id="app">
    <tea-biscuit-form />
    <tea-list :teas="teas" />
    <biscuit-list :biscuits="biscuits" />
  </div>
</template>

<script>
import TeaBiscuitForm from '@/components/TeaBiscuitForm';
import TeaList from '@/components/TeaList';
import BiscuitList from '@/components/BiscuitList';

import { eventBus } from './main';

export default {
  name: 'app',
  data () {
    return {
      teas: [],
      biscuits: []
    }
  },
  methods: {
    fetchData(){
      fetch("http://localhost:3000/api/teas")
        .then(response => response.json())
        .then(teas => this.teas = teas);

      fetch("http://localhost:3000/api/biscuits")
        .then(response => response.json())
        .then(biscuits => this.biscuits = biscuits);
    }
  },
  mounted() {
    this.fetchData();

    eventBus.$on("refresh-data", this.fetchData);
  },
  components: {
    'tea-biscuit-form': TeaBiscuitForm,
    'tea-list': TeaList,
    'biscuit-list': BiscuitList
  }
}
</script>

<style>

</style>
