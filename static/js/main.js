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
const totalRows = 18;

function showPage(page) {
    // Sakrij sve redove
    for (let i = 1; i <= totalRows; i++) {
        const row = document.getElementById(`row${i}`);
        if (row) {
            row.style.display = 'none';
        }
    }

    // Prikazi samo odabrani red
    const selectedRow = document.getElementById(`row${page}`);
    if (selectedRow) {
        selectedRow.style.display = 'flex';
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

    // Onemogući dugme za prethodnu stranu ako smo na prvoj stranici
    document.getElementById('btnPrevious').disabled = page === 1;

    // Onemogući dugme za sledeću stranu ako smo na poslednjoj stranici
    document.getElementById('btnNext').disabled = page === totalRows;
}

function showNextPage(event) {
    event.preventDefault();
    if (currentPage < totalRows) {
        currentPage++;
    }
    showPage(currentPage);
}

function showPreviousPage(event) {
    event.preventDefault();
    if (currentPage > 1) {
        currentPage--;
    }
    showPage(currentPage);
}


// Prikazi prvu stranu kada se stranica učita
document.addEventListener("DOMContentLoaded", function () {
    showPage(currentPage);
});


// // Prikazi prvu stranu kada se stranica učita
// document.addEventListener("DOMContentLoaded", function () {
//     // Proverite da li se nalazite na stranici "vesti.html"
//     if (window.location.pathname.includes("vesti.html")) {
//         // Ako da, prikaži prvu stranu
//         showPage(currentPage);
//     }
// });