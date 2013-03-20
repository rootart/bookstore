jQuery ->
  $('.search-menu').click (e) ->
    $('.menu-space').width '271'
    $('.search-menu .search').css('display':'inline-block')
    return

  # show popup block
  $('#show-popup').click (e) ->
    e.preventDefault()
    order_link = $(@).attr 'data-url'
    $('#popup-order .popup-wrap').load order_link
    $('#popup-order').show()
    return False

  # close popup on escape
  $('body').keypress (e) ->
    if e.keyCode is 27 then $('$popup-order').hide()

  $('a.book-gallery').fancybox
    'autoHeight': true
    'autoWidth': true