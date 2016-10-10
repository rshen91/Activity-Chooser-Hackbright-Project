// $(document).ready(function () {
//     console.log("HEY YOU, I AM HERE in the document.ready");

    function initMap(user_lat, user_lng, business_lat, business_lng, end_lat, end_lng) {

        //getting variables out of the DOM
        var user_lat = $("#user_lat").val();
        var user_lng = $("#user_lng").val();
        var activity_lat = $("#activity_lat").val();
        var activity_lng = $("#activity_lng").val();
        var end_lat = $("#end_lat").val();
        var end_lng = $("#end_lng").val();
        var user_lat = $("#user_lat").val();
        var user_lng = $("#user_lng").val();
        //documentation for route panel
        //these appear to be set in the displayDirections function
        // var displayDirections = new google.maps.DirectionsRenderer;
        // var directionsService = new google.maps.DirectionsService;
        var final_map = new google.maps.Map(document.getElementById('final-map'), {
              center: {lat: Number(user_lat), lng: Number(user_lng)},
              zoom: 18
        });
        directionsDisplay(final_map);
        // directionsDisplay(document.getElementById('right-panel'));


        var onChangeHandler = function(){
            calculateAndDisplayRoute(directionsService, displayDirections);

        //sets the map traffic layer
        var trafficLayer = new google.maps.TrafficLayer();
        trafficLayer.setMap(final_map);    

        //adding the markers
        var userMarker = addMarker(final_map, Number(user_lat), Number(user_lng));
        var activityMarker = addMarker(final_map, activity_lat, activity_lng);
        var userEndMarker = addMarker(final_map, Number(end_lat), Number(end_lng));
        
    }//for onChangeHandler
    };
    google.maps.event.addDomListener(window, "load", initMap);

    function directionsDisplay(map) {
        var user_lat = $("#user_lat").val();
        var user_lng = $("#user_lng").val();
        var activity_lat = $("#activity_lat").val();
        var activity_lng = $("#activity_lng").val();
        var end_lat = $("#end_lat").val();
        var end_lng = $("#end_lng").val();
        var user_lat = $("#user_lat").val();
        var user_lng = $("#user_lng").val();
        var activityWaypoint = {
            location: {lat: Number(activity_lat), lng: Number(activity_lng)},
            stopover: true
        };
        var routeOptions = {
            origin: {lat: Number(user_lat), lng: Number(user_lng)},
            destination: {lat: Number(end_lat), lng: Number(end_lng)},
            waypoints: [activityWaypoint],
            travelMode: google.maps.TravelMode.DRIVING
        };

        var directionsService = new google.maps.DirectionsService;
        directionsService.route(routeOptions, function(response, status) {
            if (status === google.maps.DirectionsStatus.OK) {
                displayDirections.setDirections(response);

            } else {
                window.alert('Directions request failed due to ' + status);
            }
        });

        var displayDirections = new google.maps.DirectionsRenderer;
        displayDirections.setMap(map);

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
            position: {lat: Number(user_lat), lng: Number(user_lng)}, 
            map: map
        });
      return marker;
    }

// }
// ); //end documentReady

