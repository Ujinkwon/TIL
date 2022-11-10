<template>
  <div id="app">
    <!-- <img alt="Vue logo" src="./assets/logo.png">
    <HelloWorld msg="Welcome to Your Vue.js App"/> -->

    <div id="container">
      <h1 class="style-1 fs-1">Ujin's First Youtube Project</h1>
    </div>
    <TheSearchBar @get-list="searchList"/>
    <VideoDetail/>
    <VideoList/>
  </div>
</template>

<script>
import VideoList from '@/components/VideoList'
import TheSearchBar from '@/components/TheSearchBar'
import VideoDetail from '@/components/VideoDetail'
import axios from 'axios'

export default {
  name: 'App',
  components: {
    VideoList,
    TheSearchBar,
    VideoDetail,
  },
  computed: {
    },
  methods: {
    searchList(inputData) {
      const searchURL = `https://www.googleapis.com/youtube/v3/search?key=AIzaSyDk_3SXDsMx_lvi2GTqVAFMuwhjBexOE8U&part=snippet&type=video&q=${inputData}`
      axios({
        method: 'get',
        url: searchURL
      })
        .then((response) => {
          console.log(response.data)
          this.$store.dispatch('searchList', response.data.items)
        })
        .catch((error) => {
          console.log(error)
        })
    },

  },

}
</script>

<style>
@import url(https://fonts.googleapis.com/css?family=Pacifico);


#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

#container {
  margin: 0 auto;
  max-width: 520px;
  text-align: center;
}

#container h1 {
  font-weight: normal;
  text-transform: uppercase;
  margin: 0.3125em 0;
  background-color: white;
  position: relative;
  display: inline-block;
  padding: 0 10px;
}

.style-1 {
  font-family: "Pacifico", sans-serif;
  text-transform: none!important;
}
.style-1:before {
  content: "";
  border-top: 1px solid black;
  position: absolute;
  width: 300%;
  top: 35%;
  left: -100%;
  z-index: -999;
}

.style-1:after {
  content: "";
  border-bottom: 1px solid black;
  position: absolute;
  width: 300%;
  bottom: 35%;
  left: -100%;
  z-index: -999;
}

</style>
