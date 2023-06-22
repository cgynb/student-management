<template>
    <a-form :model="form" :style="{ width: '600px' }" @submit="handleSubmit">
      <a-form-item field="student_id" label="学生编号">
        <a-input v-model="form.student_id" placeholder="学生编号" />
      </a-form-item>
      <a-form-item field="course_id" label="课程编号">
        <a-input v-model="form.course_id" placeholder="课程编号" />
      </a-form-item>
      <a-form-item>
        <a-button html-type="submit">导入</a-button>
      </a-form-item>
    </a-form>
  </template>
    
    <script setup>
  import { reactive } from "vue";
  import { importGrade } from '@/api/admin';
  const form = reactive({
    student_id: "",
    course_id: ""
  });
  const handleSubmit = (data) => {
    console.log(data);
    importGrade(data.values.student_id, data.values.course_id)
  };
  </script>
    