##https://www.nylas.com/blog/use-python-requests-module-rest-apis/

import requests
import json
import uuid

response = requests.get("http://api.open-notify.org/astros.json")
##print(response)

#print(response.content()) # Return the raw bytes of the data payload
#response.text() # Return a string representation of the data payload
##print(response.json()) # This method is convenient when the API returns JSON

##query = {'lat':'45', 'lon':'180'}
##response = requests.get('http://api.open-notify.org/iss-pass.json', params=query)
payload = response.json()

dump = json.dumps(payload, indent=4)

print(dump)

print(type(payload))

people = (payload['people'])

print(people)

print(json.dumps(people, indent=4))

class Astronaut ():
    def __init__(self, name, craft):
        self.name = name
        self.craft = craft
    
    def get_astronaut_details(self):
        print(f"I am {self.name} from the craft {self.craft}.")

for key in people:
    name = (key['name'])
    craft = (key['craft'])
    astronaut = Astronaut(name,craft)
    astronaut.get_astronaut_details()

astronaut_list_id = uuid.uuid4()

data = {
"astronaut_list_id": str(astronaut_list_id),
"astronauts" : str(people)
}

print(data)

print(type(data))

print(data['astronaut_list_id'])

class Astronauts(object):
    def __init__(self, astronauts: Astronaut):
         self.astronaut_list_id = uuid.uuid4()
         self.astronauts = astronauts

    def get_payload(self):
        data = {
            "astronaut_list_id": str(self.astronaut_list_id),
            "astronauts" : str(self.astronauts)
            }
        return data

    # def get_astronaut_details(self):
    #    for astronaut in self.astronauts:
    #         astronaut.get_astronaut_details()

astronauts = Astronauts(people)
print(astronauts.get_payload())
#astronauts.get_astronaut_details()
