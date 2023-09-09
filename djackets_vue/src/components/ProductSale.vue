<template>

<div class="page-product">
  <div class="columns is-multiline">
    <div class="column is-9">
      <figure class="image mb-10 animation-effect">
        <img :src="product.get_image">
        {{ product.name }}
        <p><strong>Цена: {{ product.price }}</strong></p>
      </figure>
      
    </div>
  </div>
</div>

</template>

<script>
export default{
    name:'ProductSale',
    props:{
        product: Object
    }
}
</script>

<style scoped>
.animation-effect {
  transition: transform 0.2s ease;
}

.animation-effect:hover {
  transform: scale(1.1);
}

</style>