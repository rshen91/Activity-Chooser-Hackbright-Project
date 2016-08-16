"use strict";


$(document).ready(function () {
console.log("HEY YOU, I AM HERE in the document.ready");
});   //end documentReady


function initMap(user_lat, user_lng) {

    // for hardcoding these are hb's lat lng
    var hackbright = {lat: 37.7886679, lng: -122.4114987};

    //rendering a new map on the homepage in the div homepage-map
    var map = new google.maps.Map(document.getElementById('homepage-map'), {
      //this function gets the values out of the DOM, see handlePositionFound
          center: {"lat":user_lat, "lng":user_lng},
          zoom: 10
          // zoomControl: false,
    });    

        var userMarker = addMarker(map, user_lat, user_lng);
        
      } //this is where initMap ends
// this is needed to load the map - triggers the cascade of functions 
google.maps.event.addDomListener(window, "load", getLocation);


function getLocation() {
    if (navigator.geolocation) {  // when the browser has geolocation capability
        navigator.geolocation.getCurrentPosition(handlePositionFound); // when you get the lat/long from the browser, give it as an argument to showPosition.
    } else {
        alert("Geolocation is not supported by the browser.");
    } 
  } 


function handlePositionFound(position) { //get the coords
  //this prints it in the console
    console.log("Latitude: "+ position.coords.latitude + "<br> Longitude: " + position.coords.longitude);
    $("#lat").val(position.coords.latitude); //user_lat
    
    $("#lng").val(position.coords.longitude); //user_lng
    
    initMap(position.coords.latitude, position.coords.longitude);
    // console.log(user_lat);
    // console.log(user_lng);
}

function addMarker(map, userLat, userLng) {
  var marker = new google.maps.Marker({
    position: {lat: parseInt(userLat), lng: parseInt(userLng)},
    title: 'User location!',
    map: map
    })
  return marker;

}





















