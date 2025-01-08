# Python and Jira Integration Application

This application integrates Python with Jira. When a comment containing "/jira" is added to an issue, it will automatically create a Jira ticket.

## Steps:

### Step 1: Create a Free Jira Account
If you don't have a Jira account yet, start by creating a free Jira account.

### Step 2: Set up an EC2 Instance and Install Dependencies

- **Create a Basic EC2 Instance**  
  Set up a basic EC2 instance. Ensure that port `5000` is open in the security group to allow access, as the Flask application will run on this port.

- **Install Python and Flask**  
  Run the following commands to install Python and Flask:

    ```sh
    sudo apt update
    sudo apt install python3
    sudo apt install python3-pip
    pip install Flask
    ```

  If you encounter any issues during Flask installation, you can try using:

    ```sh
    sudo apt install python3-flask
    ```

- **Configure the Python Script**  
  Before running the script, make sure to configure the following values in the Python file:
    - `base_url`
    - `EMAIL`
    - `API_TOKEN`
    - `issuetype_title`
    - `project_key`

- **Run the Python Script**  
  Navigate to the folder containing the Python script and run it:

    ```sh
    python3 create_issue.py
    ```

  Once the script runs, you should see output like this:

    ```
    Serving Flask app 'createJIRA'
    Debug mode: off
    WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
    Running on all addresses (0.0.0.0)
    Running on http://127.0.0.1:5000
    ```

### Step 3: Configure the Jira Webhook

- Navigate to **Settings > Webhooks** in your Jira repository.
- Click **Create Webhook**.

#### Webhook Configuration:

- **Payload URL**:  
  Use the public DNS of your EC2 instance. The URL should look like this:  
  `http://<your_DNS_name>:5000/createJira`

- **Content Type**:  
  Select `application/json`.

- **Events**:  
  Check the box for **Issue Comment** so that the webhook will be triggered when an issue comment is made.

### Step 4: Add a Comment to Create a Jira Ticket

- Go to an issue in Jira.
- Add the comment `/jira` to the issue.
- The webhook will automatically trigger and create a Jira ticket.

---

Congratulations! You have successfully integrated Python with Jira to create Jira tickets by simply adding a `/jira` comment to an issue.
