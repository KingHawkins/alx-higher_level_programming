// Adds a <li> element to a list when user clicks on tag 'div#add_item'
$('#add_item').click(function () {
  $('ul').append('<li>Item</li>');
});
