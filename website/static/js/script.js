// Add form-control class to Django password form fields
// This is used on the change_password page
document.addEventListener('DOMContentLoaded', function() {
    // Add form-control class to Django form fields
    document.querySelectorAll('input[type="password"]').forEach(function(input) {
        input.classList.add('form-control');
    });
});

// Toggle edit form for tasks on day_detail page
function toggleEdit(taskId) {
    const taskItem = document.getElementById('task-' + taskId);
    const editForm = document.getElementById('edit-form-' + taskId);

    if (editForm.style.display === 'none') {
        editForm.style.display = 'flex';
        taskItem.style.display = 'none';
    } else {
        editForm.style.display = 'none';
        taskItem.style.display = 'flex';
    }
}
