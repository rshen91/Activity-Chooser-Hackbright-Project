$(document).ready(function () {
//////////////////////////////////////////////////////////////////////////////////
//JS for choose_activity.html where a map is on the page showing the different businesses as markers

// google.maps.event.addDomListener(window, "load", getLocation); 
// from Google Maps lecture 
var user_latlng = {lat: , lng: }
var activity = {lat: , lng: }
var user_end = {lat: , lng: }

var activityWaypoint = {
    location: activity,
    stopover: true
}
function initMap() {
  var directionsService = new google.maps.DirectionsService;
  var directionsDisplay = new google.maps.DirectionsRenderer;
  var final_map = new google.maps.Map(document.getElementById('final-map'), {
      zoom: 6,
      center: activity  //what are the lat lngs I want for the center of the map? 
        });
directionsDisplay.setMap(final_map);

// document.getElementById('submit').addEventListener('click', function(){
//   calculateAndDisplayRoute(directionsService, directionsDisplay);
// }); 
// }

// function calculateAndDisplayRoute (directionsService, directionsDisplay) {
//   var waypts = []; //put the activity they choose here
// }

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