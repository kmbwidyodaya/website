let currentSlideIndex = 0;
document.addEventListener('DOMContentLoaded', function () {
    initDots();
    startAutoSlide(); // Jalankan timer otomatis saat halaman dimuat
});

function initDots() {
    const slides = document.querySelectorAll('.news-slider .slide');
    const dotsContainer = document.getElementById('sliderDots');

    if (!dotsContainer || slides.length <= 1) return;

    dotsContainer.innerHTML = '';

    // Buat elemen dot sesuai jumlah slide yang ada
    slides.forEach((_, index) => {
        const dot = document.createElement('span');
        dot.classList.add('dot');
        if (index === 0) dot.classList.add('active');
        
        // Pindah slide saat dot diklik
        dot.addEventListener('click', () => showSlide(index));
        dotsContainer.appendChild(dot);
    });
}

function showSlide(index) {
    const slides = document.querySelectorAll('.news-slider .slide');
    const dots = document.querySelectorAll('.slider-dots .dot');
    if (slides.length === 0) return;

    if (index >= slides.length) currentSlideIndex = 0;
    else if (index < 0) currentSlideIndex = slides.length - 1;
    else currentSlideIndex = index;

    slides.forEach((slide, i) => {
        if (i === currentSlideIndex) {
            slide.classList.add('active');
        } else {
            slide.classList.remove('active');
        }
    });
    dots.forEach((dot, i) => {
        if (i === currentSlideIndex) {
            dot.classList.add('active');
        } else {
            dot.classList.remove('active');
        }
    });
}

function moveSlide(step) {
    showSlide(currentSlideIndex + step);
}
// Fungsi untuk menjalankan slide otomatis setiap 10 detik (10000 ms)
function startAutoSlide() {
    const slides = document.querySelectorAll('.news-slider .slide');
    if (slides.length <= 1) return; // Jangan jalankan timer jika gambar cuma 1

    autoSlideTimer = setInterval(() => {
        showSlide(currentSlideIndex + 1);
    }, 7000);
}

// Fungsi reset timer agar perpindahan otomatis tidak bentrok saat diklik manual
function resetAutoSlide() {
    if (autoSlideTimer) {
        clearInterval(autoSlideTimer);
        startAutoSlide();
    }
}