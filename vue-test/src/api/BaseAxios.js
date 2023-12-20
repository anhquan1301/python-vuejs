import axios from 'axios'

const baseDomain = 'http://localhost:7071/api'
axios.defaults.headers.common['Access-Control-Allow-Origin'] = '*'
const baseURL = `${baseDomain}`

export const baseAxios = axios.create({
  baseURL: baseURL
})

