<template>
  <a-list :scrollbar="scrollbar" :style="{ height: '100%', width: '100%' }">
    <template #header>成绩单</template>
    <a-list-item v-for="(item, k) of gradeList" :key="k"
      ><p
        :class="[
          item.grade == null ? 'level5' : '',
          item.grade >= 90 ? 'level1' : '',
          item.grade < 90 && item.grade >= 77 ? 'level2' : '',
          item.grade >= 60 && item.grade < 77 ? 'level3' : '',
          item.grade < 60 ? 'level4' : '',
        ]"
      >
        {{ item.course_name }}{{ item.grade == null ? "暂无成绩" : item.grade }}
      </p></a-list-item
    >
  </a-list>
</template>
  
<script setup>
import { ref, reactive } from "vue";
import { getGrades } from "@/api/student";
const gradeList = reactive([]);
const scrollbar = ref(true);
getGrades().then((res) => {
    for(let item of res){
        gradeList.push(item);
    }
}).catch(err => {
    // console.log(err)
});
// for (let i = 0; i < 2; i++) {
//   gradeList.push({
//     course_name: "数据库",
//     grade: 100,
//   });
//   gradeList.push({
//     course_name: "数据库",
//     grade: 78,
//   });
//   gradeList.push({
//     course_name: "数据库",
//     grade: 66,
//   });
//   gradeList.push({
//     course_name: "数据库",
//     grade: 20,
//   });
//   gradeList.push({
//     course_name: "数据库",
//     grade: null,
//   });
// }
</script>
<style scoped>
.level1 {
  color: rgb(11, 176, 121);
  font-size: large;
  font-weight: 400;
}
.level2 {
  color: rgb(219, 239, 67);
  font-size: large;
  font-weight: 400;
}

.level3 {
  color: rgb(230, 97, 20);
  font-size: large;
  font-weight: 400;
}

.level4 {
  color: rgb(230, 24, 20);
  font-size: large;
  font-weight: 400;
}

.level5 {
  color: rgb(138, 142, 141);
  font-size: large;
  font-weight: 400;
}
</style>