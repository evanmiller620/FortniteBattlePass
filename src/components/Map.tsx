'use client';
import { useEffect } from 'react';
import mapboxgl from 'mapbox-gl';
mapboxgl.accessToken = process.env.MAPBOX_ACCESS_TOKEN || 'pk.eyJ1Ijoib2poYXIiLCJhIjoiY205ZWdtNTRhMWJmbjJrcHY3MGd3MGcxdCJ9.OSjbsd5Mo7U2t2jw1QH74w';

const fetchPlaces = async (lat: number, lng: number, filter?: string) => {
  const params = new URLSearchParams({ lat: lat.toString(), lng: lng.toString() });
  if (filter) params.append('filter', filter);

  const res = await fetch(`/api/place-info?${params.toString()}`);
  const data = await res.json();
  return data.places;
};

const Map = () => {
    useEffect(() => {
        const map = new mapboxgl.Map({
            container: 'map',
            style: 'mapbox://styles/mapbox/streets-v11',
            config: {
                basemap: {
                    lightPreset: 'dusk',
                    showPointOfInterestLabels: false,
                }
            },
            center: [-86.9081, 40.4259],
            zoom: 12,
        });

        map.on('click', async (e) => {
            const places = await fetchPlaces(e.lngLat.lat, e.lngLat.lng);
            console.log(places);
        });

        return () => map.remove();
    }, []);

    return <div id="map" style={{ width: '100%', height: '100vh' }} />;
};

export default Map;