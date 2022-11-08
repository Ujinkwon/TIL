import Vue from 'vue'
import Vuex from 'vuex'
import createPersistedState from 'vuex-persistedstate'

Vue.use(Vuex)

export default new Vuex.Store({
  plugins: [
    createPersistedState(),
  ],
  state: {
    orderList: [],
    menuList: [
      {
        title: '아메리카노',
        price: 3000,
        selected: false,
        image: 'https://source.unsplash.com/featured/?americano'
      },
      {
        title: '라떼',
        price: 4500,
        selected: false,
        image: 'https://source.unsplash.com/featured/?latte'
      },
      {
        title: '아이스티',
        price: 2000,
        selected: false,
        image: 'https://source.unsplash.com/featured/?icetea'
      },
      
    ],
    sizeList: [
      {
        name: 'small',
        price: 500,
        selected: false,
      },
      {
        name: 'medium',
        price: 700,
        selected: false,
      },
      {
        name: 'large',
        price: 1000,
        selected: false,
      },
    ],
    optionList: [
      {
        type: '샷',
        price: 500,
        count: 0,
      },
      {
        type: '바닐라 시럽',
        price: 700,
        count: 0,
      },
      {
        type: '카라멜 시럽',
        price: 700,
        count: 0,
      }
    ]
  },
  getters: {
  },
  mutations: {
    addOrder(state) {
      const menuS = state.menuList.find((menu) => {
        return menu.selected
      })
      const sizeS = state.sizeList.find((size) => {
        return size.selected
      })
      const optionS = state.optionList.map((option) => {
        const opt = {...option}
        return opt
      })

      const order = {
        menu: menuS,
        size: sizeS,
        option: optionS
      }
      state.orderList.push(order)
    },
    updateMenuList(state, selectedMenu) {
      state.menuList = state.menuList.map((menu) => {
        if (menu.title === selectedMenu.title) {
          menu.selected = true
        }
        else {
          menu.selected = false
        }
        return menu
      })
    },
    updateSizeList(state, selectedSize) {
      state.sizeList = state.sizeList.map((size) => {
        if (size.name === selectedSize.name) {
          size.selected = true
        }
        else {
          size.selected = false
        }
        return size
      })
    },
    updateOptionList(state, newOption) {
      state.optionList = state.optionList.map((option) => {
        if (option.type === newOption.type) {
          option.count = newOption.count
        }
        return option
      })
    },
    ORDER_FINISH(state) {
      state.orderList.splice(0, state.orderList.length)
    },
  },
  actions: {
    selectMenu(context, menu) {
      context.commit('updateMenuList', menu)
    },
    selectSize(context, size) {
      context.commit('updateSizeList', size)
    },
    order(context) {
      context.commit('addOrder')
    },

    increase(context, option) {
      option.count += 1
      context.commit('updateOptionList', option)
    },
    decrease(context, option) {
      if (option.count > 0) {
        option.count -= 1
      }
      context.commit('updateOptionList', option)
    },
    orderFinish(context) {
      context.commit('ORDER_FINISH')
    },
  },
  modules: {
  }
})