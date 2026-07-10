<template>

  <div>

    <h2>{{ name }}</h2>

    <p>Code: {{ code }}</p>

    <p>Credits: {{ credits }}</p>

    <p>Grade: {{ grade }}</p>

  </div>

</template>

<script setup>

defineProps({

  name: String,
  code: String,
  credits: Number,
  grade: String

})

</script>