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

let person_choosen = [];
let aircraft_choosen = [];
console.log("aircraft choosen length" + aircraft_choosen.length);


person_choosen = $(".person").change(function(){
    var checked_people = document.querySelectorAll('input[name=person_choosen]').is(':checked');
    console.log(checked_people.length)
    console.log(checked_people);
    return checked_people
})    
    

aircraft_choosen = $('.aircraft').change(function(){
    var checked_aircrafts = document.querySelectorAll('input[name=aircraft_choosen]').is(':checked');
    console.log(checked_aircrafts.length);
    console.log(checked_aircrafts);
    return checked_aircrafts;
    });

console.log(aircraft_choosen);
console.log("aircraft choosen length" + aircraft_choosen.length);


zapis_btn = document.getElementById('zapis-btn');
error = document.getElementById('error');

function zapis(event){

        if (person_choosen.length === 0 || aircraft_choosen.length === 0 || person_choosen.length < 2  || aircraft_choosen.length < 1){
            if(error.classList.contains('active')){
                console.log("The requirement is not met!")
                event.preventDefault();
                } else{
                    error.classList.add('active')
                    console.log("The requirement is not met!")
                    event.preventDefault();
            }
        }
        
        if(person_choosen.length >= 2  || aircraft_choosen.length >= 1){
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


