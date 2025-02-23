function enableEditing(deviceId) {
    const form = document.querySelector(`.updateDeviceForm[data-device-id="${deviceId}"]`);
    const editButton = document.querySelector(`#deviceEdit${deviceId}`);
    const saveButton = document.querySelector(`#saveButton${deviceId}`);
    const inputs = form.querySelectorAll('.card-text');

    console.log(editButton, saveButton);

    inputs.forEach(input => {
        input.removeAttribute("disabled");
    });

    editButton.classList.add('d-none');
    saveButton.classList.remove('d-none');
}

function save(deviceId) {
    const form = document.querySelector(`.updateDeviceForm[data-device-id="${deviceId}"]`);
    const editButton = document.querySelector(`#deviceEdit${deviceId}`);
    const saveButton = document.querySelector(`#saveButton${deviceId}`);
    const inputs = form.querySelectorAll('.card-text');

    inputs.forEach(input => {
        input.setAttribute("disabled", 'disabled');
    });

    editButton.classList.remove('d-none');
    saveButton.classList.add('d-none')
    form.addEventListener('submit', function (event) {
        event.preventDefault();

        const potency = form.querySelector(`#new_potency${deviceId}`).value;
        const timeInterval = form.querySelector(`#new_time_interval${deviceId}`).value;

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
                    form.reset()
                    window.location.reload()
                } else {
                    window.location.reload();
                }
            })
            .catch(error => {
                console.error('Erro:', error);
                alert('Ocorreu um erro ao atualizar o dispositivo.');
            });
    });
}

function deleteDevice(deviceId) {
    if (!confirm("Tem certeza que deseja excluir esse aparelho? Esta ação não pode ser desfeita.")) {
        return;
    }

    fetch(`/consumo/delete/${deviceId}`, {
        method: "DELETE",
        credentials: "include"
    })
        .then(response => response.json())
        .then(data => {
            if (data.message) {
                window.location.href = "/simulador";
            }
        })
        .catch(error => console.error("Erro:", error));
}