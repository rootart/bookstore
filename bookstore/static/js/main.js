$(function(){
  /*show popup*/
  $('#show-popup').click(function(e) {
	  $('#popup-order').show();
	  
	  e.preventDefault()
  });	
  
  $('body').keypress(function(e) { 
      if (e.keyCode == 27) {
		   $('#popup-order').hide();
      }     
  });
  
});
