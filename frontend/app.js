const { createApp, ref, onMounted } = Vue;

createApp({
    setup() {
        // Reactive State (Vue tracks these variables for live UI updates)
        const students = ref([]);
        const form = ref({ name: '', age: '', course: '' });
        const errorMessage = ref('');

        // Fetch students via studentService (Axios wrapper)
        const fetchStudents = async () => {
            try {
                students.value = await studentService.getAll();
            } catch (err) {
                errorMessage.value = "Failed to load students from backend.";
            }
        };

        // Submit form handler
        const handleAddStudent = async () => {
            try {
                errorMessage.value = '';
                await studentService.create(form.value);
                form.value = { name: '', age: '', course: '' }; // Clear input fields
                await fetchStudents();                          // Refresh list
            } catch (err) {
                errorMessage.value = err.response?.data?.error || "Error adding student.";
            }
        };

        // Delete handler
        const handleDeleteStudent = async (id) => {
            try {
                errorMessage.value = '';
                await studentService.delete(id);
                await fetchStudents(); // Refresh list
            } catch (err) {
                errorMessage.value = "Error deleting student.";
            }
        };

        // Lifecycle hook: runs automatically when the page finishes loading
        onMounted(fetchStudents);

        return {
            students,
            form,
            errorMessage,
            handleAddStudent,
            handleDeleteStudent
        };
    }
}).mount('#app');