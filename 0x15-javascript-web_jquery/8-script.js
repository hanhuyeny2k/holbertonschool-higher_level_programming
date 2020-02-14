// print out the title from the url
$.ajax({
  url: 'https://swapi.co/api/people/5/?format=json',
  type: 'GET',
  dataType: 'json'
})
  .done(function (json) {
    let titles = json.results;
    for (let x = 0; x < titles.length; x++) {
      $('UL#list_movies').append('<li>' + titles[x].title + '</li>');
    }
  });
