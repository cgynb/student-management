<template>
  <a-card title="学生信息" :style="{ height: '100%', width: '100%' }">
    <a-row>
      <a-col :span="4"></a-col>
      <a-col :span="8">
        <p>姓名: {{ store.user.student_name }}</p>
        <p>学院: {{ store.user.academy_name }}</p>
        <p>班级: {{ store.user.class_name }}</p>
        <p>生源地: {{ store.user.origin }}</p>
      </a-col>
      <a-col :span="8">
        <p>学号: {{ store.user.student_id }}</p>
        <p>专业: {{ store.user.profession_name }}</p>
        <p>性别: {{ store.user.gender }}</p>
        <p>生日: {{ store.user.birth }}</p>
      </a-col>
      <a-col :span="4"></a-col>
    </a-row>
  </a-card>
</template>
<script setup>
import { useUserStore } from "@/store/user";

const store = useUserStore();
</script>
  