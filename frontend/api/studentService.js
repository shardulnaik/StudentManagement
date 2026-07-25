// Centralized Axios Service Module
const API_BASE_URL = "http://127.0.0.1:5000/students";

const studentService = {
    // 1. GET Request
    async getAll() {
        const response = await axios.get(API_BASE_URL);
        return response.data; // Returns parsed JSON array from Flask
    },

    // 2. POST Request
    async create(studentData) {
        const response = await axios.post(API_BASE_URL, studentData);
        return response.data;
    },

    // 3. DELETE Request
    async delete(id) {
        const response = await axios.delete(`${API_BASE_URL}/${id}`);
        return response.data;
    }
};