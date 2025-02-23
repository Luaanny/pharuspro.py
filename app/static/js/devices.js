const deleteButton = document.querySelector('#deviceDeleteBtn')

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