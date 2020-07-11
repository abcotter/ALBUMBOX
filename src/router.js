import Vue from 'vue';
import VueRouter from 'vue-router';

Vue.use(VueRouter);

import Main from './components/Main.vue'
import Board from './components/Board.vue';

const routes = [
	{
		path: "/",
		component: Main
	},
	{
		path: "/board",
		component: Board
	}
];

const router = new VueRouter({
	mode: "history",
	routes,
});

export default router;