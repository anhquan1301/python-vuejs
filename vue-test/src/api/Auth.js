import { baseAxios } from '@/api/BaseAxios'

const login = async (data) => {
  return await baseAxios.post(`/login`, data)
}

export default {
  login
}
