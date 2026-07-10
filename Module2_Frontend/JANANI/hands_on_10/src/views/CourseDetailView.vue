<template>

  <div>

    <h1>

      Course Detail

    </h1>

    <h2>

      Course ID:

      {{ route.params.id }}

    </h2>

    <button
      type="button"
      @click="enrollCourse"
    >

      Enroll

    </button>

  </div>

</template>

<script setup>

import {

  useRoute,
  useRouter

} from 'vue-router'

import {

  useEnrollmentStore

} from '../stores/enrollment'

const route = useRoute()

const router = useRouter()

const store =

  useEnrollmentStore()

async function enrollCourse() {

  await store.fetchAndEnroll(

    route.params.id

  )

  router.push('/profile')

}

</script>