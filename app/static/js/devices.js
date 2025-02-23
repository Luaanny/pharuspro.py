const deleteButton = document.querySelector('#deviceDeleteBtn')
const editButton = document.querySelector('#deviceEdit')
const saveButton = document.querySelector('#saveButton')
const inputs = document.querySelectorAll('.card-text')

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

    let form = document.querySelector('#updateDeviceForms');

    form.addEventListener('submit', function (event) {
        console.log('entrou')
        event.preventDefault();
        console.log('entrou aq tmb')

        const deviceId = form.getAttribute('data-device-id');
        const potency = form.querySelector('#new_potency').value;
        const timeInterval = form.querySelector('#new_time_interval').value;

        fetch(`/update_device/${deviceId}`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                potency: potency,
                time_interval: timeInterval,
            }),
        })
            .then(response => response.json())
            .then(data => {
                if (data.error) {
                    console.error('Erro:', data);
                } else {
                    window.location.reload();
                }
            })
            .catch(error => {
                console.error('Erro:', error);
            });
    });
}

function deleteDevice() {
    const deviceID = deleteButton.getAttribute("data-device-id")

    if (!confirm("Tem certeza que deseja excluir esse aparelho? Esta ação não pode ser desfeita.")) {
        return;
    }

    fetch(`/consumo/delete/${deviceID}`, {
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
                window.location.href = "/simulador";
            }
        })
        .catch(error => console.error("Erro:", error));
}