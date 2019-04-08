<template>
  <div>
    <el-menu :default-active="$route.path" class="el-menu-demo" mode="horizontal" router>
      <el-menu-item index="/read">
        <span>查询信息</span>
        <i class="el-icon-search el-icon--right" slot></i>
      </el-menu-item>
      <el-menu-item index="/admin-login" @click="authCheck">
        <span>添加 & 编辑 & 删除</span>
        <i class="el-icon-edit-outline el-icon--right" slot></i>
      </el-menu-item>
      <el-menu-item index="/main">
        <span>返回主页</span>
        <i class="el-icon-menu el-icon--right el-icon--right" slot></i>
      </el-menu-item>
      <el-menu-item index="/">
        <span>退出系统</span>
        <i class="el-icon-circle-close-outline el-icon--right" slot></i>
      </el-menu-item>
      <!--<el-button id="logOut" type="danger" @click="Bye" round>退出<i class="el-icon-circle-close-outline el-icon&#45;&#45;right"></i></el-button>-->
    </el-menu>
  </div>
</template>

<script>
export default {
  name: "Main",
  methods: {
    authCheck: function() {
      this.$confirm("此操作需要有更高权限, 是否继续?", "提示", {
        confirmButtonText: "确定",
        cancelButtonText: "取消",
        type: "warning"
      })
        .then(() => {
          this.$router.go(0);
        })
        .catch(() => {
          this.$router.push({ path: "/main" });
        });
    }
    // Bye: function() {
    //   this.$router.push({ path: "/" });
    // }
  }
};
</script>

<style lang="less">
</style>
