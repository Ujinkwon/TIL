<template>
  <div>
    <h1>hello, {{ userName }}</h1>
  </div>
</template>

<script>
export default {
    name: 'HelloView',
    data() {
      return {
        userName: this.$route.params.userName
      }
    },
    // 컴포넌트 가드
    // params 변화 감지
    beforeRouteUpdate(to, from, next) {
      this.userName = to.params.userName
      next()
    }
}
</script>

<style>

</style>