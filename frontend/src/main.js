import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import axios from "axios";
import VueAxios from "vue-axios";
import qs from "qs";
import Element from "element-ui";
import "element-ui/lib/theme-chalk/index.css";

Vue.use(Element);

Vue.config.productionTip = false;

axios.defaults.headers.post["Content-Type"] =
  "application/x-www-form-urlencoded";

Vue.prototype.$qs = qs;
Vue.use(VueAxios, axios);

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount("#app");
