<template>
  <div class="about">
    <div id="nav">
      <router-link to="/">Home</router-link> |
      <router-link to="/about">About</router-link>
    </div>
    <h1>e l e m e . D B</h1>
    <h3>项目作者</h3>
    <h5>柯瀚林</h5>
    <h3>项目结构</h3>
    <h5>Vue.js + django + MySQL</h5>
    <h3>项目语言</h3>
    <h5>Python + HTML + JavaScript + CSS</h5>
  </div>
</template>

<style lang="less">
#nav {
  padding: 2%;
  a {
    font-weight: bold;
    color: #2c3e50;
    &.router-link-exact-active {
      color: #409eff;
    }
  }
}
h1 {
  margin-top: 5%;
  margin-bottom: 5%;
}
h3 {
  margin-bottom: 2%;
}
h5 {
  margin-bottom: 2%;
}
</style>
