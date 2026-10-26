let currentBannerIndex = 0;
let autoBannerTimer = null;

document.addEventListener('DOMContentLoaded', function () {
    initBannerDots();
    startAutoBanner();
});

function initBannerDots() {
    const slides = document.querySelectorAll('.banner-slider .banner-slide');
    const dotsContainer = document.getElementById('bannerDots');

    if (!dotsContainer || slides.length <= 1) return;

    dotsContainer.innerHTML = '';

    slides.forEach((_, index) => {
        const dot = document.createElement('span');
        dot.classList.add('dot');
        if (index === 0) dot.classList.add('active');
        
        dot.addEventListener('click', () => {
            showBannerSlide(index);
            resetAutoBanner();
        });
        dotsContainer.appendChild(dot);
    });
}

function showBannerSlide(index) {
    const slides = document.querySelectorAll('.banner-slider .banner-slide');
    const dots = document.querySelectorAll('.banner-dots .dot');
    
    if (slides.length === 0) return;

    if (index >= slides.length) currentBannerIndex = 0;
    else if (index < 0) currentBannerIndex = slides.length - 1;
    else currentBannerIndex = index;

    slides.forEach((slide, i) => {
        slide.classList.toggle('active', i === currentBannerIndex);
    });

    dots.forEach((dot, i) => {
        dot.classList.toggle('active', i === currentBannerIndex);
    });
}

function moveBannerSlide(step) {
    showBannerSlide(currentBannerIndex + step);
    resetAutoBanner();
}

function startAutoBanner() {
    const slides = document.querySelectorAll('.banner-slider .banner-slide');
    if (slides.length <= 1) return;

    autoBannerTimer = setInterval(() => {
        showBannerSlide(currentBannerIndex + 1);
    }, 6000); // Berganti otomatis setiap 6 detik
}

function resetAutoBanner() {
    if (autoBannerTimer) {
        clearInterval(autoBannerTimer);
        startAutoBanner();
    }
}