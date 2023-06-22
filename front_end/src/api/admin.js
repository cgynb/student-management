import request from "./config";
import { Message } from "@arco-design/web-vue";
import { useUserStore } from '@/store/user';
const store = useUserStore();

export const importAcademy = (name, dean) => {
    request({
        method: "post",
        url: "/admin/academy",
        data: {
            name,
            dean
        }
    }).then(resp => {
        console.log(resp.data.data);
        if (resp.data.code == 200) {
            Message.info({ content: "添加成功", showIcon: true });
        }else{
            throw new Error("err");
        }
    }).catch(err => {
        Message.error("导入失败");
        console.log(err);
    })
}
export const importProfession = (name, academy_id) => {
    request({
        method: "post",
        url: "/admin/profession",
        data: {
            name,
            academy_id
        }
    }).then(resp => {
        console.log(resp.data.data);
        if (resp.data.code == 200) {
            Message.info({ content: "添加成功", showIcon: true });
        }else{
            throw new Error("err");
        }
    }).catch(err => {
        console.log(err);
        Message.error("导入失败");
    })
}
export const importClass = (name, profession_id) => {
    request({
        method: "post",
        url: "/admin/class",
        data: {
            name,
            profession_id
        }
    }).then(resp => {
        console.log(resp.data.data);
        if (resp.data.code == 200) {
            Message.info({ content: "添加成功", showIcon: true });
        }else{
            throw new Error("err");
        }
    }).catch(err => {
        console.log(err);
        Message.error("导入失败");
    })
}
export const importStudent = (name, password, gender, birth, origin, class_id) => {
    request({
        method: "post",
        url: "/admin/student",
        data: {
            name,
            password,
            gender,
            birth,
            origin,
            class_id
        }
    }).then(resp => {
        console.log(resp.data.data);
        if (resp.data.code == 200) {
            Message.info({ content: "添加成功", showIcon: true });
        }else{
            throw new Error("err");
        }
    }).catch(err => {
        console.log(err);
        Message.error("导入失败");
    })
}
export const importCourse = (name, start, end, day) => {
    request({
        method: "post",
        url: "/admin/course",
        data: {
            name,
            start,
            end,
            day
        }
    }).then(resp => {
        console.log(resp.data.data);
        if (resp.data.code == 200) {
            Message.info({ content: "添加成功", showIcon: true });
        }else{
            throw new Error("err");
        }
    }).catch(err => {
        console.log(err);
        Message.error("导入失败");
    })
}
export const importGrade = (student_id, course_id) => {
    request({
        method: "post",
        url: "/admin/grade",
        data: {
            student_id,
            course_id
        }
    }).then(resp => {
        console.log(resp.data.data);
        if (resp.data.code == 200) {
            Message.info({ content: "添加成功", showIcon: true });
        }else{
            throw new Error("err");
        }
    }).catch(err => {
        console.log(err);
        Message.error("导入失败");
    })
}

export const getAcademies = () => {
    return new Promise((resolve, reject) => {
        request({
            method: "get",
            url: "/admin/academies"
        }).then(resp => {
            if(resp.data.code != 200){
                throw new Error("err");
            }
            resolve(resp.data.data);
        }).catch(err => {
            console.log(err);
            Message.error("获取失败");
            reject(err);
        })
    })
}
export const getProfessions = () => {
    return new Promise((resolve, reject) => {
        request({
            method: "get",
            url: "/admin/professions"
        }).then(resp => {
            if(resp.data.code != 200){
                throw new Error("err");
            }
            resolve(resp.data.data);
        }).catch(err => {
            console.log(err);
            Message.error("获取失败");
            reject(err);
        })
    })
}
export const getClasses = () => {
    return new Promise((resolve, reject) => {
        request({
            method: "get",
            url: "/admin/classes"
        }).then(resp => {
            if(resp.data.code != 200){
                throw new Error("err");
            }
            resolve(resp.data.data);
        }).catch(err => {
            console.log(err);
            Message.error("获取失败");
            reject(err);
        })
    })
}
export const getStudents = () => {
    return new Promise((resolve, reject) => {
        request({
            method: "get",
            url: "/admin/students"
        }).then(resp => {
            if(resp.data.code != 200){
                throw new Error("err");
            }
            resolve(resp.data.data);
        }).catch(err => {
            console.log(err);
            Message.error("获取失败");
            reject(err);
        })
    })
}
export const getGrades = () => {
    return new Promise((resolve, reject) => {
        request({
            method: "get",
            url: "/admin/grades"
        }).then(resp => {
            if(resp.data.code != 200){
                throw new Error("err");
            }
            resolve(resp.data.data);
        }).catch(err => {
            console.log(err);
            Message.error("获取失败");
            reject(err);
        })
    })
}
export const getCourses = () => {
    return new Promise((resolve, reject) => {
        request({
            method: "get",
            url: "/admin/courses"
        }).then(resp => {
            if(resp.data.code != 200){
                throw new Error("err");
            }
            resolve(resp.data.data);
        }).catch(err => {
            console.log(err);
            Message.error("获取失败");
            reject(err);
        })
    })
}

export const modifyStudent = (student_id, set, value) => {
    return new Promise((resolve, reject) => {
        request({
            method: "put",
            url: "/admin/student",
            data: {
                student_id,
                set,
                value
            }
        }).then(resp => {
            console.log(resp.data)
            if(resp.data.code != 200){
                throw new Error("err");
            }else{
                resolve(resp.data.data);
            }
        }).catch(err => {
            console.log(err);
            Message.error("失败");
            reject(err);
        })
    })
}
export const modifyGrade = (student_id, course_id, grade) => {
    return new Promise((resolve, reject) => {
        request({
            method: "put",
            url: "/admin/grade",
            data: {
                grade,
                student_id,
                course_id
            }
        }).then(resp => {
            if(resp.data.code != 200){
                throw new Error("err");
            }
            resolve(resp.data);
        }).catch(err => {
            console.log(err);
            Message.error("失败");
            reject(err);
        })
    })
}


