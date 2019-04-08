<template>
  <div>
      <Header />
      <h1 align="center">Welcome to eleme.DB</h1>
      <h3 align="center">饿了么数据管理系统</h3>
    </div>
</template>

<script>
import Header from "@/components/MainHeader.vue";

export default {
  name: "Main",
  components: {
    Header
  }
};
</script>

<style lang="less">
h1 {
  margin-top: 20%;
}
h3 {
  margin-bottom: 20%;
}
</style>
