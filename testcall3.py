##https://www.nylas.com/blog/use-python-requests-module-rest-apis/

import requests
import uuid

craft = "ISS" #Shenzhou 13

class Astronaut ():
    def __init__(self, name, craft):
        self.name = name
        self.craft = craft
    
    def get_astronaut_details(self):
        detail = (f"<p>Hello I am {self.name} and I am in the spacecraft {self.craft}.</p>")
        return detail

class Astronauts(object):
    def __init__(self):
        self.astronaut_list_id = uuid.uuid4()
        response = requests.get("http://api.open-notify.org/astros.json")
        payload = response.json()
        self.astronauts: Astronaut = (payload['people'])

    def get_payload(self):
        data = {
            "astronaut_list_id": str(self.astronaut_list_id),
            "astronauts" : str(self.astronauts)
            }
        return data

    def filter_astronauts(self, craft):
        self.astronauts = list(filter(lambda d: d['craft'] in craft, self.astronauts))

    def get_astronauts_html(self):
        html = ""
        for key in self.astronauts:
            name = (key['name'])
            craft = (key['craft'])
            astronaut = Astronaut(name,craft)
            html = html + astronaut.get_astronaut_details()
        return html

astronauts = Astronauts()
astronauts.filter_astronauts(craft)
html = astronauts.get_astronauts_html()
print(html)
