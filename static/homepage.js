"use strict";

$(document).ready(function () {
console.log("HEY YOU, I AM HERE in the document.ready");


function initMap(user_lat, user_lng) {
    console.log('user_lat:', user_lat, 'user_lng:', user_lng);

    //rendering a new map on the homepage in the div homepage-map
    var map = new google.maps.Map(document.getElementById('homepage-map'), {
      //this function gets the values out of the DOM, see handlePositionFound
          center: {"lat":user_lat, "lng":user_lng},
          zoom: 18
    });    

        var userMarker = addMarker(map, user_lat, user_lng);
        var trafficLayer = new google.maps.TrafficLayer();
        trafficLayer.setMap(map);    
    }
    
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
    console.log("Latitude: "+ position.coords.latitude + "<br> Longitude: " + position.coords.longitude);
    $("#lat").val(position.coords.latitude); 
    $("#lng").val(position.coords.longitude);
    
    initMap(position.coords.latitude, position.coords.longitude);
}

function addMarker(map, user_lat, user_lng) {
  var marker = new google.maps.Marker({
    position: {lat: user_lat, lng: user_lng}, //parseInt() rounds so the marker isn't on their current location
    title: 'User location!',
    map: map
    })
    console.log('marker position '+user_lat, user_lng);
  return marker;

}


});   //end documentReady

















