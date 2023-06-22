<template>
  <a-table
    :columns="columns"
    :data="rowCourses"
    :pagination="false"
    :style="{ height: '100%', width: '100%' }"
  />
</template>
  
<script setup>
import { reactive } from "vue";
import { getCourses } from "@/api/student";
const columns = [
  {
    title: "时间",
    dataIndex: "time",
  },
  {
    title: "一",
    dataIndex: "Mon",
  },
  {
    title: "二",
    dataIndex: "Tues",
  },
  {
    title: "三",
    dataIndex: "Wed",
  },
  {
    title: "四",
    dataIndex: "Thur",
  },
  {
    title: "五",
    dataIndex: "Fri",
  },
  {
    title: "六",
    dataIndex: "Sat",
  },
  {
    title: "日",
    dataIndex: "Sun",
  },
];
const rowCourses = reactive([]);
let columnCourses = null;
for (let i = 1; i <= 11; i++) {
  rowCourses.push({
    key: `${i}`,
    time: `${i}`,
    Mon: "",
    Tues: "",
    Wed: "",
    Thur: "",
    Fri: "",
    Sat: "",
    Sun: "",
  });
}
getCourses().then((res) => {
  columnCourses = res;
  for (let item of columnCourses) {
    switch (item.day) {
      case 1:
        for (let i = item.start - 1; i < item.end; i++) {
          rowCourses[i].Mon = item.course_name;
        }
        break;
      case 2:
        for (let i = item.start - 1; i < item.end; i++) {
          rowCourses[i].Tues = item.course_name;
        }
        break;
      case 3:
        for (let i = item.start - 1; i < item.end; i++) {
          rowCourses[i].Wed = item.course_name;
        }
        break;
      case 4:
        for (let i = item.start - 1; i < item.end; i++) {
          rowCourses[i].Thur = item.course_name;
        }
        break;
      case 5:
        for (let i = item.start - 1; i < item.end; i++) {
          rowCourses[i].Fri = item.course_name;
        }
        break;
      case 6:
        for (let i = item.start - 1; i < end; i++) {
          rowCourses[i].Sat = item.course_name;
        }
        break;
      case 7:
        for (let i = item.start - 1; i < item.end; i++) {
          rowCourses[i].Sun = item.course_name;
        }
        break;
    }
  }
}).catch(err => {
    // console.log(err)
});

// const columnCourses = [
//   {
//     course_name: "代数",
//     day: 1,
//     end: 4,
//     start: 3,
//     student_id: 1,
//     student_name: "cgy",
//   },
//   {
//     course_name: "数据库",
//     day: 1,
//     end: 2,
//     start: 1,
//     student_id: 1,
//     student_name: "cgy",
//   },
//   {
//     course_name: "数值分析",
//     day: 2,
//     end: 2,
//     start: 1,
//     student_id: 1,
//     student_name: "cgy",
//   },
//   {
//     course_name: "体育",
//     day: 2,
//     end: 6,
//     start: 5,
//     student_id: 1,
//     student_name: "cgy",
//   },
// ];
</script>
