<template>
  <a-form :model="form" :style="{ width: '600px' }" @submit="handleSubmit">
    <a-form-item field="name" label="课程名称">
      <a-input v-model="form.name" placeholder="课程名称" />
    </a-form-item>
    <a-form-item field="gender" label="上课时间（节）">
      <a-input v-model="form.start" placeholder="上课时间" />
    </a-form-item>
    <a-form-item field="gender" label="下课时间（节）">
      <a-input v-model="form.end" placeholder="下课时间" />
    </a-form-item>
    <a-form-item field="gender" label="上课星期">
      <a-input v-model="form.day" placeholder="周几" />
    </a-form-item>
    <a-form-item>
      <a-button html-type="submit">导入</a-button>
    </a-form-item>
  </a-form>
</template>
<script setup>
import { reactive } from "vue";
import { importCourse } from "@/api/admin";
const form = reactive({
  name: "",
  start: "",
  end: "",
  day: "",
});
const handleSubmit = (data) => {
  console.log(data);
  importCourse(
    data.values.name,
    data.values.start,
    data.values.end,
    data.values.day
  );
};
</script>
    