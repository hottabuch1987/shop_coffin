<template>

  <div class="carousel">    
    <div class="carousel__container" ref="carouselContainer">
      <div class="carousel__item">    
        <figure class="image mb-10 animation-effect">
          <img :src="product.get_image">
        </figure>
        <!-- Контент первого товара -->
      </div>
      <div class="carousel__item">
        <figure class="image mb-10 animation-effect">
          <img :src="product.get_image2">
        </figure>
        <!-- Контент второго товара -->
      </div>
      <div class="carousel__item">
        <figure class="image mb-10 animation-effect">
          <img :src="product.get_image3">
        </figure>
        <!-- Контент третьего товара -->
      </div>

    </div>
    <div class="carousel__controls">
      <button class="carousel__prev-btn" @click="prev"><svg xmlns="http://www.w3.org/2000/svg" width="26" height="26" fill="currentColor" class="bi bi-arrow-left-circle-fill" viewBox="0 0 16 16">
        <path d="M8 0a8 8 0 1 0 0 16A8 8 0 0 0 8 0zm3.5 7.5a.5.5 0 0 1 0 1H5.707l2.147 2.146a.5.5 0 0 1-.708.708l-3-3a.5.5 0 0 1 0-.708l3-3a.5.5 0 1 1 .708.708L5.707 7.5H11.5z"/>
      </svg>
      </button>
      <button class="carousel__next-btn" @click="next"><svg xmlns="http://www.w3.org/2000/svg" width="26" height="26" fill="currentColor" class="bi bi-arrow-right-circle-fill" viewBox="0 0 16 16">
        <path d="M8 0a8 8 0 1 1 0 16A8 8 0 0 1 8 0zM4.5 7.5a.5.5 0 0 0 0 1h5.793l-2.147 2.146a.5.5 0 0 0 .708.708l3-3a.5.5 0 0 0 0-.708l-3-3a.5.5 0 1 0-.708.708L10.293 7.5H4.5z"/>
      </svg>
      </button>
                <router-link v-bind:to="product.get_absolute_url" class="button is-dark mt-4">Посмотреть</router-link>
    </div>
        <h3 class="title">{{ product.name }}</h3>
          <strong>{{ product.price }} ₽</strong>
        
        <h6>{{product.description}}</h6>
        
        
  </div>

</template>

<script>
export default {
  name: 'ProductBox',
  props: {
    product: Object
  },
  mounted() {
    this.carouselContainer = this.$refs.carouselContainer;
    this.carouselItems = this.carouselContainer.querySelectorAll('.carousel__item');

    this.currentIndex = 0;
  },
  methods: {
    prev() {
      if (this.currentIndex > 0) {
        this.currentIndex--;
        const translateX = -(this.currentIndex * this.carouselItems[0].offsetWidth);
        this.carouselContainer.style.transform = `translateX(${translateX}px)`;
      }
    },
    next() {
      if (this.currentIndex < this.carouselItems.length - 1) {
        this.currentIndex++;
        const translateX = -(this.currentIndex * this.carouselItems[0].offsetWidth);
        this.carouselContainer.style.transform = `translateX(${translateX}px)`;
      }
    }
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

.carousel {
  position: relative;
  overflow: hidden;
}

.carousel__container {
  display: flex;
  transition: transform 0.3s ease-in-out;
}

.carousel__item {
  flex: 0 0 100%;
}

.carousel__controls {
  position: absolute;
  top: 50%;
  left: 0;
  right: 0;
  text-align: center;
}

.carousel__prev-btn,
.carousel__next-btn {
  background: none;
  border: none;
  font-size: 20px;
  cursor: pointer;
  outline: none;
}

.carousel__prev-btn {
  position: absolute;
  left: 10px;
  transform: translateY(-50%);
}

.carousel__next-btn {
  position: absolute;
  right: 10px;
  transform: translateY(-50%);
}
p {
  position: absolute;
  top: 0;
  right: 2rem;
}


</style>
