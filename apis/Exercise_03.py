'''
Write the necessary code to make a POST request to:

    http://demo.codingnomads.co:8080/tasks_api/users

and create a user with your information.

Make a GET request to confirm that your user information has been saved.

'''

import requests

base_url = "http://demo.codingnomads.co:8080/tasks_api/users"

body = {
    "first_name": "James",
    "last_name": "Bond",
    "email": "james.bond@007.uk"
}

response = requests.post(base_url, json=body)

print(f"Status code of POST: {response.status_code}")

response = requests.get(base_url)
print(f"Status code of GET: {response.status_code}")

