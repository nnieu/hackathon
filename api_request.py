# import requests

# # API endpoint URL
# url = 'https://www.googleapis.com/geolocation/v1/geolocate?key=YOUR_API_KEY'

# # Sample request data (Wi-Fi access points)
# data = {
#     "wifiAccessPoints": [
#         {"macAddress": "00:11:22:33:44:55", "signalStrength": -65, "signalToNoiseRatio": 40},
#         {"macAddress": "66:77:88:99:AA:BB", "signalStrength": -70, "signalToNoiseRatio": 35}
#     ]
# }

# # Make POST request to the API
# response = requests.post(url, json=data)

# # Check if the request was successful (status code 200)
# if response.status_code == 200:
#     # Parse and print the response data
#     location = response.json()['location']
#     accuracy = response.json()['accuracy']
#     print("Latitude:", location['lat'])
#     print("Longitude:", location['lng'])
#     print("Accuracy (meters):", accuracy)
# else:
#     print("Error:", response.status_code)
