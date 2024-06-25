let navbar= document.querySelector('.navbar');
let faTime=document.querySelector('.fa-times');
let faTimes=document.querySelector('#fa_times');
let faBars= document.querySelector('.fa-bars');
let fa_Bars= document.querySelector('#fa_bars');
let header=document.querySelector('.header');
let body=document.querySelector('.body');
let main_body=document.querySelector('.main_body');
faTime.style.display='none'
faTimes.style.display='none'
function showMenu(){
    navbar.classList.toggle('show');
    if(faBars.style.display='block'){
        faBars.style.display='none';
        faTime.style.display='block'
    }
    header.style.width='20%'
    body.style.left='20%'
}
function closes(){
    navbar.classList.toggle('show');
    if(faTime.style.display='block'){
        faBars.style.display='block';
        faTime.style.display='none'
    }
    header.style.width='6%'
    body.style.left='6%'
}
function Show_second_menu(){
    navbar.classList.toggle('second_navbar_show');
    fa_Bars.style.display='none';
    faTimes.style.display='block'
    main_body.style.overflow='hidden';
}
function Close_second_menu(){
    navbar.classList.toggle('second_navbar_show');
    fa_Bars.style.display='block';
    faTimes.style.display='none'
    main_body.style.overflow='visible';
}

function Container(){
    Comment_slide(1);
}
function init(){
    setInterval(Container,20000);
}
addEventListener('load',init);

let index3=0;
function Comment_slide(s){
    let slide= document.getElementsByClassName('comments');
    index3+=s;
    if(index3>=slide.length){
        index3=0
    }
    if(index3<0){
        index3=slide.length-1;
    }
    for(let i=0; i<slide.length; i++){
        slide[i].style.display='none';
    }
    slide[index3].style.display='block';
}

function Select(){
    let single= document.getElementById('date')
    let Date= document.querySelector('.date')
    let main_date=document.getElementById('main_date')
    let value=single.value;
    if (value=='1'){
        Date.style.display='none';
        main_date.style.display='block';
    }
    else{
        Date.style.display='flex';
        main_date.style.display='none';
    }
}


function isBlank(field){
    if(field.length==0){
        return true;
    }
}

function validate(){
    let re=/^.+[a-z]\.[a-z]+(\.[a-z]+)?$/;
    let de=/^\+234\d{10}$/
    let fullName= document.querySelector('.fullName').value;
    let Email= document.querySelector('.Email').value;
    let phone= document.querySelector('.phone').value;
    let errorName= document.querySelector('.errorName');
    let errorEmail= document.querySelector('.errorEmail');
    let invalidemail= document.querySelector('.invalidemail');
    let invalidphone=document.querySelector('.invalidPhone');
    let errorPhone=document.querySelector('.errorPhone');
    if(isBlank(fullName.trim())){
        errorName.style.display='block';
    }
    else{
        errorName.style.display='none';
    }
    if(isBlank(Email.trim())){
        errorEmail.style.display='block';
        invalidemail.style.display='none'
    }
    else{
        errorEmail.style.display='none';
    }
    if(!Email.match(re)){
        invalidemail.style.display='block';
    }
    else{
        invalidemail.style.display='none';
    }
    if(isBlank(phone.trim())){
        errorPhone.style.display='block';
    }
    else{
        errorPhone.style.display='none';
    }
    if(!phone.match(de)){
        invalidphone.style.display='block';
    }
    else{
        invalidphone.style.display='none';
    }
    if ( isBlank(fullName.trim()) || isBlank(Email.trim()) || !Email.match(re) || isBlank(phone.trim()) || !phone.match(de) || isBlank(Password.trim())){
        return false;
    }
}