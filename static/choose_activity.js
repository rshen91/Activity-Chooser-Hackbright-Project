"use strict";


$(document).ready(function () {
console.log("HEY YOU, I AM HERE in the document.ready");

function initMap(user_lat, user_lng, end_lat, end_lng) {
    console.log('user_lat:', user_lat, 'user_lng:', user_lng);

    //rendering a new map on the homepage in the div homepage-map
    var marker_map = new google.maps.Map(document.getElementById('marker_map'), {
      //this function gets the values out of the DOM, see handlePositionFound
          center: {"lat":Number(user_lat), "lng":Number(user_lng)},
          zoom: 18
    });    

        var trafficLayer = new google.maps.TrafficLayer();
        trafficLayer.setMap(marker_map);    
        displayDirections(marker_map);
        
    }
  google.maps.event.addDomListener(window, "load", initMap);

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
      
      initMap(position.coords.latitude, position.coords.longitude);
      console.log("user lat" + user_lat);
      console.log("user lng" + user_lng);
  }

  function displayDirections(map) {
        var user_lat = $("#user_lat").val();
        var user_lng = $("#user_lng").val();
        // var activity_lat = $("#activity_lat").val();
        // var activity_lng = $("#activity_lng").val();
        var end_lat = $("#end_lat").val();
        var end_lng = $("#end_lng").val();
        var user_lat = $("#user_lat").val();
        var user_lng = $("#user_lng").val();
        // var activityWaypoint = {
        //     location: {lat: Number(activity_lat), lng: Number(activity_lng)},
        //     stopover: true
        var routeOptions = {
            origin: {lat: Number(user_lat), lng: Number(user_lng)},
            destination: {lat: Number(end_lat), lng: Number(end_lng)},
            // waypoints: [activityWaypoint],
            travelMode: google.maps.TravelMode.DRIVING
        };
        var directionsService = new google.maps.DirectionsService;
        directionsService.route(routeOptions, function(response, status) {
            if (status === google.maps.DirectionsStatus.OK) {
                directionsDisplay.setDirections(response);
            } else {
                window.alert('Directions request failed due to ' + status);
            }

        // in the callback from google maps directions service
        var lenOfDirections = response.routes[0].legs[0].steps.length;
        console.log("The length of directions "+ lenOfDirections);

        var halfWayDirectionIndex = Math.round(lenOfDirections/2);
        console.log("The halfway direction index "+ halfWayDirectionIndex);

        var theHalfwayDirection = response.routes[0].legs[0].steps[halfWayDirectionIndex];
        console.log("The halfway direction "+ theHalfwayDirection);

        var theHalfwayDirectionLatLng = {lat: Number(theHalfwayDirection.end_point.lat()), lng: Number(theHalfwayDirection.end_point.lng())};
        console.log("The theHalfwayDirectionLatLng "+ (theHalfwayDirectionLatLng);
        var halfwaylat = response.route[0].legs[0].steps[theHalfwayDirectionIndex].end_point.lat()
        var halfwayLng = response.routes[0].legs[0].steps[theHalfwayDirectionIndex].end_point.lng()
        console.log("halfwayLng " + halfwayLng);
        

        }); //end of directionsService 

        var directionsDisplay = new google.maps.DirectionsRenderer;
        directionsDisplay.setMap(map);
        } //end of displayDirections

        
    }); //end documentReady




