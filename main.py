import requests

# Get the ISS current location
response1 = requests.get(url="http://api.open-notify.org/iss-now.json")
response1.raise_for_status()  # Called as a method
lati = response1.json()["iss_position"]["latitude"]
longi = response1.json()["iss_position"]["longitude"]

# Parameters for the second API request
parameters = {
    "lat": lati,
    "lng": longi
}

# Fetch sunrise and sunset times using the latitude and longitude
response2 = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response2.raise_for_status()  # Called as a method
sunrise = response2.json()["results"]["sunrise"]
sunset = response2.json()["results"]["sunset"]

# Print the results
print(f"Sunrise: {sunrise}\nSunset: {sunset}")
