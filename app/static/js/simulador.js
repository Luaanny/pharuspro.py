const devicesToggle = document.querySelector('#devicesToggle')
const devicesList = document.querySelector("#devicesList")
const cardListCLose = document.querySelector('#cardListClose')

function showDevices () {
    devicesList.classList.add('enter')
    devicesList.classList.remove('exit')
    devicesToggle.classList.add('d-none')
}

function hideDevices () {
    devicesList.classList.add('exit')
    devicesList.classList.remove('enter')
    devicesToggle.classList.remove('d-none')
}

devicesToggle.addEventListener('mouseover', showDevices)
cardListCLose.addEventListener('click', hideDevices)