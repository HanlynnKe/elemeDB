<template>
  <div class="home">
    <div id="nav">
      <router-link to="/">Home</router-link> |
      <router-link to="/about">About</router-link>
    </div>
    <Welcome msg="eleme.DB HITSZDBSEXP3"/>
  </div>
</template>

<script>
// @ is an alias to /src
import Welcome from "@/components/Welcome.vue";

export default {
  name: "home",
  components: {
    Welcome
  }
};
</script>

<style lang="less">
#nav {
  padding: 30px;
  a {
    font-weight: bold;
    color: #2c3e50;
    &.router-link-exact-active {
      color: #409eff;
    }
  }
}
</style>
