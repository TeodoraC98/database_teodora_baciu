
const toggleEls=document.querySelectorAll(".toggle_menu");
const closeToggleEles=document.querySelectorAll(".close");

toggleEls.forEach(item=>{
    item.addEventListener("click",(e)=>{
        // from the element that triggered the click event based on the id stored in the target.dataset.idToggle, 
        // is selected the element that needs to be toggled
        // e.target.dataset.idToggle stores the id of the element that needs to be toggled
        let id=e.target.dataset.idToggle;
        let toggledElem= document.querySelector(id);
        // the element is set visible to the user
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