$(document).ready(function(){
    $(".sd").owlCarousel({
        // loop:true,
        margin:30,
        nav:true,
        dots:false,
        autoplay:true,
        autoplayTimeout:2000,
        autoplayHoverPause:true,
        navText:[$('.first_nav .prev'), $('.first_nav .next')],
        responsive:{
            0:{
                items:1,
            },
            600:{
                items:2,
                margin:0,
            },
            800:{
                items:3,
                margin:20
            }
        }
    }),
    $(".owl-carousel").owlCarousel({
        // loop:true,
        margin:30,
        nav:true,
        dots:false,
        autoplay:true,
        autoplayTimeout:2000,
        autoplayHoverPause:true,
        navText:[$('.owl-navigation .owl-nav-prev'), $('.owl-navigation .owl-nav-next')],
        responsive:{
            0:{
                items:1,
            },
            600:{
                items:2,
                margin:0,
            },
            800:{
                items:3,
                margin:20
            }
        }
    })
});

// Register Error Start
var close_container = document.querySelector(".close_container"),
    close_btn = document.querySelector(".close");

close_btn.addEventListener("click", a);
function a(){
    close_container.style.display = "none";   
}


setTimeout(function() {
    $(".close_container").fadeOut('slow');
}, 3000);
// Register Error End
