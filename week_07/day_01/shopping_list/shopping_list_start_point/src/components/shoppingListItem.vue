<template>
  <li :class="purchasedClass">{{ item.name }}</li>
</template>

<script>
export default {
    name: 'shopping-list-item',
    props: ['item'],
    computed: {
        purchasedClass: function() {
            return this.item.isPurchased ? "purchased" : "not-purchased"
        }
    }
}
</script>

<style>

    .not-purchased {
        background-color: lightgoldenrodyellow;
    }

    .purchased {
        text-decoration: line-through;
        background-color: red;
    }

</style>