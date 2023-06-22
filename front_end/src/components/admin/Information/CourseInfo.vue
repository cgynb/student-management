<template>
  <a-table
    :columns="columns"
    :data="data"
    @change="handleChange"
    :pagination="false"
    :style="{ height: '100%', width: '100%' }"
  >
  </a-table>
</template>
<script setup>
import { reactive, h } from "vue";
import { IconSearch } from "@arco-design/web-vue/es/icon";
import { getCourses } from "@/api/admin";

const data = reactive([]);
getCourses().then((res) => {
  for (let item of res) {
    item.key = item.id;
    data.push(item);
  }
});
const columns = [
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
    title: "上课时间",
    dataIndex: "start",
  },
  {
    title: "下课时间",
    dataIndex: "end",
  },
  {
    title: "星期",
    dataIndex: "day",
  },
];

const handleChange = (data, extra, currentDataSource) => {
  console.log("change", data, extra, currentDataSource);
};
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
      