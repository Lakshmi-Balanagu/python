# Python and Jira Integration Application

This application integrates Python with Jira. Whenever a comment containing "/jira" is added to an issue, it automatically creates a Jira ticket.

## Steps:

### Step 1: Set up EC2 Instance and Install Dependencies

- **Create a basic EC2 instance.**  
  Make sure to allow traffic on port `5000` in the security group, as the Flask application runs on this port.

- **Install Python and Flask**  
  Run the following commands to install Python and Flask:

    ```sh
    sudo apt update
    sudo apt install python3
    sudo apt install python3-pip
    pip install Flask
    ```

    If you encounter an error while installing Flask, try installing it using:

    ```sh
    sudo apt install python3-flask
    ```

- **Run the Python script**  
  Once Flask is installed, navigate to the folder containing the Python file and run:

    ```sh
    python3 create_issue.py
    ```

  After running the script, you should see output similar to:

    ```
    > Serving Flask app 'createJIRA'
    Debug mode: off
    WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
    Running on all addresses (0.0.0.0)
    > Running on http://127.0.0.1:5000
    ```

### Step 2: Configure Jira Webhook

- Go to your Jira repository and navigate to **Settings > Webhooks**.
- Click on **Create Webhook**.

#### Configuration Details:

- **Payload URL**:  
  Use the public DNS of your newly created EC2 instance. The URL should look like:  
  `http://<your_DNS_name>:5000/createJira`

- **Content type**:  
  Select `application/json`.

- **Events**:  
  Check the box for **Issue Comment** to trigger the webhook on issue comments.

### Step 3: Add Comment to Create Jira Ticket

- Go to an issue in Jira.
- Add the comment `/jira` to the issue.
- The webhook will trigger and automatically create a Jira ticket.

---

You have now successfully integrated Python and Jira to create Jira tickets by commenting `/jira` on issues!
