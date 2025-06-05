const containerCarouselEl=document.querySelector(".container_carousel");
const carouselEl=containerCarouselEl.querySelector(".carousel");
const slidesCarouselEls=carouselEl.querySelectorAll(".carousel-slide")
const containerDotsEl=containerCarouselEl.querySelector(".container-dots");
let indexCS=0;
// based on the number of slides inside the carousel, the function createDots() create the elements and insert them into the carousel
// The “dots” elements are used for navigation between the carousel slides
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
// the function selectes a new slide in the carousel by implementing the click event for buttons
// the user can navigate between carousel slides through the dots
const dotSelectSlide=(removeCurrentElementClass)=>{
  dotsEls.forEach((dot, index) =>{
   dot.addEventListener("click",()=>{
    // removeElementByClass removes the class of the current slide
      removeCurrentElementClass('current_slide');
      //  a new slide is selected
      slidesCarouselEls[index].classList.add("current_slide");
      // removeElementByClass removes the class of the current dot
      removeCurrentElementClass('current_dot');
        // the new dots is selected 
      dot.classList.add("current_dot");
      // indexCS saves the position of the current element, this position is used in the function automaticSlide()
      indexCS=index;
    })
})
 }

const removeCurrentElementClass=(classElem)=>{
  let currentElement=containerCarouselEl.querySelector(`.`+classElem);
  currentElement.classList.remove(classElem);
}

dotSelectSlide(removeCurrentElementClass);

// the function changes the slide every 4s

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

automatic(removeCurrentElementClass)