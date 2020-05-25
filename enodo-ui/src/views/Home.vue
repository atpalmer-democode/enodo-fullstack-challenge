<template>
  <div class="home">
    <div>
      <img alt="Vue logo" src="../assets/enodo.svg">
    </div>
    <div class="title">Fullstack Challenge</div>
    <div class="login">
      <router-link :to="{ name: 'Properties' }" tag="el-button" class="start-button">Start</router-link>
    </div>
  </div>
</template>

<style scoped>
.home {
  height: 100vh;
  background-color: #263238;
}

.title {
  color: #f7f7f7;
  font-size: 32pt;
  padding: 20px;
}

.login {
  padding: 20px;
}

.start-button {
  font-size: 16pt;
  background-color: #f7f7f7;
  color: #424242;
}
</style>

