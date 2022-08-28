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
      component: () => import('@/views/form/index'),
      name: 'lts_task',
      meta: { title: '测试任务', roles: ['admin'], icon: 'el-icon-s-platform' }
    },
    {
      path: 'report',
      component: () => import('@/views/form/index'),
      name: 'lts_report',
      meta: { title: '历史报告', roles: ['admin'], icon: 'el-icon-notebook-1' }
    }
  ]
}

export default ltsRouter
