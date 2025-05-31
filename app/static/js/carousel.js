const containerCarouselEl=document.querySelector(".container_carousel");
const carouselEl=containerCarouselEl.querySelector(".carousel");
const slidesCarouselEls=carouselEl.querySelectorAll(".carousel-slide")
const containerDotsEl=containerCarouselEl.querySelector(".container-dots");
let indexCS=0;
createDots=()=>{
    for(let index=0; index<slidesCarouselEls.length;index++){
       if(index==0){
        containerDotsEl.insertAdjacentHTML("beforeend",`
          <div class="carousel-dot current_dot"></div>`)
       }else{
        containerDotsEl.insertAdjacentHTML("beforeend",`
          <div class="carousel-dot"></div>`)
       }
    }
    
}
createDots();

const dotsEls=containerCarouselEl.querySelectorAll(".carousel-dot");

 const dotSelectSlide=(removeElementByClass)=>{
  dotsEls.forEach((dot, index) =>{
   dot.addEventListener("click",()=>{
      removeElementByClass('current_slide');
      slidesCarouselEls[index].classList.add("current_slide");
      removeElementByClass('current_dot');
      dot.classList.add("current_dot");
      indexCS=index;

    })
})
 }

const removeElementByClass=(classElem)=>{
  let currentElement=containerCarouselEl.querySelector(`.`+classElem);
  currentElement.classList.remove(classElem);
}

dotSelectSlide(removeElementByClass);

function automatic(removeS){
  const automaticSlide = () =>{
    removeS("current_slide");
   slidesCarouselEls[indexCS].classList.add("current_slide");
   removeS("current_dot");
   dotsEls[indexCS].classList.add("current_dot");
   if(indexCS < slidesCarouselEls.length-1){
     indexCS++;
   }
   else{
     indexCS=0;
   }
     setTimeout(automaticSlide,4000)
 }
 automaticSlide();
}

// automatic(removeElementByClass)