const navbtn = document.querySelector('.navbtn')
const nav = document.querySelector('.nav')
navbtn.onclick = function(){
    this.classList.toggle('active');
    nav.classList.toggle('active');
}

let contactbtn = document.querySelector('.contactbtn')
const contact = document.querySelector('.contact')
contactbtn.onclick = function(){
    this.classList.toggle('active');
    contact.classList.toggle('active');
}

let date = new Date();
console.log(date.getFullYear());
document.getElementsByClassName('year').innerHTML = date.getFullYear();
console.log(date.getFullYear());
