<template>
    <button
    class="btn m-3 p-3"
    @click="selectSize"
      :class="{'btn-info': size.selected, 'btn-outline-dark': !size.selected}"
    >
      <span>{{ size.name }}</span>
      <span>{{ size.price }}</span>
    </button>
</template>

<script>
export default {
  name: 'SizeListItem',
  props: {
    size: Object,
  },

  methods: {
    selectSize() {
      this.$store.dispatch('selectSize', this.size)
    }
  }
}
</script>

<style>
</style>