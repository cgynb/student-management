<template>
  <a-row>
    <a-col :span="6"></a-col>
    <a-col :span="12">
      <a-form :model="form" :style="{ width: '600px' }" @submit="handleSubmit">
        <a-form-item field="id" :label="form.role == 'student' ? '学号': '管理员编号'">
          <a-input v-model="form.id" :placeholder="form.role == 'student' ? '请输入学号': '请输入管理员编号'" />
        </a-form-item>
        <a-form-item field="password" label="密码" tooltip="首次登录密码为123">
          <a-input v-model="form.password" placeholder="请输入密码" />
        </a-form-item>
        <a-form-item field="isStudent">
            学生
            <a-switch v-model="form.role" checked-value="admin" unchecked-value="student" />
            管理员
        </a-form-item>
        <a-form-item>
          <a-button html-type="submit">登录</a-button>
        </a-form-item>
      </a-form>
    </a-col>
    <a-col :span="6"></a-col>
  </a-row>
</template>
  
<script setup>
import { reactive } from "vue";
import { studentLogin, adminLogin } from "@/api/basic";
import { useRouter } from 'vue-router';

const router = useRouter();

const form = reactive({
  id: "",
  password: "",
  role: "student",
});

const handleSubmit = (data) => {
  if (data.values.role == "student") {
    studentLogin(data.values.id, data.values.password);
    router.push("/student/info");
  }else{
    adminLogin(data.values.id, data.values.password);
    router.push("/admin/info")
  }
};
</script>
  