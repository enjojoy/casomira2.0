// const zapis_btn = document.querySelector(".btn-zapis");

// zapis_btn.addEventListener('click', zapis)

// function zapis(event){
//     console.log('Ypu are trying to sign in')
//     event.preventDefault();
// }

var inputs = document.getElementsByTagName('input');

function onLoad(){
for (var i=0; i<inputs.length; i++)  {
  if (inputs[i].type == 'checkbox')   {
    inputs[i].checked = false;
  }
}
}

// var aircraft_choosen = [];
// console.log("aircraft choosen length" + aircraft_choosen.length);
// console.log("person choosen length" + person_choosen.length);
// console.log(document.querySelectorAll('input[name=person_choosen]:checked'));


// var person_choosen = [];
// person_choosen = $("input[name=person_choosen]").change(function(){
//     var l = document.querySelectorAll('input[name=person_choosen]:checked');
//     console.log(l.length)
//     if(l.length === 0){
//         return [];
//     }else{
//         return document.querySelectorAll('input[name=person_choosen]:checked')
//     }
// });    
    
// var person_choosen = [];

// person_choosen = $("input[name=person_choosen]:checked").change(function(){
//     console.log(l)
//     var l = document.querySelectorAll('input[name=person_choosen]:checked');

//     console.log(l.length)
//     if(l.length === 0){
//         return [];
//     }else{
//         return document.querySelectorAll('input[name=person_choosen]:checked')
//     }
// }).get();        
// console.log(person_choosen)

// aircraft_choosen = $('input[name=aircraft_choosen]:checked').change(function(){
//     console.log(document.querySelectorAll('input[name=aircraft_choosen]:checked'))
//     return document.querySelectorAll('input[name=aircraft_choosen]:checked');
//     }).get();



zapis_btn = document.getElementById('zapis-btn');
error = document.getElementById('error');

function zapis(event){
        p=$("input[name=person_choosen]:checked").get();
        a=$('input[name=aircraft_choosen]:checked').get();
        console.log($("input[name=person_choosen]:checked").get());
        console.log($('input[name=aircraft_choosen]:checked').get());

        if ( p.length < 2  || a.length < 1){
            if(error.classList.contains('active')){
                console.log("The requirement is not met!")
                event.preventDefault();
                } else{
                    error.classList.add('active')
                    console.log("The requirement is not met!")
                    event.preventDefault();
            }
        // }if(person_choosen.length >= 2  && aircraft_choosen.length >= 1){
        }else{
            if(error.classList.contains('active')){
                error.classList.remove('active')
                console.log("Congrats it works")
                event.preventDefault();
            }else{
                console.log("Congrats it works")
                event.preventDefault();
            }
        }
}
        
                
//Event listeners

zapis_btn.addEventListener("click", zapis);


