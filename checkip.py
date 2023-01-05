//Open in Linux Terminal//

nano checkip.py

import socket
import json
import requests
import pprint

hostname = input('Enter a domain name : ')
ip_address = socket.gethostbyname(hostname)

request_url = 'https://geolocation-db.com/jsonp/' + ip_address
response = requests.get(request_url)
geolocation = response.content.decode()
geolocation = geolocation.split("(")[1].strip(")")
geolocation = json.loads(geolocation)

for k,v in geolocation.items():
  pprint.pprint(str(k) + ' : ' + str(v))
  
//to check if the source code is working//

//type in terminal : python checkip.py or python3 checkip.py//
