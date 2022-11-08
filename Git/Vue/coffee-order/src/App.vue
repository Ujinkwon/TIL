<template>
  <div id="app">
    <div>
      <b-navbar toggleable="sm" type="light" variant="white">
        <b-navbar-toggle target="nav-text-collapse"></b-navbar-toggle>
        <b-navbar-brand>Coffee Order App</b-navbar-brand>
      </b-navbar>
    </div>

    <b-list-group class="d-flex flex-row p-4" style="border-radius: 13px; background-color: aliceblue">
      <b-list-group-item class="box border-white"><MenuList/></b-list-group-item>
      <b-list-group-item class="mx-4 box border-white"><SizeList/></b-list-group-item>
      <b-list-group-item class="box border-white"><OptionList/></b-list-group-item>
    </b-list-group>

    <div class="d-flex flex-column m-3">
      <button
      class="btn btn-outline-primary btn-lg mb-3"
      @click="order"
    >
      장바구니 담기
    </button>

    <button
      class="btn btn-outline-primary btn-lg"
      @click="orderFinish"
    >
      주문하기
    </button>
    </div>

    <OrderList class="box" style="background-color: aliceblue; padding: 30px;"/>

  </div>
</template>

<script>
import MenuList from '@/components/MenuList'
import SizeList from '@/components/SizeList'
import OrderList from '@/components/OrderList'
import OptionList from '@/components/OptionList'

export default {
  name: 'App',
  components: {
    MenuList,
    SizeList,
    OrderList,
    OptionList,
  },

  computed: {
  },

  methods: {
    order() {
      this.$store.dispatch('order')
    },
    orderFinish() {
      this.$store.dispatch('orderFinish')
    },
  }
}
</script>

<style>
* {
  box-sizing: border-box;
  font-family: 'Noto Sans KR', sans-serif;
  padding: 0;
  margin: 0;
}

ul {
  list-style: none;
}

.box {
  border-radius: 13px;
}

/* #app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
} */
</style>
