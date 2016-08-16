"use strict";
//If this doesn't print in the console then the server.py isn't able to read the js
console.log("YO I AM HERE");

$(document).ready(function () {


//from lecture jquery notes page 5
  function handleLatLngSave(data) {
    alert("handled lat lng!");
  }

  function submitOrder(evt) {
    evt.preventDefault();

    var formInputs = {
      "lat": $("#lat").val(),
      "lng": $("#lng").val()
    };

    $.post("/submission",
            formInputs,
            handleLatLngSave);
  }
  $("#order-form").on("submit", submitOrder);

});   //end documentReady
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

    // var user_lat = $("#lat").val();
    // var user_lng = $("#lng").val();
// Random code writings that might be relvant sometime
// from https://developers.google.com/maps/documentation/javascript/examples/directions-complex
    //     function calculateAndDisplayRoute (directionsDisplay, directionsService, markerArray, stepDisplay, map) {
    //     // First, remove any existing markers from the map.
    //     for (var i = 0; i < markerArray.length; i++) {
    //       markerArray[i].setMap(null);
    //     }

    //     // Retrieve the start and end locations and create a DirectionsRequest using
    //     // WALKING directions.
    //     directionsService.route({
    //       origin: document.getElementById('start').value,
    //       destination: document.getElementById('end').value,
    //       travelMode: 'WALKING'
    //     }, function(response, status) {
    //       // Route the directions and pass the response to a function to create
    //       // markers for each step.
    //             if (status === 'OK') {
    //                 document.getElementById('warnings-panel').innerHTML =
    //             '<b>' + response.routes[0].warnings + '</b>';
    //                 directionsDisplay.setDirections(response);
    //                 showSteps(response, markerArray, stepDisplay, map);
    //             } else {
    //               window.alert('Directions request failed due to ' + status);
    //             }
    //     });
    //   }

    // function showSteps(directionResult, markerArray, stepDisplay, map) {
    //     // For each step, place a marker, and add the text to the marker's infowindow.
    //     // Also attach the marker to an array so we can keep track of it and remove it
    //     // when calculating new routes.
    //     var myRoute = directionResult.routes[0].legs[0];
    //     for (var i = 0; i < myRoute.steps.length; i++) {
    //       var marker = markerArray[i] = markerArray[i] || new google.maps.Marker;
    //       marker.setMap(map);
    //       marker.setPosition(myRoute.steps[i].start_location);
    //       attachInstructionText(
    //           stepDisplay, marker, myRoute.steps[i].instructions, map);
    //     }
    //   }

    // function attachInstructionText(stepDisplay, marker, text, map) {
    //     google.maps.event.addListener(marker, 'click', function() {
    //       // Open an info window when the marker is clicked on, containing the text
    //       // of the step.
    //       stepDisplay.setContent(text);
    //       stepDisplay.open(map, marker);
    //     });
    //   }

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



//user_lat and user_lng are just parameters 
function initMap(user_lat, user_lng) {

    var hackbright = {lat: 37.7886679, lng: -122.4114987};

    var map = new google.maps.Map(document.getElementById('homepage-map'), {
          center: {lat:parseInt(user_lat), lng: parseInt(user_lng) },
          zoom: 10,
          // zoomControl: false,
    });    
        var markerArray = [];

        // Instantiate a directions service.
        var directionsService = new google.maps.DirectionsService;

        // Create a renderer for directions and bind it to the map.
        var directionsDisplay = new google.maps.DirectionsRenderer({map: map});

        // Instantiate an info window to hold step text.
        var stepDisplay = new google.maps.InfoWindow;

        // Display the route between the initial start and end selections.
        // calculateAndDisplayRoute(
        //     directionsDisplay, directionsService, markerArray, stepDisplay, map);
        // Listen to change events from the start and end lists.
        // var onChangeHandler = function() {
        //   calculateAndDisplayRoute(
        //       directionsDisplay, directionsService, markerArray, stepDisplay, map);
        // };
        // document.getElementById('start').addEventListener('change', onChangeHandler);
        // document.getElementById('end').addEventListener('change', onChangeHandler);
      }

google.maps.event.addDomListener(window, "load", getLocation);


function getLocation() {
    if (navigator.geolocation) {  // when the browser has geolocation capability
        navigator.geolocation.getCurrentPosition(handlePositionFound); // when you get the lat/long from the browser, give it as an argument to showPosition.
    } else {
        console.log("Geolocation is not supported by the browser.");
    } 
  } 

function handlePositionFound(position) { //get the coords
    console.log("Latitude: "+ position.coords.latitude + "<br> Longitude: " + position.coords.longitude);
  var userLat = $("#lat").val(position.coords.latitude); //user_lat
  var userLng = $("#lng").val(position.coords.longitude); //user_lng

  var marker = new google.maps.Marker({
    position: {lat:parseInt(userLat), lng: parseInt(userLng)},
    setMap: 'homepage-map',
    title: 'User location!'
  }); 

initMap(position.coords.latitude, position.coords.longitude);
}


  
//FROM LECTURE NOTES ADDING MARKERS 
// function addMarker() {
//   var myImageURL = 'https://developers.google.com/maps/documentation/javascript/examples/full/images/beachflag.png';
//   var image = myImageURL;
//   var nearHackbright = new google.maps.LatLng(37.7886679, -122.4114987)
//   var marker = new google.maps.Marker({
//                 position = nearHackbright,
//                 map: map, 
//                 title: 'Hover text',
//                 icon: image
//   });
//   return marker;
// }
// var marker = addMarker()














