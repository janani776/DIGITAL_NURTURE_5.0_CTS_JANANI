<template>

  <div>

    <h1>
      Course Detail
    </h1>

    <h2>
      Course ID:
      {{ route.params.id }}
    </h2>

    <button @click="enrollCourse">

      Enroll

    </button>

  </div>

</template>

<script setup>

import { useRoute, useRouter } from 'vue-router'

const route = useRoute()

const router = useRouter()

function enrollCourse() {

  alert('Enrolled Successfully')

  router.push('/profile')

}

</script>