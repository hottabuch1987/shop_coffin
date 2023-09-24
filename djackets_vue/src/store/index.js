import { createStore } from 'vuex'

export default createStore({
  state: {
    cart: {
      items: []
    },
    
    isAuthenticated: false,
    auth_code: '',
    isLoading: false
  },
  mutations: {
    initializeStore(state){
      if (localStorage.getItem('cart')){
        state.cart = JSON.parse(localStorage.getItem('cart'))
      } else{
        localStorage.setItem('cart', JSON.stringify(state.cart))
      }
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
    addToCart(state, item) {
      const exists = state.cart.items.filter(i => i.product.id === item.product.id)
      if (exists.length){
        exists[0].quantity = parseInt(exists[0].quantity) + parseInt(item.quantity)
      }else{
        state.cart.items.push(item)
      }
      localStorage.setItem('cart', JSON.stringify(state.cart))
    },
    clearCart(state) {
      state.cart = { items: [] }
      localStorage.setItem('cart', JSON.stringify(state.cart))
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
