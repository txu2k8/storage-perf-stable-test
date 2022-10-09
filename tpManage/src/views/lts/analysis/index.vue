<template>
  <tabs-menu :tab-pane-list="tabPaneList" />
</template>

<script>
import TabsMenu from '@/components/TabsMenu'
import VideoMonitor from '@/views/lts/analysis/video-monitor'

export default {
  name: 'Index',
  components: { TabsMenu },
  data() {
    return {
      tabPaneList: [
        {
          name: 'VideoMonitor',
          label: '视频监控',
          components: [VideoMonitor]
        }
      ]
    }
  }
}
</script>

<style scoped>

</style>
