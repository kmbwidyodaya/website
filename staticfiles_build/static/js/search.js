document.addEventListener('DOMContentLoaded', function () {
    const searchInput = document.getElementById('searchInput');
    const mediaCards = document.querySelectorAll('.media-card-item');

    if (!searchInput) return;

    searchInput.addEventListener('input', function () {
        const query = searchInput.value.toLowerCase().trim();

        mediaCards.forEach(card => {
            const titleEl = card.querySelector('.media-card-title');
            const descEl = card.querySelector('.media-card-desc');

            // Ambil teks murni menggunakan textContent agar aman dari XSS
            const titleText = titleEl ? titleEl.textContent.toLowerCase() : '';
            const descText = descEl ? descEl.textContent.toLowerCase() : '';

            // Cek apakah query ada pada judul atau deskripsi
            if (titleText.includes(query) || descText.includes(query)) {
                card.style.display = '';
            } else {
                card.style.display = 'none';
            }
        });
    });
});