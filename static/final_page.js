$(document).ready(function () {
    console.log("HEY YOU, I AM HERE in the document.ready");
    //////////////////////////////////////////////////////////////////////////////////

    // from Google Maps lecture 

    // need a function to initMap

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
    $("#end_lat").data()
    initMap(activity, )
    function initMap(activity, user_end) {

        //rendering a new map on the homepage in the div homepage-map
        var user_lat = $("#lat").val();
        var user_lng = $("#lng").val();
        var activity_lat = $("#activity_lat").val();
        var activity_lng = $("#activity_lng").val();
        var end_lat = $("#end_lat").val();
        var end_lng = $("#end_lng").val();
        var user_latlng = {lat: user_lat, lng: user_lng};
        var final_map = new google.maps.Map(document.getElementById('final-map'), {
          //this function gets the values out of the DOM, see handlePositionFound
              center: user_latlng,
              zoom: 18
              // zoomControl: false,
        });    
        var userMarker = addMarker(final_map, user_latlng);
        var activityMarker = addMarker(final_map, activity);
        var userEndMarker = addMarker(final_map, user_end);
        displayDirections(final_map);
    }
}
    google.maps.event.addDomListener(window, "load", getLocation);

    function displayDirections(map) {
        var user_lat = $("#user_lat").val();
        var user_lng = $("#user_lng").val();
        var activity_lat = $("#activity_lat").val();
        var activity_lng = $("#activity_lng").val();
        var end_lat = $("#end_lat").val();
        var end_lng = $("#end_lng").val();
        var user_latlng = {lat: user_lat, lng: user_lng};
        console.log(user_latlng);
        var activity = {lat: activity_lat, lng: activity_lng};
        console.log(activity);
        var user_end = {lat: end_lat, lng: end_lng};
        console.log(user_end);
        var activityWaypoint = {
            location: activity,
            stopover: true
        };
        var routeOptions = {
            origin: user_latlng,
            desintation: user_end,
            waypoints: [activityWaypoint],
            travelMode: google.maps.TravelMode.DRIVING
        };

        var directionsService = new google.maps.DirectionsService;
        directionsService.route(routeOptions, function(response, status) {
            if (status === google.maps.DirectionsStatus.OK) {
                directionsDisplay.setDirections(response);
            } else {
                window.alert('Directions request failed due to ' + status);
            }
        });

        var directionsDisplay = new google.maps.DirectionsRenderer;
        directionsDisplay.setMap(map);
    }

    function addMarker(map, user_latlng) {
        var user_lat = $("#user_lat").val();
        var user_lng = $("#user_lng").val();
        var activity_lat = $("#activity_lat").val();
        var activity_lng = $("#activity_lng").val();
        var end_lat = $("#end_lat").val();
        var end_lng = $("#end_lng").val(); 
        var user_latlng = {lat: user_lat, lng: user_lng};    
        var marker = new google.maps.Marker({
            position: user_latlng, //parseInt() rounds so the marker isn't on their current location
            // title: 'User location!',
            map: map
        });
      return marker;
    }



    //HELLO!!!!!!

}); //end documentReady