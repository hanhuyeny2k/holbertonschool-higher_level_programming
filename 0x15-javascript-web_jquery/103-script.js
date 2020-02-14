// fetch and print how to say "hello"
$.ajax({
  url: 'https://www.fourtonfish.com/hellosalut/hello/',
  type: 'GET',
  dataType: 'json'
})
