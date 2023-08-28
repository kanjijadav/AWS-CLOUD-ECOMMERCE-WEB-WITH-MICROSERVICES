document.addEventListener("DOMContentLoaded", function () {
    const menuIcon = document.getElementById("menu-icon");
    const dropdown = document.getElementById("dropdown");

    menuIcon.addEventListener("click", function () {
        dropdown.classList.toggle("active");
    });
});
