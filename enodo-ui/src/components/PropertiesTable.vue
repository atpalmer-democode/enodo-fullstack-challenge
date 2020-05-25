<template>
  <div v-if="!rows.length" class="no-properties">
    No Properties Currently Selected
  </div>

  <el-table v-else :data="rows" style="word-break: normal;">
    <el-table-column label="Full Address" prop="fullAddress"></el-table-column>
    <el-table-column label="Class Description" prop="classDescription"></el-table-column>
    <el-table-column width="80" label="Delete">
      <template slot-scope="scope">
        <el-button type="danger" icon="el-icon-delete" circle="circle" @click="deleteProperty(scope);"></el-button>
      </template>
    </el-table-column>
  </el-table>
</template>

<script>
import api from '@/services/api';

export default {
  props: {
    rows: Array,
  },
  
  methods: {
    async deleteProperty(scope) {
      this.$emit('delete-property', scope.row.id);
    }
  },
}
</script>

<style>
.el-table .cell {
  /* override element.js selector */
  word-break: normal;
}

.no-properties {
  color: #6a6a6a;
}
</style>
