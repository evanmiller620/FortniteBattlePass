from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="my_geocoding_app")
location = geolocator.geocode("175 5th Avenue, New York, NY 10010")

print((location.latitude, location.longitude))

# locations based on zip code
location = geolocator.geocode("94102, San Francisco, California, US")
print((location.latitude, location.longitude))