const navEl = document.getElementById("container-nav");
const bannerEl=document.querySelector("#banner__mala")
 const homeIntroObtion={ 
    rootMargin:"-100% 0px 0px 0px"
 };
//  Because I want the navigation to be transparent on the Home page, but when the user scrolls down, 
// it should change the background, I use IntersectionObserver to monitor when the navigation intersects with the banner
 const homeIntroObserver = new  IntersectionObserver(function(entries, homeIntroObserver ){
    entries.forEach(entry=>{
         if(entry.isIntersecting){
            // when the navigation intersects the banner
            // the background of the navigation is transparent
            navEl.classList.add("nav__scrolled")
         }else{
           navEl.classList.remove("nav__scrolled")
         }
    })
 },
homeIntroObtion)
homeIntroObserver.observe(bannerEl)

