const menuToggle = document.querySelector(".menu-toggle");
const primaryNav = document.querySelector(".primary-nav");
const searchToggle = document.querySelector(".search-toggle");
const searchPanel = document.querySelector(".search-panel");
const searchInput = document.querySelector("#site-search");

menuToggle.addEventListener("click", () => {
    const isOpen = menuToggle.getAttribute("aria-expanded") !== "true";
    menuToggle.setAttribute("aria-expanded", String(isOpen));
    menuToggle.setAttribute("aria-label", isOpen ? "Закрыть меню" : "Открыть меню");
    primaryNav.classList.toggle("is-open", isOpen);
});

primaryNav.addEventListener("click", (event) => {
    if (event.target.closest("a")) {
        primaryNav.classList.remove("is-open");
        menuToggle.setAttribute("aria-expanded", "false");
        menuToggle.setAttribute("aria-label", "Открыть меню");
    }
});

function closeSearch() {
    searchPanel.hidden = true;
    searchToggle.setAttribute("aria-expanded", "false");
    searchInput.value = "";
    searchInput.dispatchEvent(new Event("input"));
}

searchToggle.addEventListener("click", () => {
    const isOpen = searchPanel.hidden;
    searchPanel.hidden = !isOpen;
    searchToggle.setAttribute("aria-expanded", String(isOpen));
    if (isOpen) {
        searchInput.focus();
    } else {
        closeSearch();
    }
});

document.querySelector(".search-close").addEventListener("click", closeSearch);
