<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <el-button id="goLog" @click="toLogin" plain round>用户登录<i class="el-icon-service el-icon--right"></i></el-button>
    <h6 @click="toAdmin">管理员入口</h6>
  </div>
</template>

<script>
export default {
  name: "Welcome",
  props: {
    msg: String
  },
  methods: {
    toAdmin: function() {
      this.$confirm("此操作需要有更高权限, 是否继续?", "提示", {
        confirmButtonText: "确定",
        cancelButtonText: "取消",
        type: "warning"
      })
        .then(() => {
          this.$router.push({ path: "/admin" });
          this.$router.go(0);
        })
        .catch(() => {
          this.$router.push({ path: "/" });
        });
    },
    toLogin: function() {
      this.$router.push({ path: "/login" });
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="less">
h1 {
  margin-top: 10%;
  margin-bottom: 5%;
}
h6 {
  margin-top: 5%;
  margin-bottom: 5%;
  cursor: pointer;
  text-decoration: underline;
}
#goLog {
  /*margin-top: 5%;*/
}
</style>
