<template>
  <div class="m-5">
    <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search" v-model="inputData" @keyup.enter="inText">
  </div>
</template>

<script>
export default {
    name: 'TheSearchBar',
    data() {
      return {
        inputData: null,
      }
    },
    methods: {
      inText() {
        this.$emit('get-list', this.inputData)
        this.$store.dispatch('inText')
      },
    },
}
</script>

<style>

</style>