mapboxgl.accessToken = 'pk.eyJ1IjoibWF4d2VscyIsImEiOiJjank3MDd1ZmMwbTBhM2dxbnUza2U3dTA5In0.HgY_TkwEuVxSBQQSyQaEcA';
var map = new mapboxgl.Map({
container: 'map', // container id
style: 'mapbox://styles/mapbox/streets-v11', // stylesheet location
center: [34.7818, 32.0853], // starting position [lng, lat]
zoom: 9 // starting zoom
});
