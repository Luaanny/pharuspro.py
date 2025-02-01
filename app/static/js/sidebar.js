const sideBar = document.querySelector('.sidebar');
const sideBarText = document.querySelectorAll('.item-description')
const main = document.querySelector("main")

sideBar.addEventListener("mouseover", () => {
    sideBar.classList.add('open')
    main.style.marginLeft = '230px'
    sideBarText.forEach((text) => {
        text.classList.add('d-block')
    })
})

sideBar.addEventListener("mouseout", () => {
    sideBar.classList.remove('open')
    main.style.marginLeft = '80px'
    sideBarText.forEach((text) => {
        text.classList.remove('d-block')
    })
})