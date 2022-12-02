$( document ).ready(function() {
    // $('#personOpt').multiselect({
    //     columns: 1,
    //     nonSelectedText : 'Select a person',
    //     numberDisplayed: 1,
        
    // });
    // $('#aircraftOpt').multiselect({
    //     columns: 1,
    //     nonSelectedText : 'Select an airplane',
    //     numberDisplayed: 1,

    // });

    let person_choosen;
    let aircraft_choosen;

    //Returns choosen values

    person_choosen =  $('person').change(function(){
        
                person_choosen = $(this).val();  // this will give values of selected option by array
                return person_choosen;
                
                });


    aircraft_choosen = $('aircraft_choosen').change(function(){
        
                aircraft_choosen = $(this).val();  // this will give values of selected option by array
                console.log(aircraft_choosen);
                return aircraft_choosen;
                });
        
    
                zapis_btn = document.getElementById('zapis-btn');
                error = document.getElementById('error');
                
                function zapis(){
                
                        if (person_choosen === null || aircraft_choosen === null || person_choosen.length < 2  || aircraft_choosen.length < 1){
                            if(error.classList.contains('active')){
                                } else{
                                    error.classList.add('active')
                            }
                        }else{
                            if(error.classList.contains('active')){
                               error.classList.remove('active')
                           }else{
                           }
                        }
                }
                
                 
                //Event listeners
                
                zapis_btn.addEventListener("click", zapis);
});

