import { defineStore } from 'pinia'

export const useUserStore = defineStore('user', {
    state: () => {
        return {
            login: false,
            role: "student",
            token: "",
            user: {
                student_name: null,
                gender: null,
                origin: null,
                birth: null,
                student_id: null,
                academy_name: null,
                profession_name: null,
                class_name: null
            }
        };
    },
    persist: {
        enabled: true,
        strategies: [
            {
                storage: localStorage,
            }
        ]
    }
})