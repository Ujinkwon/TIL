<template>
  <div>
    <h1>주문 내역</h1>
    <p>총 {{ totalOrderCount }}건 : {{ totalOrderPrice }}원</p>
    <b-list-group>
    <OrderListItem
      v-for="(order, index) in orderList"
      :key="index"
      :order="order"
      class="d-flex justify-content-between"
    />
  </b-list-group>


  </div>
</template>

<script>
import OrderListItem from '@/components/OrderListItem'

export default {
  name: 'OrderList',
  components: {
    OrderListItem,
  },
  

    computed: {
      orderList() {
        console.log(this.$store.state.orderList)
        return this.$store.state.orderList
      },
      totalOrderCount() {
        return this.$store.state.orderList.length
      },
      totalOrderPrice() {
        const price = this.orderList.reduce((acc, order) => {
          const optionPrice = (order.option[0].price*order.option[0].count) + (order.option[1].price*order.option[1].count) + (order.option[2].price*order.option[2].count)
          return acc + ( order.menu.price + order.size.price + optionPrice )
        }, 0)
        return price
      },
    },
}
</script>

<style>
</style>