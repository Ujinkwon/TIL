import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
import HelloView from '@/views/HelloView.vue'
import LoginView from '@/views/LoginView'
import NotFound404 from '@/views/NotFound404'
import DogView from '@/views/DogView'

Vue.use(VueRouter)

const isLoggedIn = true

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  },
  {
    path: '/hello/:userName',
    name: 'hello',
    component: HelloView
  },
  // 전역가드
  // {
  //   path: '/login',
  //   name: 'login',
  //   component: LoginView

  // }

  // 라우터 가드
  {
    path: '/login',
    name: 'login',
    component: LoginView,
    beforeEnter(to, from, next) {
      if (isLoggedIn === true) {
        console.log('이미 로그인함')
        next({name: 'home'})
      }
      else {
        next()
      }
    }
  },

  {
    path: '/dog/:breed',
    name: 'dog',
    component: DogView
  },


  {
    path: '/404',
    name: 'NotFound404',
    component: NotFound404
  },



  // 요청한 리소스가 존재하지 않는 경우
  // 404 page로 redirect 시키기
  // 이때, routes 최하단부에 작성
  {
    path: '*',
    redirect: '/404'
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

// 전역가드
// 비로그인 상태에서 로그인이 필요한 페이지로 접근시
// 해당 페이지를 렌더링 하지 않고 Login 페이지로 이동
// router.beforeEach((to, from, next) => {
//   // 로그인 여부
//   const isLoggedIn = true
//   // 로그인에 필요한 페이지
//   const authPages = ['hello', 'home', 'about']
//   // 앞으로 이동할 페이지(to)가
//   // 로그인이 필요한 사이트인지 확인
//   const isAuthRequired = authPages.includes(to.name)

//   // const allowAllPages = ['login']
//   // const isAuthRequired = !allowAllPages.includes(to.name)

//   if (isAuthRequired && !isLoggedIn) {
//     console.log('Login으로 이동!')
//     next({ name: 'login' })
//   }
//   else {
//     // 기존 루트로 이동
//     console.log('to로 이동!')
//     next()
//   }
// })

export default router
