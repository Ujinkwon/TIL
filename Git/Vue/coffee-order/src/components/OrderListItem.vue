<template>
  <b-list-group-item>
    <span class="d-flex">
    <img :src="imgSrc" alt="" style="width: 100px;">
    <span class="d-flex flex-column justify-content-center m-3">
      <div>{{ order.menu.title }}</div>
      <div>사이즈 : {{ order.size.name }}</div>
    </span>
    </span>

  <span class="d-flex flex-column justify-content-center">
    가격 : {{ totalPrice }}
    <span class="d-flex flex-row">
    <div v-for="(option, index) in order.option"
      :key="index"
    >
    <div>
      {{ option.type }}
      {{ option.count }}회
      <span>|</span>
    </div>
    </div>
  </span>
</span>
  </b-list-group-item>
</template>

<script>
export default {
  name: 'OrderListItem',
  data() {
    return {
      imgSrc: this.order.menu.image,
    }
  },
  props: {
    order: Object,
  },
  computed: {
    totalPrice() {
      const optionPrice = (this.order.option[0].price*this.order.option[0].count) + (this.order.option[1].price*this.order.option[1].count) + (this.order.option[2].price*this.order.option[2].count)
      return this.order.menu.price + this.order.size.price + optionPrice
    },

  },
}
</script>

<style>
</style>