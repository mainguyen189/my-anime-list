import Vue from "vue";
import VueRouter from "vue-router";
import Miaow from "../components/Miaow";
import Anime from "../components/Anime";

Vue.use(VueRouter);

const routes = [
  {
    path: "/anime",
    name: "Anime",
    component: Anime,
  },
  {
    path: "/miaow",
    name: "Miaow",
    component: Miaow,
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
