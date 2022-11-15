import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import 'bootstrap/dist/css/bootstrap.css';
import BootstrapVue from 'bootstrap-vue';

Vue.config.productionTip = false;
Vue.vue(BootstrapVue);

new Vue({
  router,
  render: (h) => h(App),
}).$mount("#app");
