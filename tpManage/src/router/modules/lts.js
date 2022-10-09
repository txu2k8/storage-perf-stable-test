/** When your routing table is too long, you can split it into small modules **/

import Layout from '@/layout'

const ltsRouter = {
  path: '/lts',
  component: Layout,
  redirect: 'noRedirect',
  name: 'lts',
  meta: {
    title: '长稳测试',
    roles: ['admin'],
    icon: 'tree-table'
  },
  children: [
    {
      path: 'task',
      component: () => import('@/views/lts/task/index'),
      name: 'lts_task',
      meta: { title: '测试任务', roles: ['admin'], icon: 'el-icon-s-platform' }
    },
    {
      path: 'report',
      component: () => import('@/views/lts/report/index'),
      name: 'lts_report',
      meta: { title: '历史报告', roles: ['admin'], icon: 'el-icon-notebook-1' }
    },
    {
      path: 'analysis',
      component: () => import('@/views/lts/analysis/index'),
      name: 'lts_analysis',
      meta: { title: '结果分析', roles: ['admin'], icon: 'el-icon-data-analysis' }
    }
  ]
}

export default ltsRouter
