##https://www.nylas.com/blog/use-python-requests-module-rest-apis/

import requests
import uuid
from azure.cosmos import CosmosClient, PartitionKey
import os

response = requests.get("http://api.open-notify.org/astros.json")

payload = response.json()

people = (payload['people'])

astronaut_list_id = uuid.uuid4()

class Astronaut ():
    def __init__(self, name, craft):
        self.name = name
        self.craft = craft
    
    def get_astronaut_details(self):
        print(f"I am {self.name} from the craft {self.craft}.")

class Astronauts(object):
    def __init__(self, astronauts: Astronaut):
         self.astronaut_list_id = uuid.uuid4()
         self.astronauts = astronauts

    def get_payload(self):
        data = {
            "id": str(self.astronaut_list_id),
            "astronauts" : str(self.astronauts)
            }
        return data

astronauts = Astronauts(people)
data = (astronauts.get_payload())

print("Create cosmos client...")
endpoint = ""
key = ""
client = CosmosClient(endpoint, key)
print("Created cosmos client.")

print("Create database...")
database_name = 'apitest'
database = client.create_database_if_not_exists(id=database_name)
print("Database created.")

print("Create container...")
container_name = 'astronauts'
container = database.create_container_if_not_exists(
    id=container_name, 
    partition_key=PartitionKey(path="/id")
)
print("Container created.")

print(data)

container.create_item(body=data)
