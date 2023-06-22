<template>
  <a-form :model="form" :style="{ width: '600px' }" @submit="handleSubmit">
    <a-form-item field="name" label="姓名">
      <a-input v-model="form.name" placeholder="姓名" />
    </a-form-item>
    <a-form-item field="password" label="密码">
      <a-input v-model="form.password" placeholder="密码" />
    </a-form-item>
    <a-form-item field="gender" label="性别">
      <a-input v-model="form.gender" placeholder="性别" />
    </a-form-item>
    <a-form-item field="birth" label="生日">
      <a-date-picker v-model="form.birth" />
    </a-form-item>
    <a-form-item field="origin" label="生源地">
      <a-input v-model="form.origin" placeholder="生源地" />
    </a-form-item>
    <a-form-item field="class_id" label="班级编号">
      <a-input v-model="form.class_id" placeholder="班级编号" />
    </a-form-item>
    <a-form-item>
      <a-button html-type="submit">导入</a-button>
    </a-form-item>
  </a-form>
</template>
  
  <script setup>
import { reactive } from "vue";
import { importStudent } from '@/api/admin';

const form = reactive({
  name: "",
  password: "",
  gender: "",
  birth: "",
  origin: "",
  class_id: "",
});
const handleSubmit = (data) => {
  console.log(data);
  importStudent(data.values.name, data.values.password, data.values.gender, data.values.birth, data.values.origin, data.values.class_id);
};
</script>
  