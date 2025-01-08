# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

base_url = "teambeta2001.atlassian.net"
email = "teambeta2001@gmail.com"
API_toke = "ATATT3xFfGF0x1LEGC_ZEDtfMqzM9rjvVUjvX-jbRjJqPhauXKhuEY_a-aQm6avI-XmvIOvtVFOy1L7Dl_ftXqHYC2hGgLHSqEl1BRawXhAVWGkI9zb4RRNEge97_Svbc6rpU-j66uPN2H7f9Z8KxNHN_q00NNZb2amkbVvPTa7ey8PjKsLqCJE=0DDDAE27"

url = f"https://{base_url}/rest/api/3/project"

auth = HTTPBasicAuth(email, API_toke)
headers = {
  "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)

output = json.loads(response.text)
for item in output:
  name = item["name"]
  print(name)

#print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))