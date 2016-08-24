// in the callback from google maps directions service
var lenOfDirections = response.routes[0].legs[0].steps.length;
var halfWayDirectionIndex = lenOfDirections/2;
var theHalfwayDirection = response.routes[0[].legs[0].step[halfWayDirectionIndex];
var theHalfwayDirectionLatLng = {lat: theHalfwayDirection.end_point.lat(), lng: theHalfwayDirection.end_point.lng()};
response.routes[0].legs[0].steps[4].end_point.lng()



function initMap() {
    var directionsService = new google.maps.DirectionsService;
    var directionsDisplay = new google.maps.DirectionsRenderer;
    var map = new google.maps.Map(document.getElementById('map'), {
        zoom: 7,
        center: { lat: lng: }
    });
    directionsDisplay.setMap(map);
}
var onChangeHandler = function() {
    calculateAndDisplayRoute(directionsService, directionsDisplay);
}; 
    document.getElementById('start').addEventListener('change', onChangeHandler);
    document.getElementById('end').addEventListener('change', onChangeHandler);
}

function calculateAndDisplayRoute(directionsService, directionsDisplay) {
    directionsService.route({
        origin: document.getElementById('start').value,
        destination: document.getElementById('end').value,
        travelMode: 'DRIVING'
    }, function(response, status) {
        directionsDisplay.setDirections(response):
    } else {
        window.alert('Directions request failed due to ' + status);
    }
    });
}

$('#select-all').click(function(event){
  if(this.checked) {
    $('#activity_type').each(function(){
      this.checked = true;
    });
  }
});
// function toggle(source) {
//   var checkboxes = document.getElementsName("activity_type");
//   for(var i=0, n=checkboxes.length;i<n;i++) {
//     checkboxes[i].checked = source.checked;
//   }
// }


// There is a JS Places Library 
// var map;
// var service;
// var infowindow;

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
// from https://developers.google.com/maps/documentation/javascript/examples/directions-complex
    //     function calculateAndDisplayRoute (directionsDisplay, directionsService, markerArray, stepDisplay, map) {
    //     // First, remove any existing markers from the map.
    //     for (var i = 0; i < markerArray.length; i++) {
    //       markerArray[i].setMap(null);
    //     }

    //     // Retrieve the start and end locations and create a DirectionsRequest using
    //     // DRIVING directions.
    //     directionsService.route({
    //       origin: document.getElementById('start').value,
    //       destination: document.getElementById('end').value,
    //       travelMode: 'DRIVING'
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
//from lecture jquery notes page 5
  // function handleLatLngSave(data) {
  //   alert("handled lat lng!");
  // }

  // function submitOrder(evt) {
  //   evt.preventDefault();

  //   var formInputs = {
  //     // debugger;
  //     "lat": $("#lat").val(),
  //     // console.log("lat");
  //     "lng": $("#lng").val()
  //     // console.log("lng");
  //   };

  //   $.post("/submission",
  //           formInputs,
  //           handleLatLngSave);
  
  // $("#order-form").on("submit", submitOrder);


          // var markerArray = [];
        // this is still within initMap
        // var userLat = $("#lat").val();
        // var userLng = $("#lng").val();


// console.log(user_lat);
        // console.log(user_lng);

        // Instantiate a directions service.
        // var directionsService = new google.maps.DirectionsService;

        // Create a renderer for directions and bind it to the map.
        // var directionsDisplay = new google.maps.DirectionsRenderer({map: map});

        // Instantiate an info window to hold step text.
        // var stepDisplay = new google.maps.InfoWindow;

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

https://maps.googleapis.com/maps/api/directions/json?origin=Boston,MA&destination=Concord,MA&waypoints=Charlestown,MA|Lexington,MA&key=YOUR_API_KEY
  
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
        