<template>
    <a-form :model="form" :style="{ width: '600px' }" @submit="handleSubmit">
      <a-form-item field="name" label="班级名称">
        <a-input v-model="form.name" placeholder="班级名称" />
      </a-form-item>
      <a-form-item field="gender" label="专业编号">
        <a-input v-model="form.profession_id" placeholder="专业编号" />
      </a-form-item>
      <a-form-item>
        <a-button html-type="submit">导入</a-button>
      </a-form-item>
    </a-form>
  </template>
    
<script setup>
  import { reactive } from "vue";
  import { importClass } from '@/api/admin';
  const form = reactive({
    name: "",
    profession_id: ""
  });
  const handleSubmit = (data) => {
    console.log(data);
    importClass(data.values.name, data.values.profession_id);
  };
  </script>
    