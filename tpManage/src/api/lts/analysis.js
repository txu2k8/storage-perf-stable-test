import request from '@/utils/request'

// 获取ObjInfo列表
export function getObjInfoList(params) {
  return request({
    url: '/api/lts/analysis/obj/list',
    method: 'get',
    params: params
  })
}

// 获取ObjInfo详情
export function getObjInfoDetail(pk, params) {
  return request({
    url: '/api/lts/analysis/obj/detail/' + pk + '/',
    method: 'get',
    params
  })
}

// 获取 DB列表
export function getDBList(params) {
  return request({
    url: '/api/lts/analysis/db/list',
    method: 'get',
    params
  })
}
