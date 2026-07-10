import axios from 'axios'

const apiClient = axios.create({

  baseURL: 'https://jsonplaceholder.typicode.com',

  timeout: 5000,

  headers: {

    'Content-Type': 'application/json'

  }

})

apiClient.interceptors.request.use(

  config => {

    config.headers.Authorization =

      'Bearer mock-token-123'

    return config

  }

)

apiClient.interceptors.response.use(

  response => {

    return response.data

  },

  error => {

    throw {

      message:
        error.message ||

        'API Error',

      statusCode:
        error.response?.status || 500

    }

  }

)

export default apiClient