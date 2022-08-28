import request from '@/utils/request'

export function login(data) {
  return request({
    url: '/api/base/jwt/token/v2',
    method: 'post',
    data
  })
}

export function getInfo(token) {
  return request({
    url: '/api/base/jwt/token/info',
    method: 'get',
    params: { token }
  })
}

export function logout() {
  return request({
    url: '/api/base/jwt/user/logout',
    method: 'post'
  })
}
