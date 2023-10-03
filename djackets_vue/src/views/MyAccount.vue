<template>
      <div class="page-category">
        <div class="columns is-multiline" >
            <div class="column is-12">
                <h1 class="title">Мой аккаунт</h1>
            </div>

            <div class="column is-12">
              
                <button @click="logout()" class="button is-danger">Выход</button>
            </div>
            
        </div>
        
    </div>
</template>
<script>
import axios from 'axios'


export default {
    name: 'MyAccount',
    
    data() {
        return {
         
            clients: []

        }
    },

    mounted() {
        document.title = "Мой аккаунт | "
        

        this.getMyOrders()
  
    },

    methods: {
        

        logout() {
            axios.defaults.headers.common['Authorization'] = ''

            localStorage.removeItem("token")
            localStorage.removeItem('username')
            localStorage.removeItem('userid')
                   
            this.$store.commit('removeToken')

            this.$router.push('/')
        },
        async getMyOrders() {
            this.$store.commit('setLodaing', true)

            await axios
                .get('/api/v1/orders/')
                .then(response => {
                    this.orders = response.data
                })
                .catch(error => {
                    console.log(error)
                })
            this.$store.commit('setLoading', false)
        }
    },
}
</script>
<style scoped>
.columns {
    margin-top: 20px;
}
</style>