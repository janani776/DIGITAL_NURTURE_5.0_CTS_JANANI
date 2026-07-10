<template>

  <div>

    <h1>

      Profile

    </h1>

    <button
      type="button"
      @click="store.$reset()"
    >

      Clear All

    </button>

    <h2>

      Enrolled Courses

    </h2>

    <div
      v-for="course in enrolledCourses"
      :key="course.id"
    >

      <h3>

        {{ course.title || course.name }}

      </h3>

    </div>

    <h2>

      Total Courses:

      {{ totalCredits }}

    </h2>

  </div>

</template>

<script setup>

import {

  storeToRefs

} from 'pinia'

import {

  useEnrollmentStore

} from '../stores/enrollment'

const store = useEnrollmentStore()

const {

  enrolledCourses,
  totalCredits

} = storeToRefs(store)

</script>