<template>

  <div id="app">

    <h1>My shopping list</h1>
    <shopping-list-item v-for="(item, index) in items" :key="index" :item="item"></shopping-list-item>

  </div>
</template>

<script>
import shoppingListItem from './components/shoppingListItem.vue';
export default {
  data(){
    return {
      items: [
        {name: "Milk", isPurchased: false},
        {name: "Cheese", isPurchased: true},
        {name: "Beans", isPurchased: false},
      ],
      newItem: "",
    }
  },
  components: {
    'shopping-list-item': shoppingListItem
  },
  methods: {
    saveNewItem: function() {
      this.items.push({
        name: this.newItem, 
        isPurchased: false,
      });
      this.newItem = "";
    },
    buyItem: function(index) {
      this.items[index].isPurchased = true;
    },
  },
}
</script>

<style>
#app {
  width: 60%;
  margin: 0 auto;
  font-family: 'Lato', sans-serif;
}

ul {
  margin: 0;
  padding: 0;
  list-style-type: none;
}

li {
  margin: 20px 0;
  padding: 10px;
  display: flex;
  justify-content: space-between;
}

li span {
  padding: 8px;
}

li button {
  background: #f2360c;
  color: #fff;
  border: none;
  padding: 10px;
  cursor: pointer;
}

/* li.purchased {
  border: 2px solid #1a681e;
  color: #1a681e;
}

li.not-purchased {
  border: 2px solid #f2360c;
} */

input[type="text"] {
  padding: 10px;
  width: 50%;
  margin:5px;
}

button, input[type="submit"]{
  padding: 10px;
  background: #000;
  color: #fff;
  cursor: pointer;
  border: 1px solid #000;
}

</style>