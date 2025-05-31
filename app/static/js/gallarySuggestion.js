const containerSgEl=document.querySelector(".container_suggestion")
const gallary =  document.querySelector(".container_gallary")
const items = gallary.querySelectorAll(".gallary_item")
const btnNext = gallary.querySelector("#next")
const btnPrev = gallary.querySelector("#prev")
let parentWidth = containerSgEl.clientWidth
let childWidth
setWidthEls(6)
const gallaryObserver={
  rootMargin:"-200px 0px 0px 0px"
}
const resizeGallaryObserver = new ResizeObserver((entries) =>{
  entries.forEach(entry =>{
      if(entry.target.clientWidth < 400 &&   entry.target.dataset.numarItems != 2){
         parentWidth = 460
        entry.target.dataset.numarItems = 2
        setWidthEls(2)
      }
      else if(entry.target.clientWidth > 1000 && entry.target.dataset.numarItems != 6){
         parentWidth = 1600
         entry.target.dataset.numarItems = 6
         console.log(6)
        setWidthEls(6)
      }
      else if((1000 >  entry.target.clientWidth  && entry.target.clientWidth > 400) && entry.target.dataset.numarItems != 4){
          parentWidth = 1000
          entry.target.dataset.numarItems = 4
          console.log(4)
          setWidthEls(4)
      }
  })
})
const intersectionGallaryObs = new IntersectionObserver(function(entries,intersectionGallaryObs){
entries.forEach(entry =>{
  if(entry.isIntersecting){
    resizeGallaryObserver.observe(gallary)
  }else{
    resizeGallaryObserver.unobserve(gallary)
  } })
},
gallaryObserver )

intersectionGallaryObs.observe(gallary)

function setWidthEls(divide){
   childWidth = Math.floor(parentWidth/divide)
    items.forEach(item =>{
      item.style.width = `${childWidth}px`
    })
  
}

containerSgEl.addEventListener("wheel",(e)=>{
  console.log("im doing someting")
    e.preventDefault();
    containerSgEl.scrollLeft += e.deltaY;
     containerSgEl.style.scrollBehavior = "auto"
})
btnNext.addEventListener('click',(e)=>{
  console.log("next")
  containerSgEl.style.scrollBehavior = "smooth"
  containerSgEl.scrollLeft +=  childWidth;
})
btnPrev.addEventListener('click',(e)=>{
  containerSgEl.style.scrollBehavior = "smooth"
  containerSgEl.scrollLeft -= childWidth;
})