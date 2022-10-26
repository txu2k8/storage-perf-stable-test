<template>
  <tabs-menu :tab-pane-list="tabPaneList" />
</template>

<script>
import TabsMenu from '@/components/TabsMenu/index'
import ObjInfo from '@/views/lts/video-monitor/analysis/obj-info'
import StatInfo from '@/views/lts/video-monitor/analysis/stat-info'

export default {
  name: 'Index',
  components: { TabsMenu },
  data() {
    return {
      tabPaneList: [
        {
          name: 'StatInfo',
          label: '统计数据',
          components: [StatInfo]
        },
        {
          name: 'ObjInfo',
          label: '对象信息',
          components: [ObjInfo]
        }
      ]
    }
  }
}
</script>

<style scoped>

</style>
