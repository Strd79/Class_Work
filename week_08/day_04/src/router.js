import Vue from 'vue';
import Router from 'vue-router';
import Home from '@/views/Home';
import About from '@/views/About';
import Contact from '@/views/Contact';

Vue.use(Router)

const router = new Router({
    mode: 'history',
    routes: [
        {
            path: '',
            name: 'home',
            component: Home
        },
        {
            path: '/about',
            name: 'about',
            component: About,
            props: true
        },
        {
            path: '/contact',
            name: 'contact',
            component: Contact,
        }
    ]
})

export default router;