<template>
    <a-form :model="form" :style="{ width: '600px' }" @submit="handleSubmit">
      <a-form-item field="name" label="专业名称">
        <a-input v-model="form.name" placeholder="专业名称" />
      </a-form-item>
      <a-form-item field="gender" label="学院编号">
        <a-input v-model="form.academy_id" placeholder="学院编号" />
      </a-form-item>
      <a-form-item>
        <a-button html-type="submit">导入</a-button>
      </a-form-item>
    </a-form>
  </template>
    
    <script setup>
  import { reactive } from "vue";
  import { importProfession } from '@/api/admin';
  const form = reactive({
    name: "",
    academy_id: ""
  });
  const handleSubmit = (data) => {
    console.log(data);
    importProfession(data.values.name, data.values.academy_id);
  };
  </script>
    