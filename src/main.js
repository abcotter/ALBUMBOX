import Vue from 'vue';
import App from './App.vue'
import store from './store.js'
import router from './router.js'
import { APIURL } from './globalVar.js'
import VueToast from 'vue-toast-notification';
import 'vue-toast-notification/dist/theme-sugar.css';
import './assets/toast.scss';

Vue.config.productionTip = false
Vue.use(VueToast, {
	position: 'bottom',
	duration: 2500
})

Vue.prototype.$apiURL = APIURL;

new Vue({
	router,
	store,
	render: h => h(App),
}).$mount('#app')
