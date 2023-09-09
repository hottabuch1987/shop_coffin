<template>
    <div class="select is-success" @click="arOptionsVisible = !arOptionsVisible">{{movie}}
        <select v-if="arOptionsVisible">
            <option v-for="option in options" :key="option.value" @click="selectOption(option)">{{option.name}}</option>
        </select>
      
    </div>

</template>
<script>
export default {
    name: 'Select',
    props: {
        options: {
            type: Array,
            default () {
                return []
            }
        },
         movie: {
            type: Number,
            default: 0
         },

    },
    data(){
        return {
            arOptionsVisible: false
        }
    },
    methods: {
        selectOption(option){
            this.$emit("select", option )
            this.arOptionsVisible = false    
        },
        hideSelect() {
            this.arOptionsVisible = false
        }
    },
    mounted() {
        document.addEventListener('click', this.hideSelect.bind(this), true)

    },
    beforeDestroy() {
        document.removeEventListener('click', this.hideSelect)
    },
}
</script>

<style scoped>

</style>