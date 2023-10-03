<template>
    <div class="page-cart">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Корзина</h1>
            </div>

            <div class="column is-12 box">
                <table class="table is-fullwidth" v-if="cartTotalLength">
                    <thead>
                        <tr>
                            <th>Продукт</th>
                            <th>Цена</th>
                            <th>Количество</th>
                            <th>Общая</th>
                            <th></th>
                        </tr>
                    </thead>

                    <tbody>
                        <CartItem
                            v-for="item in cart.items"
                            v-bind:key="item.product.id"
                            v-bind:initialItem="item"
                            v-on:removeFromCart="removeFromCart"
                        />
                    </tbody>
                </table>

                <p v-else>У вас нет товаров в корзине...</p>
            </div>

            <div class="column is-12 box">
                <h2 class="subtitle">Продукты</h2>

                <strong>{{ cartTotalPrice.toFixed(2) }} ₽</strong>, количество: {{ cartTotalLength }} 

                <hr>

                <router-link to="/order" class="button is-dark">Перейти к оформлению заказа(cтраница)</router-link>
                <div>
                      <button class="button is-dark mt-3" @click="showModal = true">Перейти к оформлению заказа(модалка)</button>
                       <div v-if="showModal" class="modal" @click.self="showModal = false">
                               <div class="modal-content">
                                
                       <span class="close" @click="showModal = false">&times;</span>
                       <form class="modal-form">
                        <h2 class="modal-subtitle">Оформление Вашего заказа</h2>
                        <label class="modal-label">Имя</label>
                        <input class="form-input" type="text" placeholder="Введите Ваше имя">
                        <label class="modal-label">Адрес электронной почты</label>
                        <input class="form-input" type="email" placeholder="Введите Ваш email">
                        <label class="modal-label">Телефон</label>
                        <input class="form-input" type="text" placeholder="+7 (000) 000-00-00">
                        <label class="modal-label">Адрес доставки</label>
                        <input class="form-input" type="textarea" placeholder="Город, улица, дом">
                        <button class="button is-dark mt-3">Отправить</button>
                       </form>
                               </div>
                       </div>
               </div>
            </div>
        </div>
    </div>
</template>

<script>

import CartItem from '@/components/CartItem.vue'
export default {
    name: 'Cart',
    components: {
        CartItem
    },
    data() {
        return {
            showModal: false,
            cart: {
                items: []
            }
        }
    },
        
    
    mounted() {
        this.cart = this.$store.state.cart    
    },
    methods: {
        removeFromCart(item) {
            this.cart.items = this.cart.items.filter(i => i.product.id !== item.product.id)
        }
    },
  
    computed: {
        cartTotalLength() {
            return this.cart.items.reduce((acc, curVal) => {
                return acc += curVal.quantity
            }, 0)
        },
        cartTotalPrice() {
            return this.cart.items.reduce((acc, curVal) => {
                return acc += curVal.product.price * curVal.quantity
            }, 0)
        },
    }
}
</script>

<style scoped>

/* Стили для модального окна */
.modal {
  display: block;
  position: fixed;
  z-index: 1;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  overflow: auto;
  background-color: rgba(0, 0, 0, 0.4);
}
.modal-form {
    display: flex;
    flex-direction: column;
}
.modal-content {
    display: flex;
    flex-direction: column-reverse;
    align-items: center;
    justify-content: space-between;
  background-color: #fefefe;
  margin: 15% auto;
  padding: 20px;
  border: 1px solid #888;
  width: 80%;
}
.modal-subtitle {
    font-size: 40px;
    color: #7d7c7c;
}

.modal-label {
    font-size: 20px;
    color: #888;
    margin-top: 10px;
}
.form-input{
    height: 40px;
    font-size: 20px;
}
.close {
  color: #f80303bf;
  float: right;
  font-size: 28px;
  font-weight: bold;
}

.close:hover,
.close:focus {
  color: black;
  text-decoration: none;
  cursor: pointer;
}
</style>