<template>
  <div>
    <input type="text" v-model="todoTitle" @keyup.enter="createTodo">

  </div>
</template>

<script>
export default {
    name: 'TodoForm',
    data() {
        return {
            todoTitle: null, 
        }
    },

    methods: {
        createTodo: function() {
            this.$emit('create-todo', this.todoTitle)
            this.todoTitle = null
        }
    },
}
</script>

<style>

</style>