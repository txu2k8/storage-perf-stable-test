import request from '@/utils/request'

// 获取项目列表
export function getProjectList(params) {
  return request({
    url: '/api/base/project/list/',
    method: 'get',
    params
  })
}

// 获取项目详情
export function getProjectDetail(pk, params) {
  return request({
    url: '/api/base/project/detail/' + pk + '/',
    method: 'get',
    params
  })
}

// 新增项目
export function addProject(data) {
  return request({
    url: '/api/base/project/add/',
    method: 'post',
    data: data
  })
}

// 局部更新项目
export function updateProject(pk, data) {
  return request({
    url: '/api/base/project/update/' + pk + '/',
    method: 'patch',
    data
  })
}

// 批量 局部更新项目
export function bulkUpdateProject(dataArr) {
  return request({
    url: '/api/base/project/bulk/',
    method: 'patch',
    data: dataArr
  })
}

// 删除项目
export function deleteProject(pk) {
  return request({
    url: '/api/base/project/del/' + pk + '/',
    method: 'delete'
  })
}

// 批量 删除项目
export function bulkDeleteProject(params) {
  return request({
    url: '/api/base/project/bulk/',
    method: 'delete',
    params
  })
}
