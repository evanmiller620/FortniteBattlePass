import Head from 'next/head';
import Map from '../components/Map';
import MenuBar from '../components/MenuBar';
import MapboxGeocoderComponent from '../components/MapboxGeocoder';
const Home = () => (
  <>
    <Head>
      <title>Vibes</title>
      <link
        href="https://api.mapbox.com/mapbox-gl-js/v2.15.0/mapbox-gl.css"
        rel="stylesheet"
      />
    </Head>

    <div className="overflow-x-hidden overflow-y-hidden relative">
      <MenuBar />
      <Map />
    </div>
  </>
);

export default Home;
