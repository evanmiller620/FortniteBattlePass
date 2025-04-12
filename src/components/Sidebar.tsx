import React from 'react';

interface SidebarProps {
  isVisible: boolean;
  places: any[];
}

const Sidebar: React.FC<SidebarProps> = ({ isVisible, places }) => {
  return (
    <div
      style={{
        width: '350px',
        height: '100vh',
        position: 'fixed',
        right: isVisible ? '0' : '-350px',
        transition: 'right 0.3s ease',
        backgroundColor: '#f7f9fc',
        boxShadow: '0 2px 10px rgba(0,0,0,0.12)',
        overflowY: 'auto',
        padding: '20px',
        borderLeft: '1px solid #ddd',
        zIndex: 1000,
      }}
    >
      {/* <h2 style={{ color: '#333', fontSize: '1.5em' }}>Place Info</h2> */}
      {places.length ? (
        places.map((place, index) => (
          <div
            key={index}
            style={{
              marginBottom: '20px',
              padding: '10px 15px',
              backgroundColor: '#fff',
              borderRadius: '8px',
              boxShadow: '0 1px 3px rgba(0,0,0,0.1)',
            }}
          >
            <h3 style={{ margin: '0 0 10px', color: '#0070f3' }}>{place.name}</h3>
            <p style={{ margin: 0, color: '#555' }}>{place.description}</p>
          </div>
        ))
      ) : (
        <p style={{ color: '#888' }}>No places found.</p>
      )}
    </div>
  );
};

export default Sidebar;