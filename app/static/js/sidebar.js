const sideBar = document.querySelector('.sidebar');
const sideBarText = document.querySelectorAll('.item-description')

sideBar.addEventListener("mouseover", () => {
    sideBar.classList.add('open')
    sideBarText.forEach((text) => {
        text.classList.add('d-block')
    })
})

sideBar.addEventListener("mouseout", () => {
    sideBar.classList.remove('open')
    sideBarText.forEach((text) => {
        text.classList.remove('d-block')
    })
})