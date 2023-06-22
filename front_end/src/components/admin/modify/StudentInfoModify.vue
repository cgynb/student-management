<template>
  <a-row>
    <a-col :span="6"></a-col>
    <a-col :span="12">
      <a-form :model="form" @submit="handleSubmit">
        <a-form-item
          field="student_id"
          label="学号"
        >
          <a-input v-model="form.student_id" placeholder="学号" />
        </a-form-item>
        <a-form-item label="修改">
            <a-select
              :options="['姓名', '密码', '性别', '生日', '生源地', '班级编号']"
              :style="{ width: '160px' }"
              placeholder="修改字段"
              v-model="form.set"
            />
            <a-input placeholder="修改值" v-model="form.value"/>
        </a-form-item>
        <a-form-item>
          <a-button html-type="submit">修改</a-button>
        </a-form-item>
      </a-form>
    </a-col>
    <a-col :span="6"></a-col>
  </a-row>
</template>
    
  <script setup>
import { reactive } from "vue";
import { modifyStudent } from "@/api/admin";
import { Message } from "@arco-design/web-vue";

const form = reactive({
  student_id: "",
  value: "",
  set: "",
});
const mp = {
    '姓名': 'name', 
    '密码': 'password',
    '性别': 'gender', 
    '生日': 'birth',
    '生源地': 'origin', 
    '班级编号': 'class_id'
}
const handleSubmit = (data) => {
  modifyStudent(data.values.student_id, mp[data.values.set], data.values.value)
    .then((res) => {
      Message.success("修改成功");
    }).catch(err => {
        Message.error("修改成功");
    });
};
</script>
    