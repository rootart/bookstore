// Generated by CoffeeScript 1.6.2
(function() {
  jQuery(function() {
    $('.search-menu').click(function(e) {
      $('.menu-space').width('271');
      $('.search-menu .search').css({
        'display': 'inline-block'
      });
    });
    $('#show-popup').click(function(e) {
      var order_link;

      e.preventDefault();
      order_link = $(this).attr('data-url');
      $('#popup-order .popup-wrap').load(order_link);
      $('#popup-order').show();
      return False;
    });
    $('body').keypress(function(e) {
      if (e.keyCode === 27) {
        return $('$popup-order').hide();
      }
    });
    return $('a.book-gallery').fancybox({
      'autoHeight': true,
      'autoWidth': true
    });
  });

}).call(this);
