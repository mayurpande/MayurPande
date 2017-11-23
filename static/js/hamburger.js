$( document ).ready(function() {

    $(".icon").on('click',function(e){

      e.preventDefault();
      $('.icon').toggleClass('active');
      $("header nav ul").toggleClass('open');
    });




});
