<template>
  <div id="lunchmenu">
    <h1>점심메뉴</h1>
    <button @click="select()">Pick Lunch</button>
    <p>{{ menu }}</p>
  </div>
</template>

<script>
var _ = require('lodash')
export default {
    name: 'TheLunch',
    data: function() {
        return {
            menu: '',
            menus: ['짜장', '짬뽕', '탕수육']
        }
    },

    methods: {
        select: function() {
            this.menu = _.sample(this.menus)
        }
    }
}

</script>

<style>

</style>