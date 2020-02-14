// Fetch and replace the name of the given url and display in the tag
$.get('https://swapi.co/api/people/5/?format=json', function (data) {
  $ ('div#character').text(data.name);
});
