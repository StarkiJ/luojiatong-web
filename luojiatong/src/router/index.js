import { 
    createRouter,
    createWebHashHistory,
} from "vue-router";

import Index from '~/pages/index.vue'
import Homepage from '~/pages/homepage.vue'
import About from '~/pages/about.vue'
import NotFound from '~/pages/404.vue'
import Login from '~/pages/login.vue'

const routes = [{
    path:"/",
    component:Homepage,
    name:'Homepage',
    mata:{
        title:'珞珈通-主页'
    }
},{
    path:"/about",
    component:About
},{
    path:"/login",
    component:Login
},{
    path:'/:pathMatch(.*)*', 
    name: 'NotFound', 
    component: NotFound
},]

const router = createRouter({
    history:createWebHashHistory(),
    routes
})

export default router
