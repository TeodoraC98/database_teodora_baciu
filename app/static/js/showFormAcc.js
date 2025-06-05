const containerAcc=document.querySelector(".container_create-acc");
const btnToggleFrmEls=document.querySelectorAll(".toggle_frm");
const frmAccEls=document.querySelectorAll(".frm_acc");
const frmLogIn=document.querySelector("#frm_log-in");
const frmCreateAcc=document.querySelector("#frm_create-acc")


// btnToggleFrmEls allows the user to navigate 
// between the login and registration forms based on the id of the form
btnToggleFrmEls.forEach(btn =>{
    btn.addEventListener("click",(e)=>{
        // e.target.dataset.idFrm = contain the id of the selected form
        let id=e.target.dataset.idFrm;
    
        switch(id){
            case 'frm_log-in':
                if(!frmLogIn.classList.contains("access_frm")){
                    frmLogIn.classList.add("access_frm")
                    if(frmCreateAcc.classList.contains("access_frm")){
                        frmCreateAcc.classList.remove("access_frm")
                    }
                 } 
                 break;
            case 'frm_create-acc':
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