<template>

  <div>

    <h1>Profile</h1>

    <h2>Enrolled Courses</h2>

    <div
      v-for="course in store.enrolledCourses"
      :key="course.id"
    >

      <h3>{{ course.name }}</h3>

      <p>{{ course.code }}</p>

      <button @click="store.unenroll(course.id)">

        Remove

      </button>

    </div>

    <h2>

      Total Credits:

      {{ store.totalCredits }}

    </h2>

  </div>

</template>

<script setup>

import { useEnrollmentStore }
from '../stores/enrollment'

const store = useEnrollmentStore()

</script>