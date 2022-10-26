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
      path: 'base-stability',
      redirect: '/lts/base-stability/task',
      component: () => import('@/views/lts/base-stability/index'),
      name: '基础长稳',
      meta: { title: '基础长稳', roles: ['admin'], icon: 'el-icon-notebook-1' },
      children: [
        {
          path: 'task',
          component: () => import('@/views/lts/base-stability/task/index'),
          name: '测试任务',
          meta: { title: '测试任务', roles: ['admin'], icon: 'el-icon-s-platform' }
        },
        {
          path: 'report',
          component: () => import('@/views/lts/base-stability/report/index'),
          name: '历史报告',
          meta: { title: '历史报告', roles: ['admin'], icon: 'el-icon-notebook-1' }
        },
        {
          path: 'analysis',
          component: () => import('@/views/lts/video-monitor/analysis/index'),
          name: '结果分析',
          meta: { title: '结果分析', roles: ['admin'], icon: 'el-icon-data-analysis' }
        }
      ]
    },
    {
      path: 'video-monitor',
      redirect: '/lts/video-monitor/analysis',
      component: () => import('@/views/lts/video-monitor/index'),
      name: '视频监控',
      meta: { title: '视频监控', roles: ['admin'], icon: 'el-icon-data-analysis' },
      children: [
        {
          path: 'task',
          component: () => import('@/views/lts/video-monitor/task/index'),
          name: 'task',
          meta: { title: '测试任务', roles: ['admin'], icon: 'el-icon-data-analysis' }
        },
        {
          path: 'analysis',
          component: () => import('@/views/lts/video-monitor/analysis/index'),
          name: 'lts_analysis',
          meta: { title: '统计分析', roles: ['admin'], icon: 'el-icon-data-analysis' }
        }
      ]
    }
  ]
}

export default ltsRouter
