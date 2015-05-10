var contentString = '<div id="content">'+
      '<div id="siteNotice">'+
      '</div>'+
      '<h4 id="firstHeading" class="firstHeading">RISTORANTE ALBERGO MOTTA</h4>'+
      '<div id="bodyContent">'+
      '<p>Via Dante Alighieri, 11<br>25057 Sale Marasino (BS) ITALY</p>'+
      '<p>TEL. +39.030.9824265 - info@ristorantealbergomotta.it</p>'
      '</div>'+
      '</div>';
  var infowindow = new google.maps.InfoWindow({
      content: contentString
  });
var geocoder;
var map;
function initialize(latlng) {
  geocoder = new google.maps.Geocoder();
  var latlng = new google.maps.LatLng(45.55425,9.99686);
  var mapOptions = {
    zoom: 10,
    center: latlng,
    mapTypeId: google.maps.MapTypeId.ROADMAP
  }
  map = new google.maps.Map(document.getElementById("map-canvas"), mapOptions);
}
function codeAddress(address) {
  if (typeof(address) == 'undefined') var address = document.getElementById("address").value;
  geocoder.geocode( { 'address': address}, function(results, status) {
    if (status == google.maps.GeocoderStatus.OK) {
      map.setCenter(results[0].geometry.location);
      var marker = new google.maps.Marker({
        map: map,
        position: results[0].geometry.location
    });
       google.maps.event.addListener(marker, 'click', function() {
        infowindow.open(map,marker);
      });
    } else {
    alert("Geocode was not successful for the following reason: " + status);
    }
  });
}
window.onload = function() {
    initialize();
    
    //replace this with the address you want the page to start at
    var myAddress = "Via Dante Alighieri, 11 - 25057 Sale Marasino (BS) ITALY";
    codeAddress(myAddress);
}
