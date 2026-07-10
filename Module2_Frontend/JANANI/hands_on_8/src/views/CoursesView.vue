<template>

  <div>

    <h1>Courses</h1>

    <input
      type="text"
      placeholder="Search Course"
      v-model="searchTerm"
    />

    <div
      v-for="course in filteredCourses"
      :key="course.id"
    >

      <RouterLink :to="'/courses/' + course.id">

        <CourseCard
          :name="course.name"
          :code="course.code"
          :credits="course.credits"
          :grade="course.grade"
        />

      </RouterLink>

      <button @click="store.enroll(course)">

        Enroll

      </button>

    </div>

  </div>

</template>

<script setup>

import {
  ref,
  onMounted,
  computed
} from 'vue'

import CourseCard from '../components/CourseCard.vue'

import { useEnrollmentStore }
from '../stores/enrollment'

const store = useEnrollmentStore()

const courses = ref([])

const searchTerm = ref('')

onMounted(() => {

  courses.value = [

    {
      id: 1,
      name: 'Maths',
      code: 'M101',
      credits: 4,
      grade: 'A'
    },

    {
      id: 2,
      name: 'Physics',
      code: 'P102',
      credits: 3,
      grade: 'B'
    },

    {
      id: 3,
      name: 'Chemistry',
      code: 'C103',
      credits: 4,
      grade: 'A'
    },

    {
      id: 4,
      name: 'Java',
      code: 'J104',
      credits: 5,
      grade: 'A'
    },

    {
      id: 5,
      name: 'Python',
      code: 'P105',
      credits: 3,
      grade: 'B'
    }

  ]

})

const filteredCourses = computed(() => {

  return courses.value.filter(

    course =>

      course.name
      .toLowerCase()
      .includes(
        searchTerm.value.toLowerCase()
      )

  )

})

</script>