$(document).ready(function () {
//////////////////////////////////////////////////////////////////////////////////
//JS for choose_activity.html where a map is on the page showing the different businesses as markers

// google.maps.event.addDomListener(window, "load", getLocation); 
// from Google Maps lecture 
var user_latlng = {lat: "user_lat", lng: "user_lng"}
console.log(user_latlng);
var activity = {lat: "activity_lat", lng: "activity_lng"}
console.log(activity);
var user_end = {lat: "end_lat", lng: "end_lng"}
console.log(user_end);

var activityWaypoint = {
    location: activity,
    stopover: true
}
var routeOptions = {
    origin: user_latlng,
    desintation: user_end,
    waypoints: [activityWaypoint],
    travelMode: google.maps.TravelMode.DRIVING
}

var directionsService = new google.maps.DirectionsService;
var directionsService.route(routeOptions, function(response, status){
    if (status === google.maps.DirectionsStatus.OK) {
        directionsDisplay.setDirections(response);
    } else {
        window.alert('Directions request failed due to ' + status);
    }
});

var directionsDisplay = new google.maps.DirectionsRenderer;
directionsDisplay.setMap(map);
}

// // function addMarker(map, user_lat, user_lng) {
// //   var marker = new google.maps.Marker({
// //     position: {lat: user_lat, lng: user_lng}, //parseInt() rounds so the marker isn't on their current location
// //     title: 'User location!',
// //     map: map
// //     })

// //   var business = new google.maps.Marker({
// //     position: {lat: user_lat, lng: user_lng},
// //     title: 'Business.name',
// //     map: map
// //   })
// //   return marker;

}); //end documentReady