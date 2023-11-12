
window.addEventListener('scroll', function() {
    const navbar = document.querySelector('nav');
    if (window.scrollY > 0) {
    navbar.classList.add('bg-opacity-50', 'backdrop-filter', 'backdrop-blur-lg');
    } else {
    navbar.classList.remove('bg-opacity-50', 'backdrop-filter', 'backdrop-blur-lg');
    }
});
