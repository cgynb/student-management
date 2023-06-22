import { createRouter, createWebHashHistory } from 'vue-router'
import { useUserStore } from '@/store/user';

const routes = [
    {
        path: '/student',
        component: () => import("@/components/student/Student.vue"),
        children: [
            {
                path: 'course',
                component: () => import("@/components/student/Course.vue")
            },
            {
                path: 'grade',
                component: () => import("@/components/student/Grade.vue")
            },
            {
                path: 'info',
                component: () => import("@/components/student/Info.vue")
            }
        ]
    },
    {
        path: '/admin',
        component: () => import("@/components/admin/Admin.vue"),
        children: [
            {
                path: 'import',
                component: () => import("@/components/admin/import/Import.vue"),
                children: [
                    {
                        path: 'student',
                        component: () => import("@/components/admin/import/ImportStudent.vue")
                    },
                    {
                        path: 'class',
                        component: () => import("@/components/admin/import/ImportClass.vue")
                    },
                    {
                        path: 'profession',
                        component: () => import("@/components/admin/import/ImportProfession.vue")
                    },
                    {
                        path: 'academy',
                        component: () => import("@/components/admin/import/ImportAcademy.vue")
                    },
                    {
                        path: 'grade',
                        component: () => import("@/components/admin/import/ImportGrade.vue")
                    },
                    {
                        path: 'course',
                        component: () => import("@/components/admin/import/ImportCourse.vue")
                    }
                ]
            },
            {
                path: 'info',
                component: () => import("@/components/admin/Info.vue")
            },
            {
                path: 'information',
                component: () => import("@/components/admin/information/Information.vue"),
                children: [
                    {
                        path: 'academy',
                        component: () => import("@/components/admin/information/AcademyInfo.vue")
                    },
                    {
                        path: 'profession',
                        component: () => import("@/components/admin/information/ProfessionInfo.vue")
                    },
                    {
                        path: 'class',
                        component: () => import("@/components/admin/information/ClassInfo.vue")
                    },
                    {
                        path: 'student',
                        component: () => import("@/components/admin/information/StudentInfo.vue")
                    },
                    {
                        path: 'course',
                        component: () => import("@/components/admin/information/CourseInfo.vue")
                    },
                    {
                        path: 'grade',
                        component: () => import("@/components/admin/information/GradeInfo.vue")
                    },
                ]
            },
            {
                path: 'modify',
                component: () => import("@/components/admin/modify/Modify.vue"),
                children: [
                    {
                        path: 'student',
                        component: () => import("@/components/admin/modify/StudentInfoModify.vue")
                    },
                    {
                        path: 'grade',
                        component: () => import("@/components/admin/modify/GradeModify.vue")
                    }
                ]
            }
        ]
    },
    {
        path: '/login',
        component: () => import("@/components/Login.vue")
    },
    {
        path: '/error',
        component: () => import("@/components/Error.vue"),
    },
    {
        path: '/:pathMatch(.*)',
        redirect: '/error'
    }
];
const router = createRouter({
    history: createWebHashHistory(),
    routes,
});

router.beforeEach((to, from) => {
    const store = useUserStore();
    if (store.login === false) {
        if (to.path !== '/login') {
            return {path: '/login'};
        }else{
            return true;
        }
    } else {
        return true;
    }
});

export default router;
