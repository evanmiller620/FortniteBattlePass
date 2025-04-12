'use client';
import { useEffect, useRef, useState } from 'react';
import mapboxgl from 'mapbox-gl';
import Sidebar from './Sidebar';

mapboxgl.accessToken = process.env.MAPBOX_ACCESS_TOKEN || 'pk.eyJ1Ijoib2poYXIiLCJhIjoiY205ZWdtNTRhMWJmbjJrcHY3MGd3MGcxdCJ9.OSjbsd5Mo7U2t2jw1QH74w';

const fetchPlaces = async (lat: number, lng: number, filter?: string) => {
  const params = new URLSearchParams({ lat: lat.toString(), lng: lng.toString() });
  if (filter) params.append('filter', filter);

  const res = await fetch(`/api/place-info?${params.toString()}`);
  const data = await res.json();
  return data.places;
};

const Map = () => {
  const markerRef = useRef<mapboxgl.Marker | null>(null);
  const [places, setPlaces] = useState<any[]>([]);
  const [isSidebarVisible, setSidebarVisible] = useState(false);

  useEffect(() => {
    const map = new mapboxgl.Map({
      container: 'map',
      style: 'mapbox://styles/mapbox/streets-v11',
      center: [-86.9081, 40.4259],
      zoom: 12,
    });

    map.on('click', async (e) => {
      // Remove existing marker if it exists
      if (markerRef.current) {
        markerRef.current.remove();
      }

      markerRef.current = new mapboxgl.Marker()
        .setLngLat([e.lngLat.lng, e.lngLat.lat])
        .addTo(map);

      const places = await fetchPlaces(e.lngLat.lat, e.lngLat.lng);
      setPlaces(places);
      setSidebarVisible(true);
    });

    return () => map.remove();
  }, []);

  return (
    <div style={{ display: 'flex', height: '100vh' }}>
      <div id="map" style={{ width: '100%', height: '100%' }} />
      <Sidebar isVisible={isSidebarVisible} places={places} />
    </div>
  );
};

export default Map;