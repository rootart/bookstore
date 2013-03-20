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
    $('#order-form').validate()
    return

  # close popup on escape
  $('body').keypress (e) ->
    if e.keyCode is 27 then $('#popup-order').hide()

  # fancybox gallery
  $('a.book-gallery').fancybox
    'autoHeight': true
    'autoWidth': true


  # Homepage news slider
  $('.bullets a').click (e) ->
    e.preventDefault()
    clicked_bullet = $ e.target
    bullet_id = clicked_bullet.data 'article'
    $('.main-article li').hide()
    sel = ".main-article li[data-article=#{bullet_id}]"
    $(sel).show()
    $('.bullets a').removeClass 'active'
    clicked_bullet.addClass 'active'

    return

  return
