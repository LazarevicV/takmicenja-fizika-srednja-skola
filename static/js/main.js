// Za aktivni link na navbar
document.addEventListener("DOMContentLoaded", function () {
    console.log("DOM učitan.");

    // Koristite url_for kako biste dobili URL trenutne stranice
    var currentUrl = "{{ url_for('index') }}"; // Zamenite 'index' sa imenom vašeg view-a
    console.log("Trenutni URL:", currentUrl);

    var currentLink = document.getElementById(currentUrl + '-link');
    console.log("Pronađeni link:", currentLink);

    if (currentLink) {
        currentLink.classList.add('active');
        console.log("Active klasa dodata.");
    }
});
// Za aktivni link na navbar


// Back to top button
let mybutton = document.getElementById("btn-back-to-top");

window.onscroll = function () {
    scrollFunction();
};

function scrollFunction() {
    if (
        document.body.scrollTop > 130 ||
        document.documentElement.scrollTop > 130
    ) {
        mybutton.style.display = "block";
    } else {
        mybutton.style.display = "none";
    }
}
mybutton.addEventListener("click", backToTop);

function backToTop() {
    document.body.scrollTop = 0;
    document.documentElement.scrollTop = 0;
}
// Back to top button


// paginacija, button za sledeca i prethodna stranica
let currentPage = 1;
let displayedPage = 1; // Dodajte novu promenljivu za praćenje trenutno prikazane stranice
const rowsPerPage = 1;
const totalRows = 18;

function showPage(page) {
    // Sakrij sve redove koji nemaju klasu "vesti"
    const rows = document.querySelectorAll('.row.vesti');
    rows.forEach(row => {
        row.classList.remove('d-flex'); // Uklanja 'd-flex' klasu
    });

    // Prikazi samo odabrani red
    const selectedRow = document.getElementById(`row${page}`);
    if (selectedRow) {
        selectedRow.classList.add('d-flex'); // Dodaje 'd-flex' klasu
        // Dodajte skakanje na odabrani red (koristeći ID stranice kao sidro)
        window.location.hash = `#row${page}`;
    }

    // Ukloni klasu current-page sa svih dugmadi paginacije
    document.querySelectorAll('.btn-pagination').forEach(btn => {
        btn.classList.remove('current-page');
    });

    // Dodaj klasu current-page na trenutno označeno dugme
    const selectedButton = document.querySelector(`.btn-pagination:nth-child(${page})`);
    if (selectedButton) {
        selectedButton.classList.add('current-page');
    }

    // Pomeri na vrh stranice
    window.scrollTo({ top: 0, behavior: 'smooth' });

    // Ažuriraj trenutnu prikazanu stranicu
    displayedPage = page;

    // Onemogući dugme za prethodnu stranu ako smo na prvoj stranici
    document.getElementById('btnPrevious').disabled = displayedPage === 1;

    // Onemogući dugme za sledeću stranu ako smo na poslednjoj stranici
    document.getElementById('btnNext').disabled = displayedPage === totalRows;
}

function showNextPage(event) {
    event.preventDefault();
    const nextPage = displayedPage + 1;
    if (nextPage <= totalRows) {
        showPage(nextPage);
    }
}

function showPreviousPage(event) {
    event.preventDefault();
    const previousPage = displayedPage - 1;
    if (previousPage >= 1) {
        showPage(previousPage);
    }
}

function generatePaginationButtons() {
    console.log("Generisanje dugmadi za paginaciju...");
    const totalPages = Math.ceil(totalRows / rowsPerPage);
    console.log("Ukupan broj stranica:", totalPages);

    const paginationContainer = document.querySelector('.pagination-container');
    console.log("Pronađen kontejner za paginaciju:", paginationContainer);

    paginationContainer.innerHTML = ''; // Očisti postojeće dugmadi

    for (let i = 1; i <= totalPages; i++) {
        const button = document.createElement('button');
        button.className = 'btn btn-pagination';
        button.textContent = i;
        button.onclick = () => showPage(i);
        paginationContainer.appendChild(button);
    }

    console.log("Dugmadi za paginaciju generisana.");
}

console.log("Poziv funkcije generatePaginationButtons");
generatePaginationButtons();



// Pozovite funkciju za generisanje dugmadi prilikom učitavanja stranice
window.onload = function () {
    // Proverite da li se nalazite na stranici "vesti.html"
    if (window.location.pathname.includes("vesti.html")) {
        // Generiši dugmadi za paginaciju prvo
        generatePaginationButtons();
        // Ako da, prikaži prvu stranu
        showPage(currentPage);
    }
};



// // Prikazi prvu stranu kada se stranica učita
// window.onload = function () {
//     // Proverite da li se nalazite na stranici "vesti.html"
//     if (window.location.pathname.includes("vesti.html")) {
//         // Ako da, prikaži prvu stranu
//         showPage(currentPage);
//     }
// };