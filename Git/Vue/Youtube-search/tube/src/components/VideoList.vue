<template>
  <b-list-group>
    <VideoListItem
      v-for="(video, index) in videos"
      :key="index"
      :video="video"
    />
  </b-list-group>
</template>

<script>
import VideoListItem from '@/components/VideoListItem'

export default {
    name: 'VideoList',
    components: {
        VideoListItem,
    },
    computed: {
      videos() {
        return this.$store.state.videos
      }
    },
}
</script>

<style>

</style>