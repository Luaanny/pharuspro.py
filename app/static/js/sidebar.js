const sideBar = document.querySelector('.sidebar');
const sideBarText = document.querySelectorAll('.item-description')
const main = document.querySelector("main")

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