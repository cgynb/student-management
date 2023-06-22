import axios from 'axios';
import { useUserStore } from '@/store/user';
const store = useUserStore();

axios.defaults.baseURL = 'http://localhost:5000/api/v1';
axios.defaults.timeout = 5000;
axios.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded';
axios.defaults.headers.put['Content-Type'] = 'application/x-www-form-urlencoded';

const request = axios.create({});

// request hook
request.interceptors.request.use(req => {
    req.headers.Authorization = store.token;
    return req;
}, err => {
    console.log('resp err', err);
    return Promise.reject(err);
});

// response hook
request.interceptors.response.use(resp => {
    store.token = resp.headers.authorization;
    return resp;
}, err => {
    console.log("resp err", err);
    return Promise.reject(err);
});

export default request;
