<template>
<div id="wrapper" :class="selectedItem">
<!-- navbar -->
<NavBar />
<!-- spiner -->
  <div class="is-loading-bar has-text-centered" v-bind:class="{'is-loading': $store.state.isLoading}">
    <div class="lds-dual-ring"></div>
  </div>
<!-- section -->
  <section class="section">
    <router-view />
  </section>
<Footer />
  

<!--  -->
</div>
</template>

<script>
import axios from 'axios'
import NavBar from '@/components/NavBar'
import Footer from '@/components/Footer'


export default {
  components: { Footer, NavBar },
  data(){
    return{
      showMobileMenu: false,
      showDropdown: false,
      selectedItem: ''

    }
  },

  
  beforeCreate(){
    this.$store.commit('initializeStore')

    // 
    const token = this.$store.state.token
    
    if (token) {
      axios.defaults.headers.common['Authorization'] = 'Token' + token
    } else {
      axios.defaults.headers.common['Authorization'] = ''
    }
  },
   methods: {
        toggleDropdown() {
          this.showDropdown = !this.showDropdown;
        },
        selectItem(item) {
          this.selectedItem = item;
          this.showDropdown = false;
        }
  },

}
</script>
<style lang="scss">

@charset "utf-8";
@import "../node_modules/bulma/bulma.sass";

// spinner
.lds-dual-ring {
  display: inline-block;
  width: 80px;
  height: 80px;
}
.lds-dual-ring:after {
  content: " ";
  display: block;
  width: 64px;
  height: 64px;
  margin: 8px;
  border-radius: 50%;
  border: 6px solid #ccc;
  border-color: #ccc transparent #ccc transparent;
  animation: lds-dual-ring 1.2s linear infinite;
}
@keyframes lds-dual-ring {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}
.is-loading-bar {
  height: 0;
  overflow: hidden;
  -webkit-transition: all 0.5s;
  transition: all 0.5s;

  &.is-loading {
    height: 80px;
  }
}

.input::placeholder {
  color: rgb(88, 92, 90);
  font-size: 1.2em;
  
}
.textarea::placeholder {
  color: rgb(88, 92, 90);
  font-size: 1.2em;
  
}

</style>
