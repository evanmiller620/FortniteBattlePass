'use client';
import { useRef, useState } from 'react';
import { useEffect } from 'react';



export default function MenuBar() {
  const [open, setOpen] = useState(false);
  const [searchTerm, setSearchTerm] = useState('');
  const [searchResults, setSearchResults] = useState<any[]>([]);
  const [isSearching, setIsSearching] = useState(false);
  const menuRef = useRef<HTMLDivElement>(null);
  
  useEffect(() => {
    const handleSearch = async () => {
      if (searchTerm.trim() === '') {
        setSearchResults([]);
        return;
      }
      
      setIsSearching(true);
      try {
        // Using default coordinates for demo - you may want to get actual user location
        const results = ["balling", "clubbing", "drinking", "eating", "shopping", "attractions"];
        setSearchResults(results);
      } catch (error) {
        console.error('Error searching places:', error);
      } finally {
        setIsSearching(false);
      }
    };
    
    const debounceTimer = setTimeout(handleSearch, 500);
    return () => clearTimeout(debounceTimer);
  }, [searchTerm]);

  return (
    <>
      <button
        className="fixed top-4 left-4 z-50 w-12 h-12 bg-black/60 backdrop-blur-md text-white rounded-full flex items-center justify-center shadow-md hover:bg-black/80 transition-colors"
        onClick={() => setOpen(!open)}
        aria-label="Toggle Menu"
      >
        {open ? '✖' : '☰'}
      </button>

      <div
        ref={menuRef}
        className={`fixed top-0 left-0 h-full w-64 z-40 bg-white/90 backdrop-blur-md shadow-xl transform transition-transform duration-300 ${open ? 'translate-x-0' : '-translate-x-full'
          }`}
      >
        
        <div className="px-6 pt-20 pb-6 space-y-4 text-black">
          {/* <h2 className="text-xl font-semibold">Vibes</h2> */}
          <div className="relative mb-4">
            <div className="absolute inset-y-0 left-0 flex items-center pl-3 pointer-events-none">
              <svg className="w-4 h-4 text-gray-500" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 20 20">
                <path stroke="currentColor" strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="m19 19-4-4m0-7A7 7 0 1 1 1 8a7 7 0 0 1 14 0Z" />
              </svg>
            </div>
            <input
              type="search"
              className="block w-full p-2.5 pl-10 text-sm text-gray-900 border border-gray-300 rounded-lg bg-white focus:ring-blue-500 focus:border-blue-500"
              placeholder="Search places..."
              value={searchTerm}
              onChange={(e) => setSearchTerm(e.target.value)}
            />
          </div>

          {isSearching && (
            <div className="flex items-center justify-center">
              <div className="w-5 h-5 border-t-2 border-b-2 border-gray-500 rounded-full animate-spin"></div>
              <span className="ml-2 text-sm text-gray-500">Searching...</span>
            </div>
          )}

          {searchResults.length > 0 && (
            <div className="mb-4">
              <h3 className="text-lg font-medium mb-2">Search Results</h3>
              <ul className="space-y-1 max-h-60 overflow-y-auto">
                {searchResults.map((place, index) => (
                  <li key={index} className="px-3 py-2 hover:bg-gray-100 rounded-md text-sm transition cursor-pointer">
                    {place.name || place.title}
                  </li>
                ))}
              </ul>
            </div>
          )}

        </div>
      </div>
    </>
  );
}
