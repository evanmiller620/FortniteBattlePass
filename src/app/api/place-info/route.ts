import { NextRequest, NextResponse } from 'next/server';

export async function GET(req: NextRequest) {
  const { searchParams } = new URL(req.url);
  const lat = searchParams.get('lat');
  const lng = searchParams.get('lng');
  const filter = searchParams.get('filter');

  if (!lat || !lng) {
    return NextResponse.json({ message: 'Missing lat or lng' }, { status: 400 });
  }

  const latitude = parseFloat(lat);
  const longitude = parseFloat(lng);

  // Mock data — replace with real logic or DB/API fetch later
  const places = [
    {
      name: 'Desert Outpost',
      category: 'landmark',
      description: 'Historical desert trading spot',
      coordinates: [latitude, longitude],
    },
    {
      name: 'Cactus Café',
      category: 'cafe',
      coordinates: [latitude, longitude],
    },
  ];

  const filtered = filter
    ? places.filter((place) => place.category === filter)
    : places;

  return NextResponse.json({ places: filtered });
}
