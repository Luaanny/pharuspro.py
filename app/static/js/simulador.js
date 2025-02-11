const devicesToggle = document.querySelector('#devicesToggle')
const devicesList = document.querySelector("#devicesList")

function showDevices () {
    devicesList.style.transform = 'translate(0, -50%)'
}

devicesToggle.addEventListener('mouseover', showDevices)