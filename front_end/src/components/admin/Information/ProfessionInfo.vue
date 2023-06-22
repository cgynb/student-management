<template>
  <a-table
    :columns="columns"
    :data="data"
    @change="handleChange"
    :pagination="false"
    :style="{ height: '100%', width: '100%' }"
  >
    <template
      #name-filter="{
        filterValue,
        setFilterValue,
        handleFilterConfirm,
        handleFilterReset,
      }"
    >
      <div class="custom-filter">
        <a-space direction="vertical">
          <a-input
            :model-value="filterValue[0]"
            @input="(value) => setFilterValue([value])"
          />
          <div class="custom-filter-footer">
            <a-button @click="handleFilterConfirm">筛选</a-button>
            <a-button @click="handleFilterReset">重置</a-button>
          </div>
        </a-space>
      </div>
    </template>
  </a-table>
</template>
    
<script setup>
import { reactive, h } from "vue";
import { IconSearch } from "@arco-design/web-vue/es/icon";
import { getProfessions } from "@/api/admin";

const data = reactive([]);
getProfessions().then((res) => {
  for (let item of res) {
    item.key = item.id;
    data.push(item);
  }
});
const columns = [
  {
    title: "学院编号",
    dataIndex: "academy_id",
    sortable: {
      sortDirections: ["ascend", "descend"],
    },
  },
  {
    title: "专业编号",
    dataIndex: "id",
    sortable: {
      sortDirections: ["ascend", "descend"],
    },
  },
  {
    title: "专业名称",
    dataIndex: "name",
    filterable: {
      filter: (value, record) => record.name.includes(value),
      slotName: "name-filter",
      icon: () => h(IconSearch),
    },
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
    