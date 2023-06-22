<template>
  <a-form :model="form" :style="{ width: '600px' }" @submit="handleSubmit">
    <a-form-item field="name" label="学院名称">
      <a-input v-model="form.name" placeholder="学院名称" />
    </a-form-item>
    <a-form-item field="gender" label="院长">
      <a-input v-model="form.dean" placeholder="院长" />
    </a-form-item>
    <a-form-item>
      <a-button html-type="submit">导入</a-button>
    </a-form-item>
  </a-form>
</template>
    
<script setup>
import { reactive } from "vue";
import { importAcademy } from '@/api/admin';
const form = reactive({
  name: "",
  dean: "",
});
const handleSubmit = (data) => {
  importAcademy(data.values.name, data.values.dean);
};
</script>
    