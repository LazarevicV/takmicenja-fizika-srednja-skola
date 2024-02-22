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



let currentPage = 1;
    const totalRows = 18; // Ukupan broj redova

    function showPage(page) {
        // Sakrij sve redove
        for (let i = 1; i <= totalRows; i++) {
            $(`#row${i}`).hide();
        }

        // Prikazi samo odabrani red
        $(`#row${page}`).show();
    }

    function showNextPage() {
        if (currentPage < totalRows) {
            currentPage++;
        } else {
            currentPage = 1;
        }
        showPage(currentPage);
    }

    function showPreviousPage() {
        if (currentPage > 1) {
            currentPage--;
        } else {
            currentPage = totalRows;
        }
        showPage(currentPage);
    }

    // Prikazi prvu stranu kada se stranica učita
    $(document).ready(function () {
        showPage(currentPage);
    });


// Paginacija

// document.addEventListener("DOMContentLoaded", function () {
//     const newsPages = document.querySelectorAll('.news-page');
//     let currentPage = 1;

//     function showPage(pageNumber) {
//         newsPages.forEach(page => {
//             page.style.display = "none";
//         });

//         const selectedPage = document.querySelector(`.news-page[data-page="${pageNumber}"]`);
//         if (selectedPage) {
//             selectedPage.style.display = "flex"; // Podešavanje stila na flex ako koristite Bootstrap grid system
//         }
//     }

//     function updatePagination() {
//         const paginationLinks = document.querySelectorAll('.pagination .page-link');
//         paginationLinks.forEach(link => {
//             link.addEventListener('click', function (event) {
//                 event.preventDefault();
//                 const targetPage = this.innerText;
//                 if (targetPage === '«') {
//                     currentPage = Math.max(1, currentPage - 1);
//                 } else if (targetPage === '»') {
//                     currentPage = Math.min(newsPages.length, currentPage + 1);
//                 } else {
//                     currentPage = parseInt(targetPage);
//                 }

//                 showPage(currentPage);
//             });
//         });
//     }

//     showPage(currentPage);
//     updatePagination();
// });