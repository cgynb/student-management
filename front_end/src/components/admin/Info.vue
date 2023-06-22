<template>
    <a-card title="学生信息" :style="{ height: '100%', width: '100%' }">
      <a-row>
        <a-col :span="4"></a-col>
        <a-col :span="8">
          <p>姓名: {{ store.user.name }}</p>
        </a-col>
        <a-col :span="8">
          <p>管理员编号: {{ store.user.id }}</p>
        </a-col>
        <a-col :span="4"></a-col>
      </a-row>
    </a-card>
  </template>
  <script setup>
  import { useUserStore } from "@/store/user";
  
  const store = useUserStore();
  </script>
    