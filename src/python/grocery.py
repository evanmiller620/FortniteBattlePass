import requests

def get_nearest_grocery_with_distance(lat, lon, api_key):
    # Step 1: Relaxed nearby search using keyword
    base_url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
    radii = [1000, 2000, 5000]
    keyword = "grocery"

    best_place = None

    for radius in radii:
        params = {
            "location": f"{lat},{lon}",
            "radius": radius,
            "keyword": keyword,
            "key": api_key
        }
        r = requests.get(base_url, params=params)
        if r.status_code != 200:
            print(f"Google Places API error: {r.status_code}")
            continue

        data = r.json()
        if data.get("status") != "OK":
            print(f"Google Places returned status: {data.get('status')}")
            continue

        results = data.get("results", [])
        if not results:
            continue

        best_place = results[0]
        break

    if not best_place:
        return "⚠️ No grocery stores found nearby (even with fallback)."

    dest_lat = best_place['geometry']['location']['lat']
    dest_lon = best_place['geometry']['location']['lng']
    name = best_place.get('name', 'Unnamed')
    address = best_place.get('vicinity', 'Unknown address')

    # Step 2: Get distance using Directions API
    directions_url = "https://maps.googleapis.com/maps/api/directions/json"
    directions_params = {
        "origin": f"{lat},{lon}",
        "destination": f"{dest_lat},{dest_lon}",
        "mode": "walking",
        "key": api_key
    }

    d = requests.get(directions_url, params=directions_params)
    if d.status_code != 200:
        return f"❌ Directions API error: {d.status_code}"

    dir_data = d.json()
    if dir_data['status'] != 'OK' or not dir_data['routes']:
        return "❌ Could not retrieve route."

    leg = dir_data['routes'][0]['legs'][0]
    distance_m = leg['distance']['value']
    duration_min = leg['duration']['value'] / 60

    return {
        'store': name,
        'address': address,
        'distance_m': round(distance_m, 1),
        'distance_km': round(distance_m / 1000, 2),
        'walk_minutes': round(duration_min, 1),
        'coordinates': (dest_lat, dest_lon)
    }