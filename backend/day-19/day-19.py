import requests

base_url = 'https://api.spacexdata.com/v5/launches/latest'

response = requests.get(base_url)

if response.status_code == 200:
  # Parse JSON content from the response
  launch_data = response.json()

  # Display launch information
  print(f"Name: {launch_data['name']}")
  print(f"Details: {launch_data['details']}")
  print(f"Launchpad ID: {launch_data['launchpad']}")
  print(f"Flight Number:{launch_data['flight_number']}")
  print(f"Date UTC: {launch_data['date_utc']}")
  print(f"Upcoming: {launch_data['upcoming']}")
else:
  print("ERROR Could not Retrieve Information")