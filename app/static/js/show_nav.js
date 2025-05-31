
const toggleEls=document.querySelectorAll(".toggle_menu");
const closeToggleEles=document.querySelectorAll(".close");
toggleEls.forEach(item=>{
    item.addEventListener("click",(e)=>{
            console.log("click")
        let id=e.target.dataset.idToggle;
        console.log(id)
        let toggledElem= document.querySelector(id);
        if(toggledElem!=null)
            toggledElem.classList.toggle("visible")

    })
})

closeToggleEles.forEach(btn=>{
    btn.addEventListener("click",(e)=>{
        let parent =e.target.offsetParent;
        parent.classList.toggle("visible")
    })
})