import Vue from 'vue';
import VueRouter from 'vue-router';

Vue.use(VueRouter);

import Login from './components/Login.vue'
import Main from './components/Main.vue'
import Board from './components/Board.vue';

const routes = [
	{
		path: "/",
		component: Login
	},
	{
		path: "/login",
		component: Login
	},
	{
		path: "/home",
		component: Main
	},
	{
		path: "/board/:boardid/:boardName",
		component: Board
	}
];

const router = new VueRouter({
	mode: "history",
	routes,
});

export default router;