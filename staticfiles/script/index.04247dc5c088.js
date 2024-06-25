
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
    Home_slide(1);
    Gallery_slide(1);
    Event_slide(1);
}
function init(){
    setInterval(Container,20000);
}
addEventListener('load',init);

let index=0;
Home_slide(index)
function Home_slide(r){ 
    let slide= document.getElementsByClassName('slides');
    index+=r;
    if(index>=slide.length){
        index=0;
    }
    if(index<0){
        index=slide.length-1;
    }
    for(let i=0; i<slide.length; i++){
        slide[i].style.display='none';
    }
    slide[index].style.display='block';
}
let index1=0;
Gallery_slide(index1);
function Gallery_slide(m){
    let slide= document.getElementsByClassName('left_slide');
    index1+=m;
    if(index1>=slide.length){
        index1=0;
    }
    if(index1<0){
        index1=slide.length-1;
    }
    for(let i=0; i<slide.length; i++){
        slide[i].style.display='none';
    }
    slide[index1].style.display='block';
}
let index2=0;
Event_slide(index2);
function Event_slide(n){
    let slide= document.getElementsByClassName('right_slide');
    index2+=n;
    if(index2>=slide.length){
        index2=0
    }
    if(index2<0){
        index2=slide.length-1;
    }
    for(let i=0; i<slide.length; i++){
        slide[i].style.display='none';
    }
    slide[index2].style.display='block';
}
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