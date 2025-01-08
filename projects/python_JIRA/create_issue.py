# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json
from flask import Flask, request

app = Flask(__name__)

# Define a route that handles POST requests
@app.route('/createJira', methods=['POST'])
def createJira():
    
    base_url = "XXXXXXXXXX.atlassian.ne" # Replace with your actual Jira API address
    EMAIL = "XXXXXXXX@gmail.com" # Replace with your actual Jira Email
    url = f"https://{base_url}/rest/api/3/project"
    API_TOKEN = ""  # Replace with your actual Jira API token
    issuetype_title = "BUG"
    project_key = "SCRUM"
    auth = HTTPBasicAuth(EMAIL, API_TOKEN)

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    # Parse the incoming JSON payload
    payload = request.get_json()

    # Check if the comment body is "/jira"
    if 'comment' in payload and isinstance(payload['comment'], dict):
        if payload['comment'].get('body') == "/jira":
            # Get the issue description and title from GitHub payload
            issue_title = payload['issue'].get('title', 'No title provided')
            issue_body = payload['issue'].get('body', 'No description provided')

            # Create the Jira ticket payload dynamically from GitHub issue
            jira_payload = {
                "fields": {
                    "description": {
                        "content": [
                            {
                                "content": [
                                    {
                                        "text": issue_body,  # Use GitHub issue body as Jira description
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
                        "key": project_key  # Replace with your Jira project key
                    },
                    "issuetype": {
                        "name": issuetype_title  # Replace with the correct issue type if necessary
                    },
                    "summary": issue_title,  # Use GitHub issue title as Jira summary
                },
                "update": {}
            }

            try:
                # Make the POST request to Jira to create the ticket
                response = requests.post(
                    url,
                    data=json.dumps(jira_payload),
                    headers=headers,
                    auth=auth
                )

                # Check the response status and return a corresponding message
                if response.status_code == 201:
                    return json.dumps({"message": "Jira ticket created successfully!"}), 201
                else:
                    return json.dumps({"error": "Failed to create Jira ticket", "details": response.text}), 500

            except Exception as e:
                return json.dumps({"error": f"An error occurred: {str(e)}"}), 500
        else:
            return json.dumps({"message": "Comment does not contain '/jira'"}), 400
    else:
        return json.dumps({"error": "Invalid payload, missing 'comment'"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
