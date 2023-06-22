<template>
  <a-row>
    <a-col :span="6"></a-col>
    <a-col :span="12">
      <a-form :model="form" @submit="handleSubmit">
        <a-form-item
          field="student_id"
          tooltip="Please enter username"
          label="学号"
        >
          <a-input v-model="form.student_id" placeholder="学号" />
        </a-form-item>
        <a-form-item field="course_id" label="课程编号">
          <a-input v-model="form.course_id" placeholder="课程编号" />
        </a-form-item>
        <a-form-item field="grade" label="成绩">
          <a-input-number v-model="form.grade" placeholder="成绩" :min="0" :max="100"/>
        </a-form-item>
        <a-form-item>
          <a-button html-type="submit">录入</a-button>
        </a-form-item>
      </a-form>
    </a-col>
    <a-col :span="6"></a-col>
  </a-row>
</template>
  
<script setup>
import { reactive } from "vue";
import { modifyGrade } from "@/api/admin";
import { Message } from "@arco-design/web-vue";

const form = reactive({
  student_id: "",
  course_id: "",
  grade: null,
});
const handleSubmit = (data) => {
  console.log(data.values.student_id, data.values.course_id, data.values.grade);
  modifyGrade(data.values.student_id, data.values.course_id, data.values.grade).then(res => {
    Message.success("录入成功");
  });
};
</script>
  