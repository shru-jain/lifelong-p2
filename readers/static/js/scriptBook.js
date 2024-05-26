document.addEventListener('DOMContentLoaded', function() {

    // get all appropriate elements
    const dropdown1Book = document.getElementById('dropdown1Book');
    const dropdown2Book = document.getElementById('dropdown2Book');
    const textFieldBook = document.getElementById('textFieldBook');
    const submitBtnBook = document.getElementById('submitBtnBook');
    const clearBtnBook = document.getElementById('clearBtnBook');


    function checkFields() {
        // Check if all fields are filled
        if (dropdown1Book.value.trim() && dropdown2Book.value.trim() && textFieldBook.value.trim()) {
            submitBtnBook.disabled = false; // Enable the submit button
        } else {
            submitBtnBook.disabled = true; // Disable the submit button
        }
 
    }

    // Add event listeners to each input field
    dropdown1Book.addEventListener('change', checkFields);
    dropdown2Book.addEventListener('change', checkFields);
    textFieldBook.addEventListener('input', checkFields);


    // Add event listener to the clear button
    clearBtnBook.addEventListener('click', function() {
        console.log("atleast this")
        dropdown1Book.value = '';
        dropdown2Book.value = '';
        textFieldBook.value = '';
        submitBtnBook.disabled = true; // Disable the submit button
    });
    // get all edit buttons
    const editButtons = document.querySelectorAll('.editButton');
    editButtons.forEach(function(button) {
        button.addEventListener('click', function() {
            console.log("edit button clicked")
            // Find the corresponding edit form container
            const editFormContainer = this.nextElementSibling;
            
            // Remove the 'is-hidden' class to show the form
            editFormContainer.classList.remove('is-hidden');
        });
    });

    // get all cancel buttons
    const cancelButtons = document.querySelectorAll('.cancelButton');
    cancelButtons.forEach(function(button) {
        button.addEventListener('click', function() {
            // Find the corresponding edit form container
            const editFormContainer = this.closest('.editFormContainer');
            
            // Add the 'is-hidden' class to hide the form
            editFormContainer.classList.add('is-hidden');
        });
    });

 
});


