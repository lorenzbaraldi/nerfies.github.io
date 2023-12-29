$(document).ready(function(){
    $('.slider-lollo').slick({
      slidesToShow: 1,
      slidesToScroll: 1,
      infinite: true,
      dots: true,
      adaptiveHeight: true,
      appendDots: $('.slider-container-lollo'),
      responsive: [
        {
          breakpoint: 768,
          settings: {
            slidesToShow: 2
          }
        },
        {
          breakpoint: 992,
          settings: {
            slidesToShow: 3
          }
        },
        {
          breakpoint: 1200,
          settings: {
            slidesToShow: 4
          }
        }
      ]
    });
  
    // Add your image groups dynamically
    var imageGroups = [
      ["./static/images/d3_images/0/0_img_gen0.png", "./static/images/d3_images/0/0_img_gen0.png", "./static/images/d3_images/0/0_img_gen0.png", "./static/images/d3_images/0/0_img_gen0.png"],
      ["./static/images/d3_images/0/0_img_gen0.png", "./static/images/d3_images/0/0_img_gen0.png", "./static/images/d3_images/0/0_img_gen0.png", "./static/images/d3_images/0/0_img_gen0.png"],
      // Add more groups as needed
    ];
  
    var slider = $('.slider-lollo');
  
    // Add images to the slider
    imageGroups.forEach(function(group){
      var slide = $('<div class="slide-lollo"></div>');
      group.forEach(function(image){
        slide.append('<img src="' + image + '" alt="Image">');
      });
      slider.append(slide);
    });
  });
  