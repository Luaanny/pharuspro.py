let editButton = document.querySelector('#editButton')
let saveButton = document.querySelector('#saveButton')
let inputs = document.querySelectorAll('input')
let deleteButton = document.querySelector("#deleteButton")

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

function deleteUser() {
    const userId = deleteButton.getAttribute("data-user-id")

    if (!confirm("Tem certeza que deseja excluir sua conta? Esta ação não pode ser desfeita.")) {
        return;
    }

    fetch(`/delete/${userId}`, {
        method: "DELETE",
        credentials: "include"
    })
        .then(response => response.text()) // Primeiro, obtemos a resposta como texto
        .then(text => {
            console.log("Resposta do servidor:", text); // Verifica o que o Flask está retornando
            return JSON.parse(text); // Depois, tentamos converter para JSON
        })
        .then(data => {
            if (data.message) {
                window.location.href = "/";
            }
        })
        .catch(error => console.error("Erro:", error));

}