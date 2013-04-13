$('#order-form').submit (e) ->
  e.preventDefault()
  form_data = $(@).serialize()
  post_url = $(@).attr 'action'
  $.post post_url,form_data,(data) ->
    if data.message then $('.popup-wrap > div').text data.message

  return

$('#order-form').validate
  onKeyup : true
  sendForm: false
  eachValidField: () ->
    $(@).css
      'border': '1px solid #5B5B5B'

  eachInvalidField: () ->
    $(@).css
      'border': '1px solid red'

$('.popup-container .fancybox-item.fancybox-close').click (e) ->
  $('.popup-container').hide()
    