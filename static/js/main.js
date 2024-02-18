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
