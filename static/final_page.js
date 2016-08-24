$(document).ready(function () {
    console.log("HEY YOU, I AM HERE in the document.ready");
    //////////////////////////////////////////////////////////////////////////////////

    // from Google Maps lecture 

    // need a function to initMap
    function initMap(user_lat, user_lng, business_lat, business_lng, end_lat, end_lng) {

        //rendering a new map on the homepage in the div homepage-map
        var user_lat = $("#user_lat").val();
        var user_lng = $("#user_lng").val();
        var activity_lat = $("#activity_lat").val();
        var activity_lng = $("#activity_lng").val();
        var end_lat = $("#end_lat").val();
        var end_lng = $("#end_lng").val();
        var user_lat = $("#user_lat").val();
        var user_lng = $("#user_lng").val();
        var final_map = new google.maps.Map(document.getElementById('final-map'), {
          //this function gets the values out of the DOM, see handlePositionFound
              center: {lat: user_lat, lng: user_lng},
              zoom: 18
              // zoomControl: false,
        });    
        var userMarker = addMarker(final_map, user_lat, user_lng);
        var activityMarker = addMarker(final_map, activity_lat, activity_lng);
        var userEndMarker = addMarker(final_map, user_lat, user_lng);
        displayDirections(final_map);
    }

    google.maps.event.addDomListener(window, "load", initMap);

    function displayDirections(map) {
        var user_lat = $("#user_lat").val();
        var user_lng = $("#user_lng").val();
        var activity_lat = $("#activity_lat").val();
        var activity_lng = $("#activity_lng").val();
        var end_lat = $("#end_lat").val();
        var end_lng = $("#end_lng").val();
        var user_lat = $("#user_lat").val();
        var user_lng = $("#user_lng").val();
        var activityWaypoint = {
            location: {lat: activity_lat, lng: activity_lng},
            stopover: true
        };
        var routeOptions = {
            origin: {lat: user_lat, lng: user_lng},
            desintation: {lat: end_lat, lng: end_lng},
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

    function addMarker(map, user_lat, user_lng) {
        var user_lat = $("#user_lat").val();
        var user_lng = $("#user_lng").val();
        var activity_lat = $("#activity_lat").val();
        var activity_lng = $("#activity_lng").val();
        var end_lat = $("#end_lat").val();
        var end_lng = $("#end_lng").val();
        var user_lat = $("#user_lat").val();
        var user_lng = $("#user_lng").val();  
        var marker = new google.maps.Marker({
            position: {lat: user_lat, lng: user_lng}, //parseInt() rounds so the marker isn't on their current location
            // title: 'User location!',
            map: map
        });
      return marker;
    }



    //HELLO!!!!!!

}); //end documentReady