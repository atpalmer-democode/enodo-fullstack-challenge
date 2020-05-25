import axios from 'axios';


const BASE_URL = 'http://localhost:5000/';


class Api {
  async complete(text) {
    const result = await axios.get(`${BASE_URL}/api/complete`, { params: { text } });
    return result.data['properties'];
  }

  async selections() {
    const result = await axios.get(`${BASE_URL}/api/selections`);
    return result.data['selections'];
  }

  async delete(propertyId) {
    await axios.delete(`${BASE_URL}/api/selections/${propertyId}`);
  }

  async putSelection(propertyId) {
    await axios.put(`${BASE_URL}/api/selections/${propertyId}`);
  }
}

export default new Api();
