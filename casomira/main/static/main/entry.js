var inputs = document.getElementsByTagName('input');

zapis_btn = document.getElementById('zapis-btn');
error = document.getElementById('error');

function zapis(event){
        p=$("input[name=person_choosen]:checked").get();
        a=$('input[name=aircraft_choosen]:checked').get();
        console.log($("input[name=person_choosen]:checked").get());
        console.log($('input[name=aircraft_choosen]:checked').get());

        if ( p.length < 2  || a.length < 1){
            if(error.classList.contains('active')){
                console.log("The requirement is not met!");
                event.preventDefault();
                } else{
                    error.classList.add('active');
                    console.log("The requirement is not met!");
                    event.preventDefault();
            }
        // }if(person_choosen.length >= 2  && aircraft_choosen.length >= 1){
        }else{
            if(error.classList.contains('active')){
                error.classList.remove('active')
                console.log("Congrats it works")

            }else{
                console.log("Congrats it works")

            }
        }
}
        
                
//Event listeners

zapis_btn.addEventListener("click", zapis);


// const app = createApp({
//     delimiters: ['[[', ']]'],
//     data(){
//         return{
//             count: 12345,
//         }
//     },
//     created(){
//         console.log('Hello')
//     }

// });


// const mountedApp = app.mount("#app");