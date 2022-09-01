import requests

# Run main.py file 1st before running this file

url = "http://127.0.0.1:5000/search?loc=Peckham"
random_cafes_url = "http://127.0.0.1:5000/random"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)
random_cafes_response = requests.request("GET", random_cafes_url, headers=headers, data=payload)

# Getting Peckham cafe
print(response.text)

# Getting random cafe
print(random_cafes_response.text)
