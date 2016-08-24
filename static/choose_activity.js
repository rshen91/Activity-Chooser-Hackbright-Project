"use strict";


$(document).ready(function () {
console.log("HEY YOU, I AM HERE in the document.ready");

  function getLocation() {
      if (navigator.geolocation) {  // when the browser has geolocation capability
          navigator.geolocation.getCurrentPosition(handlePositionFound); // when you get the lat/long from the browser, give it as an argument to showPosition.
      } else {
          alert("Geolocation is not supported by the browser.");
      } 
    } 

  function handlePositionFound(position) { //get the coords
    console.log('position:', position); //expand the arrow
    //this prints it in the console
      console.log("Latitude: "+ position.coords.latitude + "<br> Longitude: " + position.coords.longitude);
      $("#lat").val(position.coords.latitude); //user_lat
      
      $("#lng").val(position.coords.longitude); //user_lng
      
      initMap(position.coords.latitude, position.coords.longitude);
      // console.log(user_lat);
      // console.log(user_lng);
  }

});   //end documentReady