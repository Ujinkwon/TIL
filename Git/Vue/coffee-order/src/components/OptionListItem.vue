<template>
  <button type="button" class="text-dark border border-dark rounded bg-white border-2 m-3 p-3" disabled>
    {{ option.type }}
    <div>
    <b-button @click="decrease" pill variant="outline-info" size="sm">-</b-button>
    {{ option.count }}
    <b-button @click="increase" pill variant="outline-info" size="sm">+</b-button>
  </div>
  </button>
</template>

<script>
export default {
  name: 'OptionListItem',
  props: {
    option: Object,
  },
  methods: {
    increase() {
      this.$store.dispatch('increase', this.option)
    },
    decrease() {
      this.$store.dispatch('decrease', this.option)
    },
  },
}
</script>

<style>
</style>