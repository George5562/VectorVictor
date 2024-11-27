# Define and Manage Secrets - MongoDB Atlas


Docs Home / MongoDB Atlas / Interact with Data / Triggers / Functions Define and Manage Secrets On this page Define a Secret View Secrets Update a Secret Use a Secret Delete a Secret A Secret is a private value that is stored on the Atlas backend and hidden from users. Secrets are useful for storing sensitive
information such as an API key or an internal identifier. You cannot directly read the value of a Secret after
defining it. Instead, you link the Secret to another Value , then
access the value from a Trigger Function . Define a Secret You can define a new Secret from the UI or using the App Services CLI. Atlas UI App Services CLI 1 Navigate to the Values Page Navigate to the Triggers page: If it's not already displayed, select the
organization that contains your project from the Organizations menu in the navigation bar. If it's not already displayed, select your project
from the Projects menu in the navigation bar. In the sidebar, click Triggers under
the Services heading. The Triggers page displays. Click the Linked App Service: Triggers link. In the sidebar, click Values under the Build heading. Click Create a Value . 2 Name the Secret Value Enter a name for the Secret. This name is how you refer to
the Secret in Functions and must be unique within the project. Note Secret Name Restrictions Value names cannot exceed 64 characters and may only contain
ASCII letters, numbers, underscores, and hyphens. The first
character must be a letter or number. 3 Define the Secret Value Select Secret type. Enter the new Secret's value in the Add Content input box. Secret values may not exceed 500 characters. Warning You cannot directly read the value of a Secret after saving it. 4 Save and Deploy After you've defined the Secret, click Save . If
your application deployment drafts enabled, click Review & Deploy to deploy the changes. 1 Authenticate a MongoDB Atlas User Use your MongoDB Atlas Administration API Key to
log in to the App Services CLI: appservices login --api-key="<API KEY>" --private-api-key="<PRIVATE KEY>" 2 Pull Your App's Latest Configuration Files Run the following command to get a local copy of your configuration files: appservices pull --remote=<App ID> By default, the command pulls files into the current working directory. You can
specify a directory path with the optional --local flag. 3 Create a New Secret Run the following command to define a new Secret: appservices secrets create --app=<Your App ID> \ --name="<Secret Name>" \ --value="<Secret Value>" 4 Deploy Your Changes Run the following command to deploy your changes: appservices push View Secrets You can view a list of all Secrets in an app from the UI or using the App Services CLI. Atlas UI App Services CLI From the Triggers page, click the Linked App
Service: Triggers link. In the sidebar, click Values under the Build heading. The table lists all Values, including Secrets, and indicates each
Value's type in its row. To list the names and IDs of all Secrets, run the following command: appservices secrets list --app=<Your App ID> Update a Secret You can update a Secret from the UI or using the App Services CLI. Atlas UI App Services CLI To update a Secret from the Atlas UI: From the Triggers page, click the Linked App
Service: Triggers link. In the sidebar, click Values under the Build heading. Find the Value that you want to update in the table, open its Actions menu, and select Edit Secret . You can change both the name and value for the Secret. Click Save and then, if needed, deploy your changes. To update the value of a Secret using the App Services CLI, run the
following command: appservices secrets update --app=<Your App ID> \ --secret="<Secret ID or Name>" \ --name="<Updated Secret Name>" \ --value="<Updated Value>" Use a Secret You cannot directly read the value of a Secret after defining it. To use a Secret in a Triggers Function: Create a new Value that links to the Secret. Use the context.values module to access the Secret's value in your Function. Delete a Secret You can delete a Secret from the UI or using the App Services CLI. Atlas UI App Services CLI To delete a Secret from the Atlas UI: From the Triggers page, click the Linked App
Service: Triggers link. In the sidebar, click Values under the Build heading. Find the Value that you want to delete in the table, open its Actions menu, and select Delete Secret . Confirm that you want to delete the Secret. To delete a Secret using the App Services CLI, run the following command: appservices secrets delete --app=<Your App ID> --secret=<Secret ID> Tip You can delete multiple Secrets with a single command by specifying
their name or id values as a comma-separated list. appservices secrets delete --app=<Your App ID> \ --secret=some-api-key,609af850b78eca4a8db4303f,another-key Back Aggregate Next MongoDB API Reference