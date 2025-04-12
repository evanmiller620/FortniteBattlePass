import requests

def reverse_geocode(lat, lon, access_token):
    url = f"https://api.mapbox.com/geocoding/v5/mapbox.places/{lon},{lat}.json"
    params = {
        'access_token': access_token,
        'types': 'address,place,region,postcode,country',
        'limit': 1
    }

    response = requests.get(url, params=params)
    if response.status_code != 200:
        return f"Error: {response.status_code}"

    data = response.json()
    if not data['features']:
        return "No address found"

    return data['features'][0]['place_name']


def extract_tilequery_address(features):
    house_num = None
    street = None

    for f in features:
        props = f.get('properties', {})
        layer = props.get('tilequery', {}).get('layer', '')

        if 'house_num' in props and house_num is None:
            house_num = props['house_num']
        if props.get('class') == 'street' and 'name' in props and street is None:
            street = props['name']

    return f"{house_num} {street}" if house_num and street else None


def get_full_address(lat, lon, tilequery_features, token):
    tilequery_address = extract_tilequery_address(tilequery_features)
    reverse_address = reverse_geocode(lat, lon, token)

    if tilequery_address and reverse_address:
        # Try merging them smartly
        components = reverse_address.split(',', maxsplit=1)
        return f"{tilequery_address}, {components[1].strip()}" if len(components) > 1 else reverse_address
    else:
        return reverse_address or tilequery_address or "Unknown address"