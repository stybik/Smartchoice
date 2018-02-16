$( document ).ready(function(){
  $(".button-collapse").sideNav();
  $(".dropdown-button").dropdown();
  $('input.autocomplete').autocomplete({
    data: {
        "Iphone X": null,
        "Samsung Galaxy S8": null,
        "Redmi Note 5 pro": null,
        "Redmi Note 5":null
    }
    }); 
});