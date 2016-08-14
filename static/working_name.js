//all the html will load before javascript is run
$(document).ready(function () {
//getting a map in the homepage
    var hackbright = {lat: 37.7886679, lng: -122.4114987}

    var map = new google.maps.Map(document.getElementById('map'), {
            center: hackbright,
            zoom: 8,
    });    


//call the function for the user html5 geolocation
    function showPosition(location) {
        console.log(location);
    }
// locating the user
// html hidden input - I have a bunch of stuff I want to pass along but I dont want the user to type it in 
    navigator.geolocation.getCurrentPosition(showPosition);

    //JQuery changes the DOM here to change the hidden input value to attri(value="lat")
                                                    // atrr(value="lng")
    // Once the user clicks submit
    $("#submit").on("submit", function getLatLng(evt))

    function getLatLng(evt) {
        $(".hidden").attr("value", "lat"); //want to set the empty value of lat
        $(".hidden").attr("value", "lng"); //want to set the emty value of lng
    }

// if the above doesn't work then maybe this will...?
// $("#lat").attr("value");
// $("#lng").attr("value");


// Random code writings that might be relvant sometime

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
// var map = new google.maps.Map(document.getElementById('map'), mapOptions);

// var markerOptions = {
//     position new google.maps.LatLng( , )
// };
// var marker = new google.maps.Marker(markerOptions);
// marker.setMap(map);  
        


        )};



















})