import { createStore } from 'vuex'

export default createStore({
  state: {
    
    isAuthenticated: false,
    auth_code: '',
    isLoading: false
  },
  mutations: {
    initializeStore(state){
      // if (localStorage.getItem('cart')){
      //   state.cart = JSON.parse(localStorage.getItem('cart'))
      // } else{
      //   localStorage.setItem('cart', JSON.stringify(state.cart))
      // }
      // Authenticated
      if (localStorage.getItem('auth_code')) {
        state.auth_code = localStorage.getItem('auth_code')
        state.isAuthenticated = true
      } else {
        state.auth_code = ''
        state.isAuthenticated = false
      }
      // //Authenticated
    },

   
    setIsLoading(state, status) {
      state.isLoading = status
    },
    // Authenticated token
    setToken(state, auth_code) {
      state.auth_code = auth_code
      state.isAuthenticated = true
    },
    removeToken(state) {
      state.auth_code = ''
      state.isAuthenticated = false
    },
    // //Authenticated token
   
  },
  actions: {
  },
  modules: {
  }
})
