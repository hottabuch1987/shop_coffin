<template>
  <div class="page-product">
      <div class="columns is-multiline">
          <div class="column is-9">
              <figure class="image mb-6">
                  <img :src="product.get_image">
              </figure>
              <h1 class="title">Телефон {{ product.name }}</h1>
              <p>{{ product.description }}</p>
          </div>
          <div class="column is-3">
              <h2 clas="subtitle">Описание</h2>
              <p><strong>Цена: </strong> {{ product.name }}</p>
          <div class="field has-addons mt-6">
             
          <div class="control">
           
          </div>
          </div>
          </div>
      </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'Product',
    data(){
        return {
            product: {},
            quantity: 1
        }
    },
    mounted(){
        this.getProduct()
    },
    methods: {
        async getProduct() {

            this.$store.commit('setIsLoading', true)

            const category_slug = this.$route.params.category_slug
            const product_slug = this.$route.params.product_slug

            await axios
                .get(`/api/products/${category_slug}/${product_slug}`)
                .then(response => {
                    this.product = response.data

                    document.title = this.product.name + ' | VIP гробы'                })
                .catch(error =>{
                    console.log(error)
                })
            this.$store.commit('setIsLoading', false)
        },
     
    }
}
</script>