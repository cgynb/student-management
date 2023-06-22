import request from "./config";
import { Message } from "@arco-design/web-vue";
import { useUserStore } from '@/store/user';
const store = useUserStore();

export const getCourses = () => {
    return new Promise((resolve, reject) => {
        request({
            method: "get",
            url: "/student/courses"
        }).then(resp => {
            console.log(resp.data)
            resolve(resp.data.data.courses);
        }).catch(err => {
            console.log(err);
            reject(err);
        })
    })
}
export const getGrades = () => {
    return new Promise((resolve, reject) => {
        request({
            method: "get",
            url: "/student/grades"
        }).then(resp => {
            console.log(resp.data)
            resolve(resp.data.data.grades);
        }).catch(err => {
            console.log(err);
            reject(err);
        })
    })
}