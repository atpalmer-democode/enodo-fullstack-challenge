import Vue from 'vue';
import VueRouter from 'vue-router';
import Home from '../views/Home.vue';

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,
  },
  {
    path: '/properties',
    name: 'Properties',
    component: () => import(/* webpackChunkName: "properties" */ '../views/Properties.vue'),
  },
];

const router = new VueRouter({
  routes
});

export default router;

