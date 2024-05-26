document.addEventListener('DOMContentLoaded', function() {

    // get all appropriate elements
    const dropdown1User = document.getElementById('dropdown1User');
    const dropdown2User = document.getElementById('dropdown2User');
    const textFieldUser = document.getElementById('textFieldUser');
    const submitBtnUser = document.getElementById('submitBtnUser');
    const clearBtnUser = document.getElementById('clearBtnUser');

    function checkFields() {
        // Check if all fields are filled

        if (dropdown1User.value.trim() && dropdown2User.value.trim() && textFieldUser.value.trim()) {
            submitBtnUser.disabled = false; // Enable the submit button
        } else {
            submitBtnUser.disabled = true; // Disable the submit button
        }
        // change which type of form fields are shown based on the type of constraint (checkbox vs regular constraint)
        if (dropdown1User.value.trim() == "typeBooks") {
            [...document.getElementsByClassName("regular")].forEach(element => element.classList.add("is-hidden"));
            [...document.getElementsByClassName("irregular")].forEach(element => element.classList.remove("is-hidden"));
        }
        else {
            [...document.getElementsByClassName("regular")].forEach(element => element.classList.remove("is-hidden"));
            [...document.getElementsByClassName("irregular")].forEach(element => element.classList.add("is-hidden"));
        }
 
    }

    // Add event listeners to each input field
    dropdown1User.addEventListener('change', checkFields);
    dropdown2User.addEventListener('change', checkFields);
    textFieldUser.addEventListener('input', checkFields);


    // Add event listener to the clear button

    clearBtnUser.addEventListener('click', function() {
        console.log("atleast this")
        dropdown1User.value = '';
        dropdown2User.value = '';
        textFieldUser.value = '';
        submitBtnUser.disabled = true; // Disable the submit button
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


