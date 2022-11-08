<template>
  <div class="menu-list">
    <h2 class="pb-2">1. 음료를 고르세요.</h2>
    <MenuListItem
      v-for="(menu, index) in menuList"
      :key="index"
      :menu="menu"
      class="d-flex justify-content-between d-grid gap-2 col-10 mx-auto"
    />
  </div>
</template>

<script>
import MenuListItem from '@/components/MenuListItem';

export default {
  name: 'MenuList',
  components: {
    MenuListItem
  },
  computed: {
    menuList() {
      return this.$store.state.menuList
    },
  },
  // methods: {
  //   selectMenu: function () {},
  // },
}
</script>

<style>

</style>