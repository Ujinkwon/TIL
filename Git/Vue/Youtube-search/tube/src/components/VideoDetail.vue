<template>
  <div v-if="video" class="box m-5 p-5">
    <p class="mb-5 fw-bold fs-3">{{ video.snippet.title }}</p>
    <iframe style="width: 100%; height: 300px;" :src="`https://www.youtube.com/embed/${video.id.videoId}`" frameborder="0"></iframe>
  </div>
</template>

<script>
export default {
    name: 'VideoDetail',
    computed: {
      video() {
        return this.$store.state.detail
      }
    }
}
</script>

<style>
  .box {
    box-shadow: 0 10px 20px rgba(0,0,0,0.19), 0 6px 6px rgba(0,0,0,0.23);
  }
</style>