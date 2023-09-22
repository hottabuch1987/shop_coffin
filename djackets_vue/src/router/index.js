import { createRouter, createWebHistory } from 'vue-router'
import store from '../store'
import HomeView from '../views/HomeView.vue'
import SingUp from '../views/SingUp.vue'
import LogIn from '../views/LogIn.vue'
import MyAccount from '../views/MyAccount.vue'
import Success from '../views/Success.vue'
import AuthCode from '../views/AuthCode.vue'
import Category from '../views/Category.vue'
import Product from '../views/Product.vue'
import Document from '../views/Document.vue'



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
    path: '/sing-up',
    name: 'SingUp',
    component: SingUp
  },
  {
    path: '/auth-code',
    name: 'AuthCode',
    component: AuthCode
  },
  {
    path: '/log-in',
    name: 'LogIn',
    component: LogIn
  },
  {
    path: '/my-account',
    name: 'MyAccount',
    component: MyAccount,
    meta: {
      requireLogin: true
    }
  },

  
  {
    path: '/success',
    name: 'Success',
    component: Success
  },
  {
    path: '/document',
    name: 'Document',
    component: Document
  },

  {
    path: '/:category_slug/:product_slug',
    name: 'Product',
    component: Product
  },
  {
    path: '/:category_slug',
    name: 'Category',
    component: Category
  },
  
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

////
router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requireLogin) && !store.state.isAuthenticated) {
    next({name: "LogIn", query: {to: to.path} })
  } else {
    next()
  }
})
////

export default router
