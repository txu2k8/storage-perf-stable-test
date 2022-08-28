/** When your routing table is too long, you can split it into small modules **/

import Layout from '@/layout'

const perfRouter = {
  path: '/perf',
  component: Layout,
  redirect: 'noRedirect',
  name: 'perf',
  meta: {
    title: '性能测试',
    icon: 'el-icon-s-data'
  },
  children: [
    {
      path: 'task',
      component: () => import('@/views/form/index'),
      name: 'perf_task',
      meta: { title: '测试任务', icon: 'el-icon-s-platform' }
    },
    {
      path: 'report',
      component: () => import('@/views/form/index'),
      name: 'perf_report',
      meta: { title: '历史报告', icon: 'el-icon-notebook-1' }
    }
  ]
}

export default perfRouter
