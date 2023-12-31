import './style.css'
import { createApp } from 'vue'
import ArcoVue from '@arco-design/web-vue';
import App from './App.vue';
import '@arco-design/web-vue/dist/arco.css';
import router from './router/index';
import { createPinia } from "pinia";
import piniaPersist from 'pinia-plugin-persist';

const pinia = createPinia();
pinia.use(piniaPersist);

const app = createApp(App);
app.use(router);
app.use(pinia);
app.use(ArcoVue);
app.mount('#app');
