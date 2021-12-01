##https://www.nylas.com/blog/use-python-requests-module-rest-apis/

import requests

import requests
response = requests.get("http://api.open-notify.org/astros.json")
print(response)

#print(response.content()) # Return the raw bytes of the data payload
#response.text() # Return a string representation of the data payload
print(response.json()) # This method is convenient when the API returns JSON

query = {'lat':'45', 'lon':'180'}
response = requests.get('http://api.open-notify.org/iss-pass.json', params=query)
print(response.json())

# Create a new resource
response = requests.post('https://httpbin.org/post', data = {'key':'value'})
# Update an existing resource
requests.put('https://httpbin.org/put', data = {'key':'value'})

print(response.headers["date"]) 


# requests.get(
#   'https://api.github.com/user', 
#   auth=HTTPBasicAuth('username', 'password')
# )

# my_headers = {'Authorization' : 'Bearer {access_token}'}
# response = requests.get('http://httpbin.org/headers', headers=my_headers)

# session = requests.Session()
# session.headers.update({'Authorization': 'Bearer {access_token}'})
# response = session.get('https://httpbin.org/headers')

## robust!

try:
    response = requests.get('http://api.open-notify.org/astros.json', timeout=5)
    response.raise_for_status()
    # Code here will only run if the request is successful
    print('poop')
except requests.exceptions.HTTPError as errh:
    print(errh)
except requests.exceptions.ConnectionError as errc:
    print(errc)
except requests.exceptions.Timeout as errt:
    print(errt)
except requests.exceptions.RequestException as err:
    print(err)