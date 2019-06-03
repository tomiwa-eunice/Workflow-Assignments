# WPS Execute Operation

import requests, os

payload = open(os.path.dirname(os.path.abspath(__file__)) +"\\nearest_poi.xml").read()


wpsServerUrl = "https://gisedu.itc.utwente.nl/student/s6040446/gpw/Assignments/assignment1/wps.py?"

response = requests.post(wpsServerUrl, data=payload)
print("Content-type: application/json")
print()
print(response.text)