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
# Message variables
summary_msg = "python program issue summary_1"
description_msg = "Order entry fails when selecting supplier."
issuetype_id = "10006"  # Correct issue type ID
project_key = "SCRUM"  # Replace with your actual project key


headers = {"Accept": "application/json", "Content-Type": "application/json"}

payload = json.dumps(
    {
        "fields": {
            "description": {
                "content": [
                    {
                        "content": [{"text": summary_msg, "type": "text"}],
                        "type": "paragraph",
                    }
                ],
                "type": "doc",
                "version": 1,
            },
            "issuetype": {"id": issuetype_id},
            "project": {"key": project_key},
            "summary": "Main order flow broken",
        },
        "update": {},
    }
)

response = requests.request("POST", url, data=payload, headers=headers, auth=auth)

print(
    json.dumps(
        json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")
    )
)