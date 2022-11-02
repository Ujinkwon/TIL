<template>
  <div>
    <h1>로또를 뽑아보자</h1>
    <button @click="pick">Pick Lotto</button>
    <p>{{ num }}</p>
  </div>
</template>

<script>
var _ = require('lodash')
export default {
    name: 'TheLotto',
    data() {
        return {
            num: '',
            nums: _.range(1, 46)
        }
    },

    methods: {
     pick: function() {
        this.num = _.sampleSize(this.nums, 6)
     }   
    }
}
</script>

<style>

</style>