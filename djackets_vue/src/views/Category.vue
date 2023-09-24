<template>


  <div class="page-category">

    <div class="columns is-multiline">
      <div class="cards column is-half" v-for="product in category.products" :key="product.id">
        <div class="card">
          <div class="carousel">
            <div class="carousel__container" ref="carouselContainer">
              <div class="carousel__item" :class="{'active': product.figure === 1}">
                <figure class="image mb-10 animation-effect">
                  <img :src="product.get_image">
                </figure>
             
              </div>
            </div>
         
          </div>
          <router-link v-bind:to="product.get_absolute_url" class="button is-dark mt-4">Посмотреть</router-link>
          <h3 class="title">{{ product.name }}</h3>
          <strong>{{ product.price }} ₽</strong>
          <h6>{{ product.description }}</h6>
        </div>
      </div>
    </div>
  </div>
</template>



<script>
import axios from 'axios'

import ProductBox from '@/components/ProductBox'

export default {
  name: 'Category',
  components: { ProductBox },
  data() {
    return {
      category: {
        products: []
      }
    }
  },
  mounted() {
    this.getCategory()
  },
  watch: {
    $route(to, from) {
      if (to.name === 'Category') {
        this.getCategory()
      }
    }
  },

  methods: {
    async getCategory() {
      const categorySlug = this.$route.params.category_slug

      this.$store.commit('setIsLoading', true)

      axios
        .get(`/api/products/${categorySlug}/`)
        .then(response => {
          this.category = response.data

          document.title = this.category.name + ' | VIP'
        })
        .catch(error => {
          console.log(error)
        })
        this.$store.commit('setIsLoading', false)
    },
   
  }
}
</script>

<style scoped>
.animation-effect {
  transition: transform 0.3s ease;
}

.animation-effect:hover {
  transform: scale(1.2);
}

.button.is-dark {
  background-color: #28316d;
  color: #fff;
  padding: 10px 20px;
  border-radius: 5px;
  transition: background-color 0.3s ease, color 0.3s ease;
}

.button.is-dark:hover {
  background-color: #5c5a5b;
  color: #000;
}


.title {
  margin-top: 20px;
}

strong {
  margin-top: 5px;
}

h6 {
  margin-top: 10px;
}

.cards {
  display: flex;
  flex-wrap: wrap;
}
</style>
