document.addEventListener('DOMContentLoaded', function() {
    // document.getElementById("users-tab").addEventListener('click', (e) => {

    //     document.getElementById("users-tab").classList.add("is-selected");
    //     document.getElementById("books-tab").classList.remove("is-selected");
    //     document.getElementById("users-content").classList.remove("is-hidden");
    //     document.getElementById("books-content").classList.add("is-hidden");

    // })
    // document.getElementById("books-tab").addEventListener('click', (e) => {

    //     document.getElementById("books-tab").classList.add("is-selected");
    //     document.getElementById("users-tab").classList.remove("is-selected");
    //     document.getElementById("books-content").classList.remove("is-hidden");
    //     document.getElementById("users-content").classList.add("is-hidden");

    // })

    const dropdown1Book = document.getElementById('dropdown1Book');
    const dropdown2Book = document.getElementById('dropdown2Book');
    const textFieldBook = document.getElementById('textFieldBook');
    const submitBtnBook = document.getElementById('submitBtnBook');
    const clearBtnBook = document.getElementById('clearBtnBook');


    function checkFields() {
        console.log("reached here")
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

 
});


