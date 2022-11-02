<template>
  <div id="app">
    <TodoForm @create-todo="addTodo"/>
    <TodoList :todos="todos" @delete-todo="deleteTodo"/>
  </div>
</template>

<script>
import TodoForm from '@/components/TodoForm'
import TodoList from '@/components/TodoList'

export default {
  name: 'App',
  components: {
    TodoForm,
    TodoList,
  },
  data: function() {
    return {
      todos: []
    }
  },

  methods: {
    addTodo: function(inputData) {
      const todo ={
        title: inputData
      }
      this.todos.push(todo)
    },

    deleteTodo: function(todo) {
      const index = this.todos.indexOf(todo)
      // 해당 인덱스 삭제하고 새배열 만들어주는 메서드
      this.todos.splice(index, 1)
    }
  }
}
</script>

<style>
/* #app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
} */
</style>
