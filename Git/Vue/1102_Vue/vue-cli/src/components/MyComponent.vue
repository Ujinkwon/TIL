<template>
  <div class="border">
    <h1>This is my component :)</h1>
    <MyComponentItem static-props="MyComponent에서 보낸 데이터"
    :dynamic-props="dynamicProps"
    @child-to-parent="parentGetEvent"
    @child-input="getDynamicData"
    />
  </div>
</template>

<script>
import MyComponentItem from '@/components/MyComponentItem'

export default {
    name: 'MyComponent',
    components: {
        MyComponentItem,
    },
    data() {
        return {
            dynamicProps: '이건 동적인 데이터!',       
        }
    },

    methods: {
        parentGetEvent: function(inputData, Data2) {
            console.log("자식 컴포넌트에서 발생한 이벤트!")
            console.log(`${inputData} ${Data2} 받음`)
        },

        getDynamicData: function(inputData) {
            console.log(`받은 데이터 : ${inputData}`)
        }
    }
}
</script>
    
<style>
    .border {
        border: solid 1px black;
    }
</style>