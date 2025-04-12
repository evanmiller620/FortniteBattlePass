// components/MapboxGeocoder.tsx

import { useEffect, useRef } from 'react';
import MapboxGeocoder from '@mapbox/mapbox-gl-geocoder';
import 'mapbox-gl/dist/mapbox-gl.css';

interface MapboxGeocoderProps {
  onResult: (result: any) => void;
}

const MapboxGeocoderComponent: React.FC<MapboxGeocoderProps> = ({ onResult }) => {
  const geocoderContainerRef = useRef<HTMLDivElement | null>(null);

  useEffect(() => {
    if (!geocoderContainerRef.current) return;

    const geocoder = new MapboxGeocoder({
      accessToken: process.env.NEXT_PUBLIC_MAPBOX_ACCESS_TOKEN!,
      placeholder: 'Search for a place',
      mapboxgl: require('mapbox-gl'),
    });

    geocoder.on('result', (event) => {
      onResult(event.result);
    });

    geocoder.addTo(geocoderContainerRef.current);

    // Cleanup on unmount
    return () => {
      geocoder.clear();
    };
  }, [onResult]);

  return <div ref={geocoderContainerRef} />;
};

export default MapboxGeocoderComponent;