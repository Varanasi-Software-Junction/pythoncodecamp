# Importing required module
from geopy.geocoders import Nominatim

# https://geopy.readthedocs.io/en/stable/
# Using Nominatim Api
geolocator = Nominatim(user_agent="geoapiExercises")

# Zipcode input
zipcode = "221007"

# Using geocode()
location = geolocator.geocode(zipcode)

# Displaying address details
print("Zipcode:", zipcode)
print("Details of the Zipcode:")
print(location)
