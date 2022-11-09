<template>
  <div>
    <h1>Dog Img</h1>
    <p v-if="!imgSrc">{{ message }}</p>
    <img v-if="imgSrc" :src="imgSrc" alt="">
  </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'DogView',
    data() {
        return {
            imgSrc: null,
            message: '로딩 중 ...'
        }
    },

    methods: {
        getDogImg() {
            const breed = this.$route.params.breed
            const dogImgSearchURL = `https://dog.ceo/api/breed/${breed}/images/random`
            axios({
                method: 'get',
                url: dogImgSearchURL
            })
                .then((response) => {
                    const imgSrc = response.data.message
                    this.imgSrc = imgSrc
                })
                .catch((error) => {
                    // this.message = `${breed}는 없는 품종입니다.`
                    this.$router.push('/404')
                    console.log(error)
                })
        },
    },
    created() {
            this.getDogImg()
        }
}
</script>

<style>

</style>