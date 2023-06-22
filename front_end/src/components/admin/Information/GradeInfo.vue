<template>
  <a-radio-group type="button" v-model="limit.pass">
    <a-radio value="all">全部</a-radio>
    <a-radio value="pass">及格</a-radio>
    <a-radio value="fail">不及格</a-radio>
    <a-radio value="no">未出成绩</a-radio>
  </a-radio-group>
  <a-input v-model="limit.course_id" placeholder="输入筛选课程编号" />
  <a-table
    :columns="columns"
    :data="data"
    :pagination="false"
    :style="{ height: '100%', width: '100%' }"
  >
  </a-table>
</template>
      
<script setup>
import { reactive, watch } from "vue";
import { IconSearch } from "@arco-design/web-vue/es/icon";
import { getGrades } from "@/api/admin";

const limit = reactive({
  pass: "all",
  course_id: null,
});
const data = reactive([]);
const all_data = [];
watch(limit, (newVal, oldVal) => {
  data.splice(0, data.length);
  const temp_data = all_data.filter((item) => {
    let filter_course_id =
      newVal.course_id == "" || newVal.course_id == null
        ? true
        : item.course_id == newVal.course_id;
    let filter_grade = true;
    if (newVal.pass == "no") {
      filter_grade = item.grade == null;
    }
    if (newVal.pass == "pass") {
      filter_grade = item.grade >= 60;
    }
    if (newVal.pass == "fail") {
      filter_grade = item.grade < 60 && item.grade != null;
    }
    return filter_course_id && filter_grade;
  });
  for (let item of temp_data) {
    data.push(item);
  }
});
getGrades().then((res) => {
  for (let item of res) {
    item.key = item.id;
    all_data.push(item);
    data.push(item);
  }
});
const columns = [
  {
    title: "成绩",
    dataIndex: "grade",
    sortable: {
      sortDirections: ["ascend", "descend"],
    },
  },
  {
    title: "学号",
    dataIndex: "student_id",
  },
  {
    title: "姓名",
    dataIndex: "student_name",
  },
  {
    title: "课程",
    dataIndex: "course_name",
  },
  {
    title: "课程编号",
    dataIndex: "course_id",
  },
  {
    title: "班级",
    dataIndex: "class_name",
  },
  {
    title: "专业",
    dataIndex: "profession_name",
  },
  {
    title: "学院",
    dataIndex: "academy_name",
  },
];
</script>
      
<style>
.custom-filter {
  padding: 20px;
  background: var(--color-bg-5);
  border: 1px solid var(--color-neutral-3);
  border-radius: var(--border-radius-medium);
  box-shadow: 0 2px 5px rgb(0 0 0 / 10%);
}

.custom-filter-footer {
  display: flex;
  justify-content: space-between;
}
</style>
      