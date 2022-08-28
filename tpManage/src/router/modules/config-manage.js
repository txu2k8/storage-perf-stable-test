/** When your routing table is too long, you can split it into small modules **/

import Layout from '@/layout'

const configManageRouter = {
  path: '/config-manage',
  component: Layout,
  redirect: 'noRedirect',
  name: 'config-manage',
  meta: {
    title: '配置管理',
    roles: ['admin'],
    icon: 'el-icon-setting'
  },
  children: [
    {
      path: 'env-manage',
      component: () => import('@/views/config-manage/env-manage'),
      name: 'env-manage',
      meta: { title: '环境管理', roles: ['admin'], icon: 'el-icon-setting' }
    },
    {
      path: 'label-manage',
      component: () => import('@/views/config-manage/label-manage'),
      name: 'label-manage',
      meta: { title: '标签管理', roles: ['admin'], icon: 'el-icon-setting' }
    },
    {
      path: 'workflow-manage',
      component: () => import('@/views/config-manage/workflow-manage'),
      name: 'workflow-manage',
      meta: { title: '工作流管理', roles: ['admin'], icon: 'el-icon-setting' }
    }
  ]
}

export default configManageRouter
