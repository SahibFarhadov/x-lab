// sifreni goster elementin alinmasi
let sifreni_goster_element = document.getElementById("id_sifreni_goster");
let id_password1 = document.getElementById("id_password1");

sifreni_goster_element.onchange = function(){
    if(sifreni_goster_element.checked){
        id_password1.setAttribute("type","text");
    }
    else{
        id_password1.setAttribute("type","password");
    }
}

