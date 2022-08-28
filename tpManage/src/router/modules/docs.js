/** When your routing table is too long, you can split it into small modules **/

import Layout from '@/layout'

const docsRouter = {
  path: '/docs',
  component: Layout,
  redirect: 'noRedirect',
  name: 'docs',
  meta: {
    title: '文档',
    roles: ['admin'],
    icon: 'component'
  }
}

export default docsRouter
