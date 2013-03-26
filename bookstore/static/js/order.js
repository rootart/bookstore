// Generated by CoffeeScript 1.6.1
(function() {

  $('#order-form').submit(function(e) {
    var form_data, post_url;
    e.preventDefault();
    form_data = $(this).serialize();
    post_url = $(this).attr('action');
    $.post(post_url, form_data, function(data) {
      if (data.message) {
        return $('.popup-wrap > div').text(data.message);
      }
    });
  });

  $('#order-form').validate({
    onKeyup: true,
    sendForm: false,
    eachValidField: function() {
      return $(this).css({
        'border': '1px solid #5B5B5B'
      });
    },
    eachInvalidField: function() {
      return $(this).css({
        'border': '1px solid red'
      });
    }
  });

}).call(this);
