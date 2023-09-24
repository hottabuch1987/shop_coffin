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

                <router-link to="/about" class="button is-dark">Перейти к оформлению заказа</router-link>
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