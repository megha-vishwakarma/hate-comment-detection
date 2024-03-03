/******************Add the story ******************/
const image_profile = [
    ['https://c0.wallpaperflare.com/preview/544/355/643/funko-pop-babygroot-collection.jpg','Groot'],
    ['https://c4.wallpaperflare.com/wallpaper/65/932/27/anime-demon-slayer-kimetsu-no-yaiba-boy-earrings-kimetsu-no-yaiba-hd-wallpaper-thumb.jpg','Little Mix'],
    ['https://c4.wallpaperflare.com/wallpaper/516/859/734/anime-girls-car-traffic-rain-wallpaper-thumb.jpg','1D'],
    ['https://c4.wallpaperflare.com/wallpaper/948/147/675/dog-animals-siberian-husky-water-wallpaper-preview.jpg','Pipo'],
    ['https://c4.wallpaperflare.com/wallpaper/370/127/644/uchiha-sasuke-rinnegan-eternal-mangekyou-sharingan-naruto-shippuuden-wallpaper-preview.jpg','amine'],
    ['https://c4.wallpaperflare.com/wallpaper/864/806/346/minimalism-digital-art-simple-cat-wallpaper-thumb.jpg','user1'],
    ['https://c4.wallpaperflare.com/wallpaper/785/944/976/smiling-simple-black-background-digital-art-wallpaper-thumb.jpg','user2'],
    ['https://i.ibb.co/7R0Vzp3/account8.jpg','user3'],
    ['https://i.ibb.co/gvrfhjL/account9.jpg','user4'],
    ['https://i.ibb.co/j8L7FPY/account10.jpg','user5'],
    ['https://i.ibb.co/JcXRPht/account11.jpg','user6'],
    ['https://i.ibb.co/6WvdZS9/account12.jpg','user7'],
    ['https://i.ibb.co/pJ8thst/account13.jpg','user8'],
    ['https://i.ibb.co/4M3W996/account14.jpg','user9'],
    ['https://i.ibb.co/Fzpg5yd/account15.jpg','user10'],
]
const story_container = document.querySelector('.owl-carousel.items');
if(story_container){
    for (var i = 0; i < image_profile.length; i++) {
        const parentDiv = document.createElement('div');
        parentDiv.classList.add("item_s");
        parentDiv.innerHTML = `
            <img src="${image_profile[i][0]}">
            <p>${image_profile[i][1]}</p>
            `;
        story_container.appendChild(parentDiv);
    }
}


$(document).ready(function(){
    $(".owl-carousel").owlCarousel();
});

$('.owl-carousel').owlCarousel({
    loop:true,
    margin:5,
    responsiveClass:true,
    responsive:{
        0:{
            items:5,
            nav:true
        },
        500:{
            items:7,
            nav:false
        }
    }
})