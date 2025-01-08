# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://teambeta2001.atlassian.net/rest/api/3/issue"

API_toke = "ATATT3xFfGF0x1LEGC_ZEDtfMqzM9rjvVUjvX-jbRjJqPhauXKhuEY_a-aQm6avI-XmvIOvtVFOy1L7Dl_ftXqHYC2hGgLHSqEl1BRawXhAVWGkI9zb4RRNEge97_Svbc6rpU-j66uPN2H7f9Z8KxNHN_q00NNZb2amkbVvPTa7ey8PjKsLqCJE=0DDDAE27"

auth = HTTPBasicAuth("teambeta2001@gmail.com", API_toke)

headers = {
  "Accept": "application/json",
  "Content-Type": "application/json"
}

payload = json.dumps( {
  "fields": {
    "description": {
      "content": [
        {
          "content": [
            {
              "text": "My jira ticket summary_3",
              "type": "text"
            }
          ],
          "type": "paragraph"
        }
      ],
      "type": "doc",
      "version": 1
    },
    "project": {
      "key": "SCRUM"
    },
    "issuetype": {
      "name": "Bug"
    },
    "summary": "today JIRA Ticket created_3",
  },
  "update": {}
} )

response = requests.request(
   "POST",
   url,
   data=payload,
   headers=headers,
   auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))