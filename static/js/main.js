function toggleSidebar() {
    const sidebar = document.getElementById('sidebarMenu');
    const overlay = document.getElementById('sidebarOverlay');
    const menuButton = document.getElementById('menuButton');
    
    if (sidebar && overlay && menuButton) {
        const isOpen = sidebar.classList.toggle('open');
        overlay.classList.toggle('open', isOpen);
        overlay.setAttribute('aria-hidden', String(!isOpen));
        sidebar.setAttribute('aria-hidden', String(!isOpen));
        sidebar.toggleAttribute('inert', !isOpen);
        menuButton.setAttribute('aria-expanded', String(isOpen));

        if (!isOpen) {
            menuButton.focus();
        }
    }
}

document.addEventListener('keydown', (event) => {
    const sidebar = document.getElementById('sidebarMenu');

    if (event.key === 'Escape' && sidebar && sidebar.classList.contains('open')) {
        toggleSidebar();
    }
});