import requests

# Define the URL and query parameters
url = 'http://127.0.0.1:5000/predict'
params = {'L1': 5.1,
    'W1': 3.5,
    'L2': 1.4,
    'W2': 0.2}

# Make the GET request
response = requests.get(url, params=params)

# Print the response
print(response.json())

response=response.json()
print(response['probabilities'])