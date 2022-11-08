<template>
  <div>
    <h2 class="pb-2">3. 옵션을 고르세요.</h2>
    <ul class="option-list">
      <OptionListItem
        v-for="(option, index) in optionList"
        :key="index"
        :option="option"
        class="d-flex justify-content-between d-grid gap-2 col-10 mx-auto"
      />
    </ul>
  </div>
</template>

<script>
import OptionListItem from '@/components/OptionListItem'

export default {
  name: 'OptionList',
  components: {
    OptionListItem,
  },
  computed: {
    optionList() {
      return this.$store.state.optionList
    },
  },
}
</script>

<style>
</style>