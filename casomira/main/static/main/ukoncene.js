const edit_btn = document.getElementById('edit-flight');
const flight_to_edit = document.getElementById('flight');



function openEdit(){
    function insertAfter(referenceNode, newNode) {
        referenceNode.parentNode.insertBefore(newNode, referenceNode.nextSibling);
      }

    console.log(flight.value, edit_btn.value);

    
    
};



edit_btn.addEventListener('click', openEdit);