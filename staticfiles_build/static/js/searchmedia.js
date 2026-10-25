document.addEventListener('DOMContentLoaded', function () {
    const searchInput = document.getElementById('searchInput');
    const mediaCards = document.querySelectorAll('.media-card');
    const noResults = document.getElementById('noResults');

    if (!searchInput) return;

    searchInput.addEventListener('input', function () {
        const query = searchInput.value.toLowerCase().trim();

        let foundResults = false;

        mediaCards.forEach(card => {
            const titleEl = card.querySelector('.media-title');

            // Ambil teks murni menggunakan textContent agar aman dari XSS
            const titleText = titleEl ? titleEl.textContent.toLowerCase() : '';

            // Cek apakah query ada pada judul atau deskripsi
            if (titleText.includes(query)) {
                card.style.display = '';
            } else {
                card.style.display = 'none';
            }
        });
        if (noResults) {
            if (query === "" || foundResults) {
                noResults.style.display = 'none';
            } else {
                noResults.style.display = 'block';
            }
        }
    });
});