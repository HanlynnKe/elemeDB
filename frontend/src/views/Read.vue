¬<template>
  <div>
    <Header />
    <h1>create · READ · update · delete</h1>
    <el-tabs tab-position="left"
             style="margin-top: 5%;
                    margin-left: 5%;
                    margin-right: 5%;"
             @tab-click="clearValue">
      <el-tab-pane label="查找选项">
        <h3 style="text-align: center; margin-top: 5%; margin-bottom: 5%;">请选择左侧的查询选项进行查询</h3>
        <el-popover placement="right-end" title="查询选项" width="200" trigger="click"
                    content="按照用户、用户收藏、用户地址簿、餐厅、餐厅菜单、用户订单对饿了么数据进行查询">
          <el-button type="info" slot="reference" icon="el-icon-back"
                     style="text-align: center" circle>
          </el-button>
        </el-popover>
      </el-tab-pane>
      <el-tab-pane label="按用户">
        <el-form ref="form" label-width="150px">
          <el-form-item label="要查询的用户姓名：" size="small" style="margin-bottom: 10%"
                        rules="[{required: true, message: '请输入姓名'}]">
            <el-row class="searchRow">
              <el-col span="16">
                <el-input v-model="name"></el-input>
              </el-col>
              <el-col span="4">
                <el-button type="success" v-on:click="searchItem(1)" @keyup.enter.native="searchItem(1)" circle><i class="el-icon-search"></i></el-button>
              </el-col>
            </el-row>
          </el-form-item>
          <el-table :data="tableData" style="width: 100%; margin-bottom: 5%" max-height="250">
            <el-table-column prop="name" label="姓名" width="120"></el-table-column>
            <el-table-column prop="tel" label="电话" width="120"></el-table-column>
            <el-table-column prop="fav" label="收藏店家数" width="100"></el-table-column>
          </el-table>
          <el-form-item label="已搜索到：" size="small">
            {{countIndex[0]}} 条记录
          </el-form-item>
        </el-form>
      </el-tab-pane>
      <el-tab-pane label="按收藏">
        <el-form ref="form" label-width="150px">
          <el-form-item label="要查询的用户姓名：" size="small" style="margin-bottom: 10%"
                        rules="[{required: true, message: '请输入姓名'}]">
            <el-row class="searchRow">
              <el-col span="16">
                <el-input v-model="name"></el-input>
              </el-col>
              <el-col span="4">
                <el-button type="success" v-on:click="searchItem(2)" @keyup.enter.native="searchItem(2)" circle><i class="el-icon-search"></i></el-button>
              </el-col>
            </el-row>
          </el-form-item>
          <el-table :data="tableData" style="width: 100%; margin-bottom: 5%" max-height="250">
            <el-table-column prop="rstrtName" label="餐厅名" width="150" fixed></el-table-column>
            <el-table-column prop="delivLeast" label="起送价" width="100"></el-table-column>
            <el-table-column prop="distance" label="距离" width="100"></el-table-column>
            <el-table-column prop="leastDeliv" label="最短送达时间" width="120"></el-table-column>
          </el-table>
          <el-form-item label="已搜索到：" size="small">
            {{countIndex[0]}} 条记录
          </el-form-item>
        </el-form>
      </el-tab-pane>
      <el-tab-pane label="按地址">
        <el-form ref="form" label-width="150px">
          <el-form-item label="要查询的用户姓名：" size="small" style="margin-bottom: 10%"
                        rules="[{required: true, message: '请输入姓名'}]">
            <el-row class="searchRow">
              <el-col span="16">
                <el-input v-model="name"></el-input>
              </el-col>
              <el-col span="4">
                <el-button type="success" v-on:click="searchItem(3)" @keyup.enter.native="searchItem(3)" circle><i class="el-icon-search"></i></el-button>
              </el-col>
            </el-row>
          </el-form-item>
          <el-table :data="tableData" style="width: 100%; margin-bottom: 5%" max-height="250">
            <el-table-column fixed prop="addressID" label="ID" width="50"></el-table-column>
            <el-table-column prop="contact" label="联系人姓名" width="120"></el-table-column>
            <el-table-column prop="gender" label="联系人性别" width="90"></el-table-column>
            <el-table-column prop="phone" label="联系人电话" width="120"></el-table-column>
            <el-table-column prop="address" label="联系人地址" width="360"></el-table-column>
            <el-table-column prop="tag" label="地址标签" width="90"></el-table-column>
          </el-table>
          <el-form-item label="已搜索到：" size="small">
            {{countIndex[0]}} 条记录
          </el-form-item>
        </el-form>
      </el-tab-pane>
      <el-tab-pane label="按餐厅">
        <el-form ref="form" label-width="150px">
          <el-form-item label="要查询的餐厅名称：" size="small" style="margin-bottom: 10%"
                        rules="[{required: true, message: '请输入餐厅名称'}]">
            <el-row class="searchRow">
              <el-col span="16">
                <el-input v-model="rstrtName"></el-input>
              </el-col>
              <el-col span="4">
                <el-button type="success" v-on:click="searchItem(4)" @keyup.enter.native="searchItem(4)" circle><i class="el-icon-search"></i></el-button>
              </el-col>
            </el-row>
          </el-form-item>
          <el-table :data="tableData" style="width: 100%; margin-bottom: 5%" max-height="250">
            <el-table-column fixed prop="rstrtName" label="餐厅名" width="120"></el-table-column>
            <el-table-column prop="rstrtClass" label="类别" width="100"></el-table-column>
            <el-table-column prop="rstrtAddress" label="地址" width="360"></el-table-column>
            <el-table-column prop="rstrtPhone" label="联系电话" width="120"></el-table-column>
            <el-table-column prop="workFrom" label="开店时间" width="120"></el-table-column>
            <el-table-column prop="workTo" label="打烊时间" width="120"></el-table-column>
          </el-table>
          <el-form-item label="已搜索到：" size="small">
            {{countIndex[0]}} 条记录
          </el-form-item>
        </el-form>
      </el-tab-pane>
      <el-tab-pane label="按菜单">
        <el-form ref="form" label-width="150px">
          <el-form-item label="要查询的餐厅名称：" size="small" style="margin-bottom: 10%"
                        rules="[{required: true, message: '请输入餐厅名称'}]">
            <el-row class="searchRow">
              <el-col span="16">
                <el-input v-model="rstrtName"></el-input>
              </el-col>
              <el-col span="4">
                <el-button type="success" v-on:click="searchItem(5)" @keyup.enter.native="searchItem(5)" circle><i class="el-icon-search"></i></el-button>
              </el-col>
            </el-row>
          </el-form-item>
          <el-table :data="tableData" style="width: 100%; margin-bottom: 5%" max-height="350">
            <el-table-column fixed prop="rstrtName" label="餐厅名" width="150"></el-table-column>
            <el-table-column prop="dish" label="菜品" width="150"></el-table-column>
            <el-table-column prop="price" label="价格" width="100"></el-table-column>
            <el-table-column prop="sale" label="销量" width="100"></el-table-column>
          </el-table>
          <el-form-item label="已搜索到：" size="small">
            {{countIndex[0]}} 条记录
          </el-form-item>
        </el-form>
      </el-tab-pane>
      <el-tab-pane label="按订单">
        <el-form ref="form" label-width="150px">
          <el-form-item label="要查询的订单号：" size="small" style="margin-bottom: 10%"
                        rules="[{required: true, message: '请输入订单号'}]">
            <el-row class="searchRow">
              <el-col span="16">
                <el-input v-model="orderID"></el-input>
              </el-col>
              <el-col span="4">
                <el-button type="success" v-on:click="searchItem(6)" @keyup.enter.native="searchItem(6)" circle><i class="el-icon-search"></i></el-button>
              </el-col>
            </el-row>
          </el-form-item>
          <el-table :data="tableData" style="width: 100%; margin-bottom: 5%" max-height="350">
            <el-table-column fixed prop="orderID" label="订单号" width="200"></el-table-column>
            <el-table-column prop="name" label="用户" width="120"></el-table-column>
            <el-table-column prop="rstrtName" label="餐厅" width="150"></el-table-column>
            <el-table-column prop="dish" label="菜品" width="150"></el-table-column>
            <el-table-column prop="price" label="菜品单价" width="100"></el-table-column>
            <el-table-column prop="sum" label="订单总价" width="100"></el-table-column>
            <el-table-column prop="orderTime" label="下单时间" width="150"></el-table-column>
            <el-table-column prop="contact" label="联系人" width="120"></el-table-column>
            <el-table-column prop="address" label="联系人地址" width="360"></el-table-column>
            <el-table-column prop="phone" label="联系人电话" width="120"></el-table-column>
            <el-table-column prop="delivPerson" label="配送员" width="120"></el-table-column>
            <el-table-column prop="delivPersonTel" label="配送员电话" width="120"></el-table-column>
          </el-table>
          <el-form-item label="已搜索到：" size="small">
            {{countIndex[0]}} 条记录
          </el-form-item>
        </el-form>
      </el-tab-pane>
    </el-tabs>
    <!--<el-button id="goHome" type="warning" @click="Home" round>返回主页<i class="el-icon-menu el-icon&#45;&#45;right"></i></el-button>-->
  </div>
