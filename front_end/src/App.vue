<template>
  <a-layout class="container" :style="{ height: '100%', width: '100%' }">
    <a-layout-sider collapsible breakpoint="xl">
      <div class="logo" />
      <a-menu
        :default-selected-keys="['0_1']"
        :style="{ width: '100%' }"
        @menu-item-click="onClickMenuItem"
      >
      <a-menu-item key="0_1" v-if="store.login">
          个人信息
        </a-menu-item>
        <a-divider />
        <a-menu-item key="0_2" v-if="store.login && store.role === 'student'">
          课程表
        </a-menu-item>
        <a-menu-item key="0_3" v-if="store.login && store.role === 'student'">
          成绩单
        </a-menu-item>
        <a-menu-item key="0_10" v-if="store.login && store.role === 'admin'">
          学院列表
        </a-menu-item>
        <a-menu-item key="0_11" v-if="store.login && store.role === 'admin'">
          专业列表
        </a-menu-item>
        <a-menu-item key="0_12" v-if="store.login && store.role === 'admin'">
          班级列表
        </a-menu-item>
        <a-menu-item key="0_13" v-if="store.login && store.role === 'admin'">
          学生列表
        </a-menu-item>
        <a-menu-item key="0_14" v-if="store.login && store.role === 'admin'">
          课程列表
        </a-menu-item>
        <a-menu-item key="0_15" v-if="store.login && store.role === 'admin'">
          成绩列表
        </a-menu-item>
        <a-divider v-if="store.login && store.role === 'admin'"/>
        <a-menu-item key="0_4" v-if="store.login && store.role === 'admin'">
          导入学生信息
        </a-menu-item>
        <a-menu-item key="0_5" v-if="store.login && store.role === 'admin'">
          导入班级信息
        </a-menu-item>
        <a-menu-item key="0_6" v-if="store.login && store.role === 'admin'">
          导入专业信息
        </a-menu-item>
        <a-menu-item key="0_7" v-if="store.login && store.role === 'admin'">
          导入学院信息
        </a-menu-item>
        <a-menu-item key="0_8" v-if="store.login && store.role === 'admin'">
          导入成绩信息
        </a-menu-item>
        <a-menu-item key="0_9" v-if="store.login && store.role === 'admin'">
          安排课程
        </a-menu-item>
        <a-divider v-if="store.login && store.role === 'admin'"/>
        <a-menu-item key="0_16" v-if="store.login && store.role === 'admin'">
          录入成绩
        </a-menu-item>
        <a-menu-item key="0_17" v-if="store.login && store.role === 'admin'">
          修改学生信息
        </a-menu-item>
      </a-menu>
      <template #trigger="{ collapsed }">
        <IconCaretRight v-if="collapsed"></IconCaretRight>
        <IconCaretLeft v-else></IconCaretLeft>
      </template>
    </a-layout-sider>
    <a-layout>
      <a-layout-header style="padding-left: 20px"> </a-layout-header>
      <a-layout style="padding: 0 24px">
        <a-breadcrumb :style="{ margin: '16px 0' }">
          <a-breadcrumb-item>学生管理系统</a-breadcrumb-item>
        </a-breadcrumb>
        <a-layout-content>
          <router-view></router-view>
        </a-layout-content>
        <a-layout-footer></a-layout-footer>
      </a-layout>
    </a-layout>
  </a-layout>
</template>
<style scoped>
.container {
  height: 500px;
  background: var(--color-fill-2);
  border: 1px solid var(--color-border);
}
.container :deep(.arco-layout-sider) .logo {
  height: 32px;
  margin: 12px 8px;
  background: rgba(255, 255, 255, 0.2);
}
.container :deep(.arco-layout-sider-light) .logo {
  background: var(--color-fill-2);
}
.container :deep(.arco-layout-header) {
  height: 64px;
  line-height: 64px;
  background: var(--color-bg-3);
}
.container :deep(.arco-layout-footer) {
  height: 48px;
  line-height: 48px;
}
.container :deep(.arco-layout-content) {
  background: var(--color-bg-3);
}
.container :deep(.arco-layout-footer),
.container :deep(.arco-layout-content) {
  display: flex;
  flex-direction: column;
  justify-content: center;
  text-align: center;
}
</style>
<script setup>
import { Message } from "@arco-design/web-vue";
import { IconCaretRight, IconCaretLeft } from "@arco-design/web-vue/es/icon";
import { ref, reactive } from 'vue';
import { useUserStore } from "@/store/user";
import { useRouter } from 'vue-router';

const store = useUserStore();
const router = useRouter();

// 点击目录
const onClickMenuItem = (key) => {
//   Message.info({ content: `You select ${key}`, showIcon: true });
  switch(key){
    case "0_1":
        if(store.role == "student"){
            router.push("/student/info");
        }else if(store.role == "admin"){
            router.push("/admin/info");
        }
        break;
    case "0_2":
        router.push("/student/course");
        break;
    case "0_3":
        router.push("/student/grade");
        break;
    case "0_4":
        router.push("/admin/import/student");
        break;
    case "0_5":
        router.push("/admin/import/class");
        break;
    case "0_6":
        router.push("/admin/import/profession");
        break;
    case "0_7":
        router.push("/admin/import/academy");
        break;
    case "0_8":
        router.push("/admin/import/grade");
        break;
    case "0_9":
        router.push("/admin/import/course");
        break;
    case "0_10":
        router.push("/admin/information/academy");
        break;
    case "0_11":
        router.push("/admin/information/profession");
        break;
    case "0_12":
        router.push("/admin/information/class");
        break;
    case "0_13": 
        router.push("/admin/information/student");
        break;
    case "0_14":
        router.push("/admin/information/course");
        break;
    case "0_15":
        router.push("/admin/information/grade");
        break;
    case "0_16": 
        router.push("/admin/modify/grade");
        break;
    case "0_17": 
        router.push("/admin/modify/student");
        break;
  }
};
</script>