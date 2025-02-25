let editButton = document.querySelector('#editButton')
let saveButton = document.querySelector('#saveButton')
let inputs = document.querySelectorAll('input')
let deleteButton = document.querySelector("#deleteButton")
let cancelButton = document.querySelector('#cancelButton')

function enableEditting() {
    inputs.forEach(input => {
        input.removeAttribute("disabled");

    });
    editButton.classList.add('d-none');
    deleteButton.classList.add('d-none')
    saveButton.classList.remove('d-none');
    cancelButton.classList.remove('d-none');
}

function save() {
    let form = document.querySelector('form');

    form.submit()

    inputs.forEach(input => {
        input.setAttribute('disabled', "disabled");
    });

    editButton.classList.remove('d-none');
    deleteButton.classList.remove('d-none');
    saveButton.classList.add('d-none');
    cancelButton.classList.add('d-none');
}

function cancel() {
    let form = document.querySelector('form')

    form.reset()

    inputs.forEach(input => {
        input.setAttribute('disabled', "disabled");
    });

    editButton.classList.remove('d-none');
    deleteButton.classList.remove('d-none');
    saveButton.classList.add('d-none');
    cancelButton.classList.add('d-none');
}

function deleteUser() {
    const userId = deleteButton.getAttribute("data-user-id")

    if (!confirm("Tem certeza que deseja excluir sua conta? Esta ação não pode ser desfeita.")) {
        return;
    }

    console.log('deletando...')
    fetch(`user/delete/${userId}`, {
        method: "DELETE",
        credentials: "include"
    })
        .then(response => response.text())
        .then(text => {
            console.log("Resposta do servidor:", text);
            return JSON.parse(text);
        })
        .then(data => {
            if (data.message) {
                window.location.href = "/";
            }
        })
        .catch(error => console.error("Erro:", error));
}