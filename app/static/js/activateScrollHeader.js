const navEl = document.getElementById("container-nav");
const bannerEl=document.querySelector("#banner__mala")
 const homeIntroObtion={ 
    rootMargin:"-100% 0px 0px 0px"
 };
 const homeIntroObserver = new  IntersectionObserver(function(entries, homeIntroObserver ){
    entries.forEach(entry=>{
         if(entry.isIntersecting){
            console.log("aixiiii")
            navEl.classList.add("nav__scrolled")
         }else{
            console.log("intersregft4yhecting")
           navEl.classList.remove("nav__scrolled")
         }
    })
 },
homeIntroObtion)
homeIntroObserver.observe(bannerEl)

