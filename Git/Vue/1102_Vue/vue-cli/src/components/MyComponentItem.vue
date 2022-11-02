<template>
  <div>
    <h3>MyComponent의 하위 컴포넌트</h3>
    <p>{{ staticProps }}</p>
    <p>{{ dynamicProps }}</p>
    <button @click="childToParent">클릭!</button>
    <br>
    <input type="text" v-model="childInputData" @keyup.enter="childInput">
  </div>
</template>

<script>

export default {
    name: 'MyComponentItem',
    props: {
        staticProps: String,
        dynamicProps: String,
    },

    data: function() {
        return {
            childInputData: null,
        }
    },
    
    methods: {
        childToParent: function() {
            this.$emit('child-to-parent', 'child data', ['1', '2'])
        },
        childInput() {
            this.$emit('child-input', this.childInputData)
            this.childInputData = ''
        }
    }
}
</script>

<style>

</style>