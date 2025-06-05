const headerEl = document.getElementById("header");
 const main=document.querySelector("main")
 const homeIntroObtion={ 
    rootMargin:"10px 0px 0px 0px"
 };
 const homeIntroObserver= new  IntersectionObserver(function(entries, homeIntroObserver ){
    entries.forEach(entry=>{
         if(!entry.isIntersecting){
            headerEl.classList.add("header__scrolled")
         }else{
            headerEl.classList.remove("header__scrolled")
         }
    })
 },
homeIntroObtion)
homeIntroObserver.observe(main)