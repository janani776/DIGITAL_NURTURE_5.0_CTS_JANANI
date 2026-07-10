import { defineStore } from 'pinia'

import {

  ref,
  computed

} from 'vue'

import {

  getCourseById

} from '../api/courseApi'

export const useEnrollmentStore = defineStore(

  'enrollment',

  () => {

    const enrolledCourses = ref([])

    const totalCredits = computed(() => {

      return enrolledCourses.value.length

    })

    function enroll(course) {

      enrolledCourses.value.push(course)

    }

    function unenroll(courseId) {

      enrolledCourses.value =

        enrolledCourses.value.filter(

          course =>

            course.id !== courseId

        )

    }

    async function fetchAndEnroll(

      courseId

    ) {

      try {

        const course =

          await getCourseById(

            courseId

          )

        enrolledCourses.value.push(

          course

        )

      }

      catch(error) {

        console.log(error)

      }

    }

    function $reset() {

      enrolledCourses.value = []

    }

    return {

      enrolledCourses,
      totalCredits,
      enroll,
      unenroll,
      fetchAndEnroll,
      $reset

    }

  }

)