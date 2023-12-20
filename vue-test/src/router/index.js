import { createRouter, createWebHistory } from 'vue-router'

import Footer from '../views/Footer.vue'
import Header from '../views/Header.vue'
import Home from '../views/Home.vue'
import Login from '../views/Login.vue'
import Register from '../views/Register.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/login',
      component: Login
    },
    {
      path: '/register',
      component: Register
    },
    {
      path: '/',
      components: {
        default: Home,
        header: Header,
        footer: Footer
      }
    }
  ]
})

export default router
