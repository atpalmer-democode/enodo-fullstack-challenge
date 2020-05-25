<template>
  <div>
    <PageHeading heading="Select Properties"/>    
    <div class="property-select">
      <h2>Find a Property</h2>
      <PropertySelect @add-property="addProperty"/>
    </div>
    <div class="property-table">
      <h2>Selected Properties</h2>
      <PropertiesTable :rows="rows" @delete-property="deleteProperty"/>
    </div>
  </div>
</template>

<script>
import PropertiesTable from '@/components/PropertiesTable';
import PageHeading from '@/components/PageHeading';
import PropertySelect from '@/components/PropertySelect';
import api from '@/services/api';

export default {
  components: {
    PropertiesTable,
    PageHeading,
    PropertySelect,
  },
  data: () => ({
    rows: [],
  }),
  methods: {
    async addProperty(propertyId) {
      await api.putSelection(propertyId);
      this.rows = await api.selections();
    },

    async deleteProperty(propertyId) {
      await api.delete(propertyId);
      this.rows = await api.selections();
    }
  },
  async mounted() {
    this.rows = await api.selections();
  },
};
</script>

<style scoped>
.property-select {
  width: 80%;
  margin: auto;
  padding: 20px;
}

.property-table {
  width: 80%;
  margin: auto;
  padding: 20px;
}
</style>
