$('#order-form').submit (e) ->
  e.preventDefault()
  form_data = $(@).serialize()
  post_url = $(@).attr 'action'
  $.post post_url,(data) ->
    alert 'ok'
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


    