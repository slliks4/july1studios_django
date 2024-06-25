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

let link=document.getElementsByClassName('link')

function AddActive(){
   const links = document.querySelectorAll("category_link")
    links.forEach(link => {
        link.addEventListener('click', ()=>{
            link.classList.add("active")
        })
    })
} 