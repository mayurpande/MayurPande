$( document ).ready(function() {

    $(".icon").on('click',function(e){

      e.preventDefault();
      $('.icon').toggleClass('active');
      $("header nav ul").toggleClass('open');
    });

    //Just a scroller for navigation
$(".navbtn").click(function(e){
    e.preventDefault();
    var adress = $(this).attr("href");
    $("html, body").animate({scrollTop: $(adress).offset().top - 20},'slow');
});



});
