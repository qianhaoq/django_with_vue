// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
// import Vue from 'vue'
// import App from './App'
// // import {Button, Select } from 'element-ui';


// // Vue.component(Button.name, Button);
// // Vue.component(Select.name, Select);

// /* eslint-disable no-new */
// new Vue({
//   el: '#app',
//   render: h => h(App)
// })


import Vue from 'vue';
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
// import { Upload } from 'element-ui';
import App from './App.vue';
var vueResource = require('vue-resource');
Vue.use(vueResource);
Vue.use(ElementUI);
// Vue.use(Upload);

new Vue({
  el: '#app',
  render: h => h(App)
});