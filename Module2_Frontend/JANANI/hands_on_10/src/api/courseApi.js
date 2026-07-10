import apiClient from './apiClient'

export async function getAllCourses() {

  return await apiClient.get('/posts')

}

export async function getCourseById(id) {

  return await apiClient.get(

    `/posts/${id}`

  )

}

export async function enrollStudent(

  studentId,
  courseId

) {

  return await apiClient.post(

    '/posts',

    {

      studentId,
      courseId

    }

  )

}