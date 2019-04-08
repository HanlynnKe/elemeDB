<template>
  <div>
    <h1>eleme.DB</h1>
    <h3>登录饿了么数据库管理系统</h3>
    <el-form ref="form" label-width="80px">
      <el-form-item label="用户名" size="small"
                    rules="[{required: true, message: '请输入用户名', trigger: 'blur'}]">
        <el-input v-model="usrName" clearable></el-input>
      </el-form-item>
      <el-form-item label="密码" size="small"
                    rules="[{required: true, message: '请输入密码', trigger: 'blur'}]">
        <el-input v-model="usrPwd" type="password" clearable></el-input>
      </el-form-item>
      <el-form-item>
        <el-row type="flex" justify="center">
          <el-button type="primary" @click="onSubmit" plain round>登录</el-button>
          <el-button type="info" @click="goBack" plain round>取消</el-button>
        </el-row>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
export default {
  name: "Login",
  data() {
    return {
      usrName: "",
      usrPwd: ""
    };
  },
  methods: {
    onSubmit: function() {
      let userInfo = {};
      userInfo["userName"] = this.usrName;
      userInfo["password"] = this.usrPwd;
      let postData = this.$qs.stringify(userInfo);
      this.axios.post("check/", postData).then(
        function(response) {
          if (response.data === 0) {
            alert("Failed!");
          } else {
            this.$router.push({ path: "/main" });
          }
        }.bind(this)
      );
    },
    goBack: function() {
      this.$router.push({ path: "/" });
    }
  }
};
</script>

<style scoped>
h1 {
  margin-top: 10%;
}

h3 {
  text-align: center;
  margin: 5% 0 0;
}

form {
  margin-top: 5%;
  margin-bottom: 10%;
  margin-left: 20%;
  margin-right: 20%;
  padding-top: 5%;
  padding-bottom: 2%;
  padding-left: 2%;
  padding-right: 5%;
  border-style: groove;
  border-color: #409eff;
}
</style>
