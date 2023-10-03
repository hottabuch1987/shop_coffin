<template>

<nav class="navbar is-dark is-fixed-top">
  <div class="navbar-brand">
    <router-link to="/" class="navbar-item"><strong>Главная</strong></router-link>
    <router-link to="/document" class="navbar-item"><strong>Документы</strong></router-link>
    <router-link to="/" class="navbar-item"><strong>Главная</strong></router-link>
      <a class="navbar-burger" aria-label="menu" aria-expanded="false" data-target="navbar-menu" @click="showMobileMenu = !showMobileMenu">
        <span aria-hidden="true"></span>
        <span aria-hidden="true"></span>
        <span aria-hidden="true"></span>
      </a>
    </div>
    <div class="navbar-menu" id="navbar-menu" v-bind:class="{'is-active': showMobileMenu }">
    <!-- search -->
      <div class="navbar-start">
        <div class="navbar-item is-small">
          <form method="get" action="/search">
            <div class="field has-addons">
              <div class="control">
                <input type="text" class="input" placeholder="Что Вы ищете?" name="query">
              </div>
              

              <div class="control">
                <button class="button is-info">
                  <span class="icon">
                    <i class="fas fa-search"></i>
                  </span>
                </button>
              </div>
              
            
            </div>
          </form>
        </div>
      </div>
    <!-- //search -->
      <div class="navbar-end">
        <router-link to="/" class="navbar-item">Товары</router-link>
    <!-- my-account -->
      <div class="navbar-item">
        <div class="buttons">
          <templete v-if="$store.state.isAuthenticated">
              <router-link to="/my-account" class="button is-light">Мой аккаунт</router-link>
          </templete>
          <templete v-else>
              <router-link to="/log-in" class="button is-light">Войти</router-link>
          </templete>
     <!-- cart     -->
          <router-link to="/cart" class="button is-success">
            <span class="icon"><i class="fas fa-shopping-cart"></i></span>
            <span> {{ cartTotalLength }}</span>
          </router-link>
        </div>
      </div> 
  </div>
    </div>
  </nav>
</template>
<script>

export default {

  data(){
    return{
      showDropdown: false,
      showMobileMenu: false,
      cart: {
        items: []
      }
    
    }
  },
  mounted(){
    this.cart = this.$store.state.cart
  },
  computed: {
    cartTotalLength(){
      let totalLength = 0
      
      for (let i = 0; i < this.cart.items.length; i++) {
        totalLength += this.cart.items[i].quantity
      }
      return totalLength
    }
  },

  
   methods: {
        toggleDropdown() {
          this.showDropdown = !this.showDropdown;
        },
        selectItem() {
       
          this.showDropdown = false;
        },
        
  },

}
</script>
<style scoped>

</style>