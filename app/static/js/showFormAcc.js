const containerAcc=document.querySelector(".container_create-acc");
const btnToggleFrmEls=containerAcc.querySelectorAll(".toggle_frm");
const frmAccEls=containerAcc.querySelectorAll(".frm_acc");
const frmLogIn=containerAcc.querySelector("#frm_log-in");
const frmCreateAcc=containerAcc.querySelector("#frm_create-acc")

btnToggleFrmEls.forEach(btn =>{
    btn.addEventListener("click",(e)=>{
        console.log(e.target.dataset.idFrm)
        let id=e.target.dataset.idFrm;
    
        switch(id){
            case 'frm_log-in':
                console.log("case1")
                if(!frmLogIn.classList.contains("access_frm")){
                    console.log("case1")
                    frmLogIn.classList.add("access_frm")
                    if(frmCreateAcc.classList.contains("access_frm")){
                        frmCreateAcc.classList.remove("access_frm")
                    }
                 } 
                 break;
            case 'frm_create-acc':
                console.log("case2")
                if(!frmCreateAcc.classList.contains("access_frm")){
                    frmCreateAcc.classList.add("access_frm")
                    if(frmLogIn.classList.contains("access_frm")){
                        frmLogIn.classList.remove("access_frm")
                    }
                 }
                 break; 
        }
    
    })
})