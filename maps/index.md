---
layout: page
title: Collection of Map
published: true
---

## Vector Maps

<div id="vector-map" class="map-preview"></div>

<div id="map-container">
	<button id="vector-osm-bright" class="map-button">OSM Bright</button
	><button id="vector-osm-basic" class="map-button">Basic Map</button>
</div>

<script src='https://api.tiles.mapbox.com/mapbox-gl-js/v0.12.1/mapbox-gl.js'></script>
<link href='https://api.tiles.mapbox.com/mapbox-gl-js/v0.12.1/mapbox-gl.css' rel='stylesheet' />

<script>
	mapboxgl.accessToken = 'pk.eyJ1IjoibW9yZ2Vua2FmZmVlIiwiYSI6IjIzcmN0NlkifQ.0LRTNgCc-envt9d5MzR75w';
	var brightMap = new mapboxgl.Map({
		    container: 'vector-map',
		    style: '/styles/bright-v8.json',
		    center: [8.54124, 47.36686],
		    zoom: 6
	});

	var bright = document.getElementById("vector-osm-bright");
	bright.onclick = function(e) {
		e.preventDefault();
        e.stopPropagation();
        var brightMap = new mapboxgl.Map({
		    container: 'vector-map',
		    style: '/styles/bright-v8.json',
		    center: [8.54124, 47.36686],
		    zoom: 6
		});
	}
	var basic = document.getElementById("vector-osm-basic");
	basic.onclick = function(e) {
		e.preventDefault();
        e.stopPropagation();
        var basicMap = new mapboxgl.Map({
		    container: 'vector-map',
		    style: '/styles/basic-v8.json',
		    center: [8.54124, 47.36686],
		    zoom: 6
		});
	}
</script>

## Raster Maps

<div id="raster-map" class="map-preview"></div>
<div id="map-container">
	<button id="raster-osm-bright" class="map-button">OSM Bright</button
	><button id="comic-map" class="map-button">Comic Map</button
	><button id="light-map" class="map-button">Light Map</button
	><button id="dark-map" class="map-button">Dark Map</button
	><button id="streets-basic" class="map-button">Streets Basic</button
	><button id="woodcut" class="map-button">Woodcut</butto><button id="pirates" class="map-button">Pirates</button
	><button id="wheatpaste" class="map-button">Wheatpaste</button>
</div>


<script src="http://cdn.leafletjs.com/leaflet/v0.7.7/leaflet.js"></script>
<link rel="stylesheet" href="http://cdn.leafletjs.com/leaflet/v0.7.7/leaflet.css" />

<script>
var map = L.map('raster-map').setView([51.505, -0.09], 13);
var layer = L.tileLayer('http://rastertiles.osm2vectortiles.org/osm-bright/{z}/{x}/{y}.png').addTo(map);

addClickListener('raster-osm-bright', 'http://rastertiles.osm2vectortiles.org/osm-bright/{z}/{x}/{y}.png');
addClickListener('comic-map', 'http://rastertiles.osm2vectortiles.org/comic/{z}/{x}/{y}.png');
addClickListener('light-map', 'http://rastertiles.osm2vectortiles.org/light/{z}/{x}/{y}.png');
addClickListener('dark-map', 'http://rastertiles.osm2vectortiles.org/dark/{z}/{x}/{y}.png');
addClickListener('streets-basic', 'http://rastertiles.osm2vectortiles.org/streets-basic/{z}/{x}/{y}.png');
addClickListener('woodcut', 'http://rastertiles.osm2vectortiles.org/woodcut/{z}/{x}/{y}.png');
addClickListener('pirates', 'http://rastertiles.osm2vectortiles.org/pirates/{z}/{x}/{y}.png');
addClickListener('wheatpaste', 'http://rastertiles.osm2vectortiles.org/wheatpaste/{z}/{x}/{y}.png');

function addClickListener(name, url) {
	var mapButton = document.getElementById(name);
	mapButton.onclick = function(e) {
		e.preventDefault();
	    e.stopPropagation();
	    layer.setUrl(url);
	}
}
</script>