const searchInput = document.querySelector("#site-search");

function filterPosts(query) {
    const normalizedQuery = query.trim().toLocaleLowerCase("ru");
    document.querySelectorAll(".searchable-card").forEach((card) => {
        card.hidden = !card.textContent.toLocaleLowerCase("ru").includes(normalizedQuery);
    });
}

searchInput.addEventListener("input", () => filterPosts(searchInput.value));

document.querySelectorAll(".post-card-image img, .latest-image img, .profile img").forEach((image) => {
    image.addEventListener("error", () => {
        image.hidden = true;
    }, { once: true });
});
