<template>
    <button 
      class="btn m-3 p-3"
      @click="selectMenu"
      :class="{'btn-info': menu.selected, 'btn-outline-dark': !menu.selected}"
    >
    <span ><img :src="imgSrc" alt="" style="width: 15px;"></span>
    <span>{{ menu.title }}</span>
    <span>{{ menu.price }}원</span>
    </button>
</template>

<script>
export default {
  name: 'MenuListItem',
  props: {
    menu: Object,
  },
  data() {
    return {
      imgSrc: this.menu.image,
    }
  },
  methods: {
    selectMenu() {
      this.$store.dispatch('selectMenu', this.menu)
    }
  }
}
</script>

<style>
.imgContainer {
  width: 200px;
  height: 150px;
  overflow: hidden;
}
.img {
  position: absolute;
  width: 100%;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}
</style>