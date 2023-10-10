<template>
  <div class="page-category">
    <div class="columns">
      <div class="column">
        <h2 class="title">Товары со скидкой!</h2>
        <section class="hero is-medium " style="height: 840px; overflow-y: scroll;">

            <ul class="subtitle m-4">
              
               <ProductSale
                v-for="product in latestProducts"
                v-bind:key="product.id"
                v-bind:product="product"
            />

                
            </ul>

        </section>
      </div>
      <div class="column">
        <section class="hero is-medium  mb-2 is-wider">
          

            <ProductBox 
                v-for="product in latestProducts"
                v-bind:key="product.id"
                v-bind:product="product"
            />
         
        </section>
      </div>
      
    </div>
  </div>




</template>

<script>
import axios from 'axios'
import ProductBox from '@/components/ProductBox'
import ProductSale from '@/components/ProductSale'


export default {
  name: 'HomeView',
  components: { ProductBox, ProductSale},
 
  data() {
    return {
        latestProducts: []
    }
  },
  mounted() {
    this.getLatestProducts()

    document.title =  'Главная | VIP гробы'   
  },
  methods: {
    async getLatestProducts(){
        this.$store.commit('setIsLoading', true)
        
        await axios
            .get('/api/products/latest-products/')
            .then(response => {
                this.latestProducts = response.data
            })
            .catch(error =>{
                console.log(error)
            })
        this.$store.commit('setIsLoading', false)
    }
  },
  

}
</script>
<style scoped>

section {
  border-radius: 1em/1em;

}


.is-wider {
  
    width: 40rem;
}
.small {
  font-size: 0.9rem;
  margin: 2rem;
  list-style-type: disc;
  
}
.columns {
    margin-top: 20px;
}
</style>


