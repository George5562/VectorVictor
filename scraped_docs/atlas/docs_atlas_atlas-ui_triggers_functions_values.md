# Define and Access Values - MongoDB Atlas


Docs Home / MongoDB Atlas / Interact with Data / Triggers / Functions Define and Access Values On this page Define a Value Access a Value A Value is a named reference to a piece of static data stored by Atlas that you can access in Atlas Functions . Values provide an
alternative to hardcoding configuration constants directly into your Functions. In other words, Values allow you to separate deployment-specific configuration
data from the business logic of your app. Values can resolve to two types of data: Plain text : Resolves to a regular JSON object, array, or
string Value that you define. Secret : Resolves to a Secret Value that you define. Define a Value You can define a new Value from the UI or using the App Services CLI. Atlas UI App Services CLI 1 Navigate to the Values Page Navigate to the Triggers page: If it's not already displayed, select the
organization that contains your project from the Organizations menu in the navigation bar. If it's not already displayed, select your project
from the Projects menu in the navigation bar. In the sidebar, click Triggers under
the Services heading. The Triggers page displays. Click the Linked App Service: Triggers link. In the sidebar, click Values under the Build heading. Click Create a Value . 2 Name the Value Enter a unique Value Name . This name is how you refer
to the Value in Functions. Note Value Name Restrictions Value names cannot exceed 64 characters and may only contain
ASCII letters, numbers, underscores, and hyphens. The first
character must be a letter or number. 3 Define the Value Select the Value type. Define either a plain text value or link to a Secret value: To define a plain text value, Custom Content and
enter the plain text Value in the input box. To link to an existing Secret's value, select Link to
Secret and select the Secret from the dropdown. To link to a new Secret value, select Link to Secret ,
then enter the new Secret's name and the new Secret's value in
the input box that appears. For more information on creating a Secret, see Create a Secret . 4 Save the Value After you have named and defined the new Value, click Save . Once saved, you can immediately access the Value in your Functions. 1 Authenticate a MongoDB Atlas User Use your MongoDB Atlas Administration API Key to
log in to the App Services CLI: appservices login --api-key="<API KEY>" --private-api-key="<PRIVATE KEY>" 2 Pull Your App's Latest Configuration Files Run the following command to get a local copy of your configuration files: appservices pull --remote=<App ID> By default, the command pulls files into the current working directory. You can
specify a directory path with the optional --local flag. 3 Add the Value Configuration Add a JSON configuration file for the new Value to the values subdirectory of your local application: touch values/<ValueName>.json Each Value is defined in its own JSON file. For example, a Value
named myValue would be defined in the file /values/myValue.json . The configuration file should have the following general form: values/<ValueName>.json { "name" : "<Value Name>" , "from_secret" : <boolean> , "value" : <Stored JSON Value|Secret Name> } Field Description name A unique name for the Value. This name is how you refer to
the Value in Functions and rules. from_secret Default: false . If true , the Value exposes a Secret instead of a plain-text JSON Value. value The stored data the Value exposes when referenced: If from_secret is false , value can be a
standard JSON string, array, or object. If from_secret is true , value is a string
that contains the name of the Secret the Value exposes. 4 Deploy Your Changes: Run the following command to deploy your changes: appservices push Access a Value You can access a Value's stored data from an Atlas Function
using the context.values module. context. values . get ( "<Value Name>" ) For example, the following Function returns true when the active
user's id is included in the plain text array Value adminUsers : Example Function that uses a Value exports = function ( ) { const adminUsers = context. values . get ( "adminUsers" ) ; const isAdminUser = adminUsers. indexOf ( context. user . id ) > 0 ; return isAdminUser ; } Back MongoDB API Reference Next Logs
