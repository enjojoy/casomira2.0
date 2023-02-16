pridat_btn = document.getElementById('pridat-btn');
pridat_novy_let = document.getElementById('pridat-novy-let');
vlecna = document.getElementById('vlecna');
vlecna_container = document.getElementById('vlecna-let');
vlecna_smazat = document.getElementById('vlecna-smazat');


function pridatLet(){
    pridat_btn.classList.add('hidden');
    pridat_novy_let.classList.remove('hidden');
}

function pridatVlecnou(){
    vlecna_container.classList.remove('vlecna-hidden');
}

function smazatVlecnou(){
    vlecna_container.classList.add('vlecna-hidden');
}

pridat_btn.addEventListener('click', pridatLet);
vlecna.addEventListener('click', pridatVlecnou);
vlecna_smazat.addEventListener('click', smazatVlecnou)

