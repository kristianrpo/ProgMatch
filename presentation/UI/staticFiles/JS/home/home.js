var swiper = new Swiper('.mySwiper', {
    slidesPerView: 5,
    spaceBetween: 30,
    pagination: {
    el: '.swiper-pagination',
    clickable: true,
    },
    breakpoints: {
    320: {
        slidesPerView: 1,
        spaceBetween: 20,
    },
    640: {
        slidesPerView: 3,
        spaceBetween: 25,
    },
    1024: {
        slidesPerView: 5,
        spaceBetween: 30,
    },
    }
});