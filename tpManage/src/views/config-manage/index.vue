<template>
  <tabs-menu :tab-pane-list="tabPaneList" />
</template>

<script>
import TabsMenu from '@/components/TabsMenu'
import GlobalEnv from '@/views/config-manage/env-manage'
import GlobalLabel from '@/views/config-manage/label-manage'

export default {
  name: 'Index',
  components: { TabsMenu },
  data() {
    return {
      tabPaneList: [
        {
          name: 'GlobalEnv',
          label: '环境管理',
          components: [GlobalEnv]
        },
        {
          name: 'GlobalLabel',
          label: '标签管理',
          components: [GlobalLabel]
        }
      ]
    }
  }
}
</script>

<style scoped>

</style>