</template>

<script>
import Header from "@/components/MainHeader.vue";
export default {
  name: "FindHim",
  components: {
    Header
  },
  data() {
    return {
      name: "",
      tel: "",
      fav: "",
      addressID: "",
      contact: "",
      gender: "",
      phone: "",
      address: "",
      tag: "",
      rstrtName: "",
      rstrtClass: "",
      rstrtAddress: "",
      rstrtPhone: "",
      workFrom: "",
      workTo: "",
      delivLeast: "",
      distance: "",
      leastDeliv: "",
      dish: "",
      price: "",
      sale: "",
      orderID: "",
      sum: "",
      orderTime: "",
      delivPerson: "",
      delivPersonTel: "",
      tableData: [],
      countIndex: [0]
    };
  },
  methods: {
    // Home: function() {
    //   this.$router.push({ path: "/main" });
    // },
    searchItem: function(mode) {
      let keyInfo = {};
      let index;
      let num = 0;
      var searchAns = [];
      keyInfo["mode"] = mode;
      keyInfo["name"] = this.name;
      keyInfo["rstrtName"] = this.rstrtName;
      keyInfo["orderID"] = this.orderID;
      let postData = this.$qs.stringify(keyInfo);
      this.axios.post("handle/", postData).then(
        function(response) {
          for (index in response.data) {
            searchAns.push(response.data[index]);
            num = num + 1;
          }
          this.countIndex.pop();
          this.countIndex.push(num);
          // console.log(searchAns);
        }.bind(this)
      );
      this.name = "";
      this.rstrtName = "";
      this.orderID = "";
      this.tableData = searchAns;
    },
    clearValue: function() {
      this.name = "";
      this.tel = "";
      this.fav = "";
      this.addressID = "";
      this.contact = "";
      this.gender = "";
      this.phone = "";
      this.address = "";
      this.tag = "";
      this.rstrtName = "";
      this.rstrtClass = "";
      this.rstrtPhone = "";
      this.rstrtAddress = "";
      this.workFrom = "";
      this.workTo = "";
      this.delivLeast = "";
      this.distance = "";
      this.leastDeliv = "";
      this.dish = "";
      this.price = "";
      this.sale = "";
      this.orderID = "";
      this.sum = "";
      this.orderTime = "";
      this.delivPerson = "";
      this.delivPersonTel = "";
      this.countIndex = [0];
    }
  }
};
</script>

<style scoped>
h1 {
  margin-top: 5%;
  margin-bottom: 5%;
}
form {
  margin-left: 10%;
  margin-right: 10%;
}
</style>
