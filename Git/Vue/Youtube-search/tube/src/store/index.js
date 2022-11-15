import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    videos: null,
    detail: null,
  },
  getters: {
  },
  mutations: {
    SEARCH_LIST(state, arr) {
      state.videos = arr
    },
    VIDEO_DETAIL(state, video) {
      state.detail = video
    },
    IN_TEXT(state) {
      state.detail = null
    }
  },
  actions: {
    searchList(context, arr) {
      context.commit('SEARCH_LIST', arr)
    },
    videoDetail(context, video) {
      context.commit('VIDEO_DETAIL', video)
    },
    inText(context) {
      context.commit('IN_TEXT')
    }
  },
  modules: {
  }
})
