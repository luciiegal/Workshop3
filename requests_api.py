import requests

# Define the URL and query parameters
url = 'http://127.0.0.1:5000/predict'
params = {'sepal_length': 5.1,
    'sepal_width': 3.5,
    'petal_length': 1.4,
    'petal_width': 0.2}

# Make the GET request
response = requests.get(url, params=params)

# Print the response
print(response.json())

response=response.json()
print(response['probabilities'])