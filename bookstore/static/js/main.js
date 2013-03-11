$(function(){
	
  //search menu
  $('.search-menu').click(function(){
    //alert('ok');
    $(".menu-space").width('158');
    $('.search-menu .search').css('display','inline-block');
  });
  

  
  /*show popup*/
  $('#show-popup').click(function(e) {
    var order_link = $(this).attr('data-url');
    console.log(order_link);
    $('#popup-order .popup-wrap').load(order_link);
	  $('#popup-order').show();
	  
	  e.preventDefault()
  });	
  
  $('body').keypress(function(e) { 
      if (e.keyCode == 27) {
		   $('#popup-order').hide();
      }     
  });
  
  
  $('a.book-gallery').fancybox({
    'autoHeight': true,
    'autoWidth': true 
  });
  
});
