<template>
  <b-list-group-item button @click="videoDetail" class="d-flex justify-content-between align-items-center">
    <!-- <iframe :src="`https://www.youtube.com/embed/${video.id.videoId}`" frameborder="0"></iframe> -->
    <img :src="`${video.snippet.thumbnails.default.url}`" alt="" srcset="">
    <span class="m-3">
        <span class="fw-bold">{{ video.snippet.title }}</span>
        <p></p>
        <span>{{ video.snippet.description }}</span>
    </span>
  </b-list-group-item>
</template>

<script>
export default {
    name: 'VideoListItem',
    props: {
      video: Object,
    },
    methods: {
      videoDetail() {
        console.log(this.video)
        this.$store.dispatch('videoDetail', this.video)
      }
    }

}
</script>

<style>

</style>