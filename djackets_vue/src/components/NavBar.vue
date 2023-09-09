<template>
<!-- navbar -->
  <nav class="navbar">
    <div class="navbar-brand">
    <div class="navbar-item">
    <div class="buttons">
      <router-link to="/" class="button is-dark">Скидки</router-link>
    </div>
    </div>
      <a class="navbar-burger" aria-label="menu" aria-expanded="false" data-target="navbar-menu" @click="showMobileMenu = !showMobileMenu">
        <span aria-hidden="true"></span>
        <span aria-hidden="true"></span>
        <span aria-hidden="true"></span>
         
      </a>
    </div>
    <div class="navbar-menu" id="navbar-menu" v-bind:class="{'is-active': showMobileMenu }" >
      <div class="navbar-item" @mouseenter="showDropdown = true" @mouseleave="showDropdown = false">
          <div class="navbar-item">Информация</div>
          <ul v-show="showDropdown" class="dropdown">
                <li><router-link to="/about" class="navbar-item">Морги </router-link></li>
                <li><router-link to="/about" class="navbar-item">Кладбища</router-link></li>
                <li><router-link to="/about" class="navbar-item">Отзывы</router-link></li>
                <li><router-link to="/about" class="navbar-item">Полезная информация</router-link></li>
          </ul>
        </div>

      <div class="navbar-end">
        <div class="navbar-item" @mouseenter="showDropdown = true" @mouseleave="showDropdown = false">
          <div class="navbar-item">Ритуальные услуги</div>

            <ul v-show="showDropdown" class="dropdown">
              <li><router-link to="/about" class="navbar-item">Документы</router-link></li>
              <li><router-link to="/about" class="navbar-item">Место на кладбище</router-link></li>
              <li><router-link to="/about" class="navbar-item">Кремация</router-link></li>
              <li><router-link to="/about" class="navbar-item">Льготы и пособия</router-link></li>
              <li><router-link to="/about" class="navbar-item">Онлайн трансляция</router-link></li>
            </ul>
        </div>
        
        <div class="navbar-item" @mouseenter="showDropdown = true" @mouseleave="showDropdown = false">
          <div class="navbar-item">Каталог товаров</div>
          <ul v-show="showDropdown" class="dropdown">
                <li><router-link to="/products/category/grobi/" class="navbar-item">Гробы</router-link></li>
                <li><router-link to="/about" class="navbar-item">Венки</router-link></li>
                <li><router-link to="/about" class="navbar-item">Кресты</router-link></li>
                <li><router-link to="/about" class="navbar-item">Композиции</router-link></li>
                <li><router-link to="/about" class="navbar-item">Корзины</router-link></li>
          </ul>
        </div>
        <!-- search -->
         
        <div class="navbar-item is-small">
          <form method="get" action="/about">
            <div class="field has-addons">
              <div class="control">
                <input type="text" class="input"  name="query">
              </div>

              <div class="control">
                <button class="button is-success">
                  <span class="icon">
                    <i class="fas fa-search"></i>
                  </span>
                </button>
              </div>
            </div>
          </form>
        </div>
      
    <!-- //search -->
        
    <!-- my-account -->
        <div class="navbar-item">
          <div class="buttons">
          <template v-if="$store.state.isAuthenticated">
            <router-link to="/my-account" class="button is-dark">Мой аккаунт</router-link>
          </template>
          <template v-else>
            <router-link to="/log-in" class="button is-dark">Войти</router-link>
            <router-link to="/sing-up" class="button is-dark">Регистрация</router-link>
   
            
          </template>

          </div>
        </div> 
      </div>

    </div>
  </nav>
</template>
<script>
import axios from 'axios'



export default {

  data(){
    return{
      showDropdown: false,
    
    }
  },

  
   methods: {
        toggleDropdown() {
          this.showDropdown = !this.showDropdown;
        },
        selectItem() {
       
          this.showDropdown = false;
        }
  },

}
</script>
<style scoped>
.navbar {
  background-color:  rgba(63, 62, 63, 0.76);
  color: #f8f5f5;
  padding: 10px;
}

.navbar-brand {
  display: flex;
  align-items: center;
}

.navbar-item {
  margin-right: 15px;
  color: #f9f5f5;
}

.navbar-item button {
  margin-right: 10px;
  border: none;
  background-color: transparent;
  color: #f9f5f5;
  cursor: pointer;
}

.navbar-burger {
  color: #faf8f8;
  cursor: pointer;
}

.navbar-end {
  display: flex;
  align-items: center;
}

.dropdown {
  display: none;
  position: absolute;
  top: 100%;
  padding: 10px;
  background-color: #898a89;
  color: #ffffff;
}

.dropdown li {
  margin-bottom: 5px;
}

.navbar-item:hover .dropdown {
  display: block;
}

.dropdown .navbar-item {
  color: #252222;
}

.dropdown .navbar-item:hover {
  text-decoration: underline;
}

.dropdown .selected {
  font-weight: bold;
}

.navbar-item.is-small {
  margin-left: auto;
}

.navbar-item.is-small .field {
  margin-bottom: 0;
}

.navbar-item.is-small .control {
  margin-right: 5px;
}

.navbar-item.is-small .input {
  height: 25px;
  font-size: 14px;
  border-color: #ffffff;
  border-radius: 3px;
  padding: 2px;
}

.navbar-item.is-small .button {
  padding: 5px;
  height: 25px;
  line-height: 15px;
  border: none;
  background-color: #ffffff;
  color: #9a9c99;
  cursor: pointer;
  border-radius: 3px;
}

.buttons {
  display: flex;
  align-items: center;
}

.buttons .button {
  margin-right: 10px;
  border: none;
  background-color: #919291;
  color: #000000;
  cursor: pointer;
  border-radius: 3px;
  padding: 5px;
}

.buttons .button:hover {
  background-color: #0f0f0e;

}



</style>