const containerSgEl=document.querySelector(".container_suggestion")
const gallary =  document.querySelector(".container_gallary")
const items = gallary.querySelectorAll(".gallary_item")
const btnNext = gallary.querySelector("#next")
const btnPrev = gallary.querySelector("#prev")
let parentWidth = containerSgEl.clientWidth
let slideWidth
setWidthEls(6)
const gallaryObserver={
  rootMargin:"-200px 0px 0px 0px"
}

const resizeGallaryObserver = new ResizeObserver((entries) =>{
  entries.forEach(entry =>{
    //with entry.target.dataset.nrItems  is checked the number of the items that shoud be set to the gallery container
    // if the gallery width is smaller than 400, but the  entry.target.dataset.nrItems is different from 2, then setWidthEls(2) is called
      if(entry.target.clientWidth < 400 &&   entry.target.dataset.nrItems != 2){
         parentWidth = 460
        entry.target.dataset.nrItems = 2
        // setWidthEls(2) sets the new width of the gallery's elements 
        setWidthEls(2)
      }
      else if(entry.target.clientWidth > 1000 && entry.target.dataset.nrItems != 6){
        // if the gallery width isbigger than 1000, but the  entry.target.dataset.nrItems is different from 6, then setWidthEls(6) is called
         parentWidth = 1600
         entry.target.dataset.nrItems = 6
         // setWidthEls(6) sets the new width of the gallery's elements 
        //  new width =  1600/6
        setWidthEls(6)
      }
      else if((1000 >  entry.target.clientWidth  && entry.target.clientWidth > 400) && entry.target.dataset.nrItems != 4){
          
          parentWidth = 1000
          entry.target.dataset.nrItems = 4
          setWidthEls(4)
      }
  })
})

// the observer intersectionGallaryObs, detects if the gallery is intersecting the viewport
const intersectionGallaryObs = new IntersectionObserver(function(entries,intersectionGallaryObs){
entries.forEach(entry =>{
  if(entry.isIntersecting){
    // if the gallery is intersecting the viewport, then the resizeGallaryObserver is called
    // resizeGallaryObserver is detects the width change of the gallery, making the changes of the slides based on the width
    resizeGallaryObserver.observe(gallary)
  }else{
    // when the gallery is not intersecting on the viewport, then the resizeGallaryObserver is set to unobserve
    resizeGallaryObserver.unobserve(gallary)
  } })
},
gallaryObserver )

intersectionGallaryObs.observe(gallary)

// depending on the screen dimension, the function calculates and 
// sets the number of the slides that can be visible in the same time to the user
// for large screens the number of the slides is 6
// for medium screens the number of the slides is 4
// for small devices the number of the slides is 2
function setWidthEls(divide){
   slideWidth = Math.floor(parentWidth/divide)
    items.forEach(item =>{
      item.style.width = `${slideWidth}px`
    })
}


containerSgEl.addEventListener("wheel",(e)=>{
    e.preventDefault();
    containerSgEl.scrollLeft += e.deltaY;
    containerSgEl.style.scrollBehavior = "auto"
})

btnNext.addEventListener('click',(e)=>{
  containerSgEl.style.scrollBehavior = "smooth"
  containerSgEl.scrollLeft +=  slideWidth;
})

btnPrev.addEventListener('click',(e)=>{
  containerSgEl.style.scrollBehavior = "smooth"
  containerSgEl.scrollLeft -= slideWidth;
})