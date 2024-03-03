// Za aktivni link na navbar
document.addEventListener("DOMContentLoaded", function () {

  // Koristite url_for kako biste dobili URL trenutne stranice
  var currentUrl = "{{ url_for('index') }}"; // Zamenite 'index' sa imenom vašeg view-a

  var currentLink = document.getElementById(currentUrl + "-link");

  if (currentLink) {
    currentLink.classList.add("active");
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
const rowsPerPage = 1;
let totalRows = document.querySelectorAll(".row.vesti").length;

function showPage(page) {
  const rows = document.querySelectorAll(".row.vesti");
  const start = (page - 1) * rowsPerPage;
  const end = start + rowsPerPage;

  rows.forEach((row, index) => {
    // Prikazi samo redove za trenutnu stranicu
    if (index >= start && index < end) {
      row.classList.add("d-flex");
    } else {
      row.classList.remove("d-flex");
    }
  });

  updatePaginationButtons(page);
}

function updatePaginationButtons(page) {
  document.querySelectorAll(".btn-pagination").forEach((btn) => {
    btn.classList.remove("current-page");
  });

  const selectedButton = document.querySelector(
    `.btn-pagination:nth-child(${page})`
  );
  if (selectedButton) {
    selectedButton.classList.add("current-page");
  }

  window.scrollTo({ top: 0, behavior: "smooth" });

  currentPage = page;

  document.getElementById("btnPrevious").disabled = currentPage === 1;
  document.getElementById("btnNext").disabled =
    currentPage === Math.ceil(totalRows / rowsPerPage);
}

function showNextPage(event) {
  event.preventDefault();
  const nextPage = currentPage + 1;
  if (nextPage <= Math.ceil(totalRows / rowsPerPage)) {
    showPage(nextPage);
  }
}

function showPreviousPage(event) {
  event.preventDefault();
  const previousPage = currentPage - 1;
  if (previousPage >= 1) {
    showPage(previousPage);
  }
}

function generatePaginationButtons() {
  totalRows = document.querySelectorAll(".row.vesti").length;
  const totalPages = Math.ceil(totalRows / rowsPerPage);

  const paginationContainer = document.querySelector(".pagination-container");
  paginationContainer.innerHTML = "";

  for (let i = 1; i <= totalPages; i++) {
    const button = document.createElement("button");
    button.className = "btn btn-pagination";
    button.textContent = i;
    button.onclick = () => showPage(i);
    paginationContainer.appendChild(button);
  }

}

generatePaginationButtons();
showPage(currentPage);

window.onload = function () {
  if (window.location.pathname.includes("vesti.html")) {
    generatePaginationButtons();
  }
};