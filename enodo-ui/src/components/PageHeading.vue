<template>
  <div class="heading">
    <img class="logo" src="../assets/enodo.svg" height="100"/>
    <h1 class="text">{{ heading }}</h1>
  </div>
</template>

<script>
export default {
  props: {
    heading: String,
  },
};
</script>

<style scoped>
.heading {
  background-color: #263238;
  color: #f7f7f7;
  text-align: left;
  padding: 8px;
}

.heading .logo {
}

.heading h1.text {
  float: right;
  display: inline;
  font-size: 24pt;
  padding: 10px;
}
</style>
