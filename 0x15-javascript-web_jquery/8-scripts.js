/*Write a JavaScript script that fetches and lists the title for all movies by using this URL: https://swapi-api.alx-tools.com/api/films/?format=json

    All movie titles must be list in the HTML tag UL#list_movies
    You can’t use document.querySelector to select the HTML tag
    You must use the JQuery API

Please test with this HTML file in your browser:
*/

$(document).ready(function () {
  const list = $('UL#list_movies');
  const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';

  $.get(url, function (data) {
    data.results.forEach(({ title }) => {
      list.append(`<li>${title}</li>`);
    });
  });
});
