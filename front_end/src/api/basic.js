import request from "./config";
import { getCourses, getGrades } from "./student";
import { Message } from "@arco-design/web-vue";
import { useUserStore } from '@/store/user';
const store = useUserStore();

export const studentLogin = (id, password) => {
    request({
        method: "post",
        url: "/student/login",
        data: {
            id,
            password
        }
    }).then(resp => {
        // console.log(resp.data.data);
        if(resp.data.code == 200){
            store.user = resp.data.data.student;
            store.login = true;
            Message.success({ content: "登录成功", showIcon: true });
        }else{
            Message.error("登录失败");
        }
    }).catch(err => {
        console.log(err);
    })
}
export const adminLogin = (id, password) => {
    request({
        method: "post",
        url: "/admin/login",
        data: {
            id,
            password
        }
    }).then(resp => {
        // console.log(resp.data.data);
        if(resp.data.code == 200){
            store.user = resp.data.data.admin;
            store.login = true;
            store.role = "admin";
            Message.success({ content: "登录成功", showIcon: true });
        }else{
            Message.error("登录失败");
        }
    }).catch(err => {
        console.log(err);
    })
}
