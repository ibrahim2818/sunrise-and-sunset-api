import requests

response1 = requests.get(url="http://api.open-notify.org/iss-now.json")
response1.raise_for_status
lati= response1.json()["iss_position"]["latitude"]
longi= response1.json()["iss_position"]["longitude"]

response2= requests.get(url= f"https://api.sunrise-sunset.org/json?lat={lati}&lng={longi}")
response2.raise_for_status
sunrise= response2.json()["results"]["sunrise"]
sunset= response2.json()["results"]["sunset"]
print(f"sunrise:{sunrise}\nsunset: {sunset}")
