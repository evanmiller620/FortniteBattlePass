'use client';

import { useRef, useState } from 'react';



export default function MenuBar() {
  const [open, setOpen] = useState(false);
  const menuRef = useRef<HTMLDivElement>(null);

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
        className={`fixed top-0 left-0 h-full w-64 z-40 bg-white/90 backdrop-blur-md shadow-xl transform transition-transform duration-300 ${
          open ? 'translate-x-0' : '-translate-x-full'
        }`}
      >
        <div className="px-6 pt-20 pb-6 space-y-4 text-black">
          <h2 className="text-xl font-semibold">Menu</h2>
          <ul className="space-y-2">
            <li className="hover:underline cursor-pointer">Map Layers</li>
            <li className="hover:underline cursor-pointer">Pins</li>
            <li className="hover:underline cursor-pointer">Settings</li>
          </ul>
        </div>
      </div>
    </>
  );
}
