<template>

  <div>

    <h1>
      Student Portal
    </h1>

    <h3>
      Enrolled Courses:
      {{ store.enrolledCourses.length }}
    </h3>

  </div>

</template>

<script setup>

import { useEnrollmentStore } from '../stores/enrollment'

const store = useEnrollmentStore()

</script>