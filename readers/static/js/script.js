document.addEventListener('DOMContentLoaded', function() {
    document.getElementById("users-tab").addEventListener('click', (e) => {

        document.getElementById("users-tab").classList.add("is-selected");
        document.getElementById("books-tab").classList.remove("is-selected");
        document.getElementById("users-content").classList.remove("is-hidden");
        document.getElementById("books-content").classList.add("is-hidden");

    })
    document.getElementById("books-tab").addEventListener('click', (e) => {

        document.getElementById("books-tab").classList.add("is-selected");
        document.getElementById("users-tab").classList.remove("is-selected");
        document.getElementById("books-content").classList.remove("is-hidden");
        document.getElementById("users-content").classList.add("is-hidden");

    })

    const dropdown1Book = document.getElementById('dropdown1Book');
    const dropdown2Book = document.getElementById('dropdown2Book');
    const textFieldBook = document.getElementById('textFieldBook');
    const submitBtnBook = document.getElementById('submitBtnBook');
    const clearBtnBook = document.getElementById('clearBtnBook');

    const dropdown1User = document.getElementById('dropdown1User');
    const dropdown2User = document.getElementById('dropdown2User');
    const textFieldUser = document.getElementById('textFieldUser');
    const submitBtnUser = document.getElementById('submitBtnUser');
    const clearBtnUser = document.getElementById('clearBtnUser');

    function checkFields() {
        // Check if all fields are filled
        if (dropdown1Book.value.trim() && dropdown2Book.value.trim() && textFieldBook.value.trim()) {
            submitBtnBook.disabled = false; // Enable the submit button
        } else {
            submitBtnBook.disabled = true; // Disable the submit button
        }

        if (dropdown1User.value.trim() && dropdown2User.value.trim() && textFieldUser.value.trim()) {
            submitBtnUser.disabled = false; // Enable the submit button
        } else {
            submitBtnUser.disabled = true; // Disable the submit button
        }

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
    dropdown1Book.addEventListener('change', checkFields);
    dropdown2Book.addEventListener('change', checkFields);
    textFieldBook.addEventListener('input', checkFields);

    dropdown1User.addEventListener('change', checkFields);
    dropdown2User.addEventListener('change', checkFields);
    textFieldUser.addEventListener('input', checkFields);


    // Add event listener to the clear button
    clearBtnBook.addEventListener('click', function() {
        console.log("atleast this")
        dropdown1Book.value = '';
        dropdown2Book.value = '';
        textFieldBook.value = '';
        submitBtnBook.disabled = true; // Disable the submit button
    });

    clearBtnUser.addEventListener('click', function() {
        console.log("atleast this")
        dropdown1User.value = '';
        dropdown2User.value = '';
        textFieldUser.value = '';
        submitBtnUser.disabled = true; // Disable the submit button
    });
 
});


