import Vue from 'vue'
import App from './App.vue'
import VueRouter from "vue-router"
import axios from 'axios'
import VueAxios from 'vue-axios'
import BootstrapVue from "bootstrap-vue"

import Loan from './components/Loan.vue'
import ApplyLoan from './components/ApplyLoan.vue'
import EditLoan from './components/EditLoan.vue'
import Home from './components/Home.vue'
import Register from './components/Register.vue'
import Login from './components/Login.vue'
import Vuelidate from 'vuelidate';
import AccountDetails from './components/AccountDetails'
import UpdateDetails from './components/UpdateDetails'

// Vue.config.productionTip = false
Vue.config.silent = true
Vue.use(BootstrapVue)
Vue.use(VueAxios, axios)
Vue.use(VueRouter)
Vue.use(Vuelidate)


const spaRoutes = new VueRouter({
  routes: [
    {
      path: '/',
      component: Home
    },
    {
      path: '/show-loans/:username',
      component: Loan
    },
    {
      path: '/add-loan/:username',
      component: ApplyLoan
    },
    {
      path: '/edit-loan/:username',
      component: EditLoan
    },
    {
      path: '/register',
      component: Register
    },
    {
      path: '/login',
      component: Login
    },
    {

      path: '/AccountDetails/:username',

      name: 'AccountDetails',

      component: AccountDetails

    },

    {

      path: '/UpdateDetails/:username',

      name: 'UpdateDetails',

      component: UpdateDetails

    }
  ],
  mode: 'history'
})

new Vue({
  router: spaRoutes,
  render: h => h(App),
}).$mount('#app')
