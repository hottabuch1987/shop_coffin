<template>
  <div class="page-category">
    <div class="columns">
      <div class="column"> 
        <div class="heading--primary">
          <h2 class="title">Документы для умершего</h2>
          <p>Фамилия <span>{{ famyli }}</span></p>
          <p>Имя <span>{{ name }}</span></p>
          <p>Отчество <span>{{ surname }}</span></p>
          <form @submit.prevent="submitForm">
            <div class="input-container">
              <input type="text" v-model="famyli" placeholder="Введите фамилию">
              <input type="text" v-model="name" placeholder="Введите имя">
              <input type="text" v-model="surname" placeholder="Введите отчество">
              <div class="notification is-danger" v-if="errors.length">
                <p v-for="error in errors" :key="error">{{ error }}</p>
              </div>
              <button type="submit" class="btn">Сохранить</button>
            </div>
          </form>
        </div>
      </div>
      <div class="column">
       <div class="deads" v-for="deadUser in deadUsers" :key="deadUser.id">
            <p><span>{{deadUser.famyli}}</span></p>
            <p><span>{{ deadUser.name }}</span></p>
            <p><span>{{deadUser.surname }}</span></p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import { toast } from 'bulma-toast'

export default {
  data() {
    return {
      deadUsers: [],
      famyli: '',
      name: '',
      surname: '',
      errors: []
    }
  },
  mounted() {
    document.title = 'Документы для покойников'
    this.getDead() // Вызов функции для получения данных при загрузке страницы
  },
  methods: {
    async submitForm() {
      this.$store.commit('setIsLoading', true)
      const formData = {
        famyli: this.famyli,
        name: this.name,
        surname: this.surname
      }
      try {
        await axios.post('api/auth/dead/', formData)
        toast({
          message: 'Данные загружены в базу',
          type: 'is-success',
          dismissible: true,
          pauseOnHover: 2000,
          position: 'bottom-right'
        })
        this.getDead() // Вызов функции для обновления данных после успешного сохранения
      } catch (error) {
        console.log('error', error)
      } finally {
        this.$store.commit('setIsLoading', false)
      }
    },
    async getDead() {
      this.$store.commit('setIsLoading', true)
      try {
        const response = await axios.get('api/auth/userdead')
        this.deadUsers = response.data
      } catch (error) {
        console.log(error)
      } finally {
        this.$store.commit('setIsLoading', false)
      }
    }
  }
}
</script>


<style scoped>
.page-category {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
}

.columns {
    margin-top: 20px;
}

.column {
    display: flex;
    justify-content: center;
    align-items: center;
}
.title {
    display: flex;
    justify-content: center;


}

.input-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    margin-top: 20px;
}

input[type="text"] {
    width: 300px;
    height: 40px;
    padding: 5px;
    border-radius: 5px;
    border: 1px solid rgb(165, 167, 167);
    margin-bottom: 10px;
}

.btn {
    display: inline-block;
    background-color: rgb(0, 123, 255);
    color: white;
    padding: 4px 2px;
    border-radius: 5px;
    text-decoration: none;
    font-size: 25px;
}

.btn:hover {
    background-color: rgb(0, 92, 191);
}

.heading--primary {
    background-color: rgb(226, 226, 223);
    padding: 10px;
    border-radius: 5px;
    margin-bottom: 20px;
}

p {
    color: rgb(165, 167, 167);
    font-size: 18px;
    margin-bottom: 5px;
}

span {
    color: rgb(88, 87, 87);
    padding-left: 40px;
}
</style>
