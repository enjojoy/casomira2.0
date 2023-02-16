// const edit_btn = document.querySelectorAll('button');
// const flight_to_edit = document.querySelectorAll('li');

// console.log(edit_btn);
// console.log(flight_to_edit);

// edit_btn.forEach(btn => {

//     btn.addEventListener('click', ()=>{
//         var btn_value = btn.value;
//         flight_to_edit.forEach(flight=>{
//             if (flight.value == btn_value){
//                 //copied from github
//                 function insertAfter(referenceNode, newNode) {
//                     referenceNode.parentNode.insertBefore(newNode, referenceNode.nextSibling);
//                   }
//                 const new_el = document.createElement('div');
//                 // const new_cont = document.createTextNode('hello');
//                 new_el.innerHTML = '<p> {{let.id}} </p>';
//                 console.log(new_el);
//                 insertAfter(flight, new_el);
//             }
//         })
//     });

// })

// function openEdit(){
//     function insertAfter(referenceNode, newNode) {
//         referenceNode.parentNode.insertBefore(newNode, referenceNode.nextSibling);
//       }

//     console.log(flight.value, edit_btn.value);
// };

// edit_btn.addEventListener('click', openEdit);