document.addEventListener('DOMContentLoaded', function () {
    const searchInput = document.getElementById('searchInput');
    const newsCards = document.querySelectorAll('.news-card');
    const noResults = document.getElementById('noResults');

    if (!searchInput) return;

    searchInput.addEventListener('input', function () {
        const query = searchInput.value.toLowerCase().trim();
        let hasVisibleCard = false;

        newsCards.forEach(card => {
            const titleEl = card.querySelector('.news-title');
            const titleText = titleEl ? titleEl.textContent.toLowerCase() : '';

            // Jika query kosong atau judul cocok, tampilkan kartu
            if (query === '' || titleText.includes(query)) {
                card.style.display = ''; // Tampilkan kartu
                hasVisibleCard = true;
            } else {
                card.style.display = 'none'; // Sembunyikan kartu
            }
        });

        // Kelola tampilan pesan noResults
        if (noResults) {
            if (query === '' || hasVisibleCard) {
                noResults.style.display = 'none';
            } else {
                noResults.style.display = 'block';
            }
        }
    });
});