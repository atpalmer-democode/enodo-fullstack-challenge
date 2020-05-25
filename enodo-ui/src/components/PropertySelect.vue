<template>
  <form>
    <el-autocomplete
      class="search-bar"
      placeholder="Address search..."
      :trigger-on-focus="false"
      :fetch-suggestions="fetchSuggestions"
      @select="selectProperty"
      v-model="current">
      <el-button class="add-button" slot="append" @click="addProperty();">Add</el-button>
    </el-autocomplete>
  </form>
</template>

<script>
import api from '@/services/api.js';
import Button from 'element-ui';

export default {
  data: () => ({
    current: '',
    selected: null,
  }),
  components: {
    Button,
  },
  methods: {
    async fetchSuggestions(text, cb) {
      this.selected = null;
      const apiResults = await api.complete(text);
      const values = apiResults.map(({fullAddress, id}) => ({
        value: fullAddress,
        id: id,
      }));
      cb(values);
    },

    selectProperty(item) {
      this.selected = item;
    },

    async addProperty() {
      if(!this.selected) {
        return;
      }
      this.$emit('add-property', this.selected.id);
    },
  },
};
</script>

<style>
.search-bar {
  width: 100%;
}

.el-autocomplete-suggestion li {
  font-family: sans-serif;
}
</style>
