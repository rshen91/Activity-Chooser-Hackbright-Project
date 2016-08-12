//all the html will load before javascript is run
$(document).ready(function () {

// locating the user
//     //call the function for the user html5 geolocation
//     navigator.geolocation.getCurrentPosition(showPosition);
//getting a map in the homepage
    var hackbright = {lat: 37.7886679, lng: -122.4114987}

    var map = new google.maps.Map(document.getElementById('map'), {
            center: hackbright,
            zoom: 8,
    });

//     window.onload = function() {
//         var startPos;
//         var geoSuccess = function(position) {
//             startPos = position;
//             document.getElementById('startLat').innerHTML = startPos.coords.latitude;
//             document.getElementById('startLon').innerHTML = startPos.coords.longitude;
//         }
//         var geoError = function(error) {
//             console.log('Error occured. Error code: ' + error.code);
//         }       
//         };
//         navigator.geolocation.getCurrentPosition(geoSuccess, geoError);
//     };

// //get a map 
//     function initMap(position) {
//         // position.coords from HTML5 Geolocation w3schools.com
//         var map_of_user = {position.coords.latitude + "," + position.coords.longitude};

//         var map = new google.maps.Map(document.getElementById('map')), {
//         center: map_of_user,
//         zoom: 8,
//     };
  
//      function ask_user_direct() {
//         var answer = prompt("Do you want to have activities built into your trip or would you prefer a direct route?")
//         if (answer == "yes") {
//             // show the map with the direct route
//             document.getElementById("mapidinthehtml");
//         } else {
//             document.getElementById("")
//         }

    
    )};



















})