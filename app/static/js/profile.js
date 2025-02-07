let editButton = document.querySelector('#editButton')
let saveButton = document.querySelector('#saveButton')
let inputs = document.querySelectorAll('input')

function enableEditting() {
    inputs.forEach(input => {
        input.removeAttribute("disabled");

    });

    editButton.classList.add('d-none');
    saveButton.classList.remove('d-none');

}

function save() {

    inputs.forEach(input => {
        input.setAttribute('disabled', "disabled");
    });

    editButton.classList.remove('d-none');
    saveButton.classList.add('d-none');
}