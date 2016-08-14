"use strict";
//all the html will load before javascript is run

$(document).ready(function () {

//getting a map in the homepage from lecture notes
    var hackbright = {lat: 37.7886679, lng: -122.4114987}

    var map = new google.maps.Map(document.getElementById('homepage-map'), {
          center: hackbright, //want to replace this with user_location
          zoom: 8,
            // zoomControl: false,
    });    


//call the function for the user html5 geolocation
    function showPosition(location) {
        console.log(location);
    }
// locating the user
// html hidden input - I have a bunch of stuff I want to pass along but I dont want the user to type it in 
    user_location = navigator.geolocation.getCurrentPosition(showPosition);

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

// There is a JS Places Library var map;
// var service;
// var infowindow;

// function initialize() {
//   var pyrmont = new google.maps.LatLng(-33.8665433,151.1956316);

//   map = new google.maps.Map(document.getElementById('map'), {
//       center: pyrmont,
//       zoom: 15
//     });

//   var request = {
//     location: pyrmont,
//     radius: '500',
//     types: ['store']
//   };

//   service = new google.maps.places.PlacesService(map);
//   service.nearbySearch(request, callback);
// }

// function callback(results, status) {
//   if (status == google.maps.places.PlacesServiceStatus.OK) {
//     for (var i = 0; i < results.length; i++) {
//       var place = results[i];
//       createMarker(results[i]);
//     }
//   }
// }

// Random code writings that might be relvant sometime
// from https://developers.google.com/maps/documentation/javascript/examples/directions-complex
    function initMap() {
        var markerArray = [];

        // Instantiate a directions service.
        var directionsService = new google.maps.DirectionsService;

        // Create a map and center it on HB.
        var map = new google.maps.Map(document.getElementById('map'), {
          zoom: 13,
          center: hackbright
        });

        // Create a renderer for directions and bind it to the map.
        var directionsDisplay = new google.maps.DirectionsRenderer({map: map});

        // Instantiate an info window to hold step text.
        var stepDisplay = new google.maps.InfoWindow;

        // Display the route between the initial start and end selections.
        calculateAndDisplayRoute(
            directionsDisplay, directionsService, markerArray, stepDisplay, map);
        // Listen to change events from the start and end lists.
        var onChangeHandler = function() {
          calculateAndDisplayRoute(
              directionsDisplay, directionsService, markerArray, stepDisplay, map);
        };
        document.getElementById('start').addEventListener('change', onChangeHandler);
        document.getElementById('end').addEventListener('change', onChangeHandler);
      }

    function calculateAndDisplayRoute(directionsDisplay, directionsService,
          markerArray, stepDisplay, map) {
        // First, remove any existing markers from the map.
        for (var i = 0; i < markerArray.length; i++) {
          markerArray[i].setMap(null);
        }

        // Retrieve the start and end locations and create a DirectionsRequest using
        // WALKING directions.
        directionsService.route({
          origin: document.getElementById('start').value,
          destination: document.getElementById('end').value,
          travelMode: 'WALKING'
        }, function(response, status) {
          // Route the directions and pass the response to a function to create
          // markers for each step.
          if (status === 'OK') {
            document.getElementById('warnings-panel').innerHTML =
                '<b>' + response.routes[0].warnings + '</b>';
            directionsDisplay.setDirections(response);
            showSteps(response, markerArray, stepDisplay, map);
          } else {
            window.alert('Directions request failed due to ' + status);
          }
        });
      }

    function showSteps(directionResult, markerArray, stepDisplay, map) {
        // For each step, place a marker, and add the text to the marker's infowindow.
        // Also attach the marker to an array so we can keep track of it and remove it
        // when calculating new routes.
        var myRoute = directionResult.routes[0].legs[0];
        for (var i = 0; i < myRoute.steps.length; i++) {
          var marker = markerArray[i] = markerArray[i] || new google.maps.Marker;
          marker.setMap(map);
          marker.setPosition(myRoute.steps[i].start_location);
          attachInstructionText(
              stepDisplay, marker, myRoute.steps[i].instructions, map);
        }
      }

    function attachInstructionText(stepDisplay, marker, text, map) {
        google.maps.event.addListener(marker, 'click', function() {
          // Open an info window when the marker is clicked on, containing the text
          // of the step.
          stepDisplay.setContent(text);
          stepDisplay.open(map, marker);
        });
      }

//      window.onload = function() {
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

// var map = new google.maps.Map(document.getElementById('map'), mapOptions);

//FROM LECTURE NOTES ADDING MARKERS 
    function addMarker() {
      var image = "image url"
      var nearUserLocation = new google.maps.LatLng(user_location)
    }
        


        )};



















})