# Context - MongoDB Atlas


Docs Home / MongoDB Atlas / Interact with Data / Triggers / Functions Context On this page Get App Metadata ( context.app ) context.app.id context.app.clientAppId context.app.name context.app.projectId context.app.deployment context.app.lastDeployed context.app.hostingUri Call a Function ( context.functions ) context.functions.execute() Check the App Environment ( context.environment ) context.environment.tag context.environment.values Connect to a MongoDB Data Source or Third-Party Service ( context.services ) context.services.get() Get Request Metadata ( context.request ) context.request Get User Data ( context.user ) context.user context.runningAsSystem() Reference a Value ( context.values ) context.values.get(valueName) Send an HTTP Request ( context.http ) context.http.get() context.http.post() context.http.put() context.http.patch() context.http.delete() context.http.head() Atlas Functions have access to a global context object that contains
metadata for the incoming requests and provides access to components and
services in your App. The context object exposes the following interfaces: Property Description context.app Access metadata about the app running the Function. context.environment Access environment values and the
current environment tag. context.functions A client object that calls your app's Functions . context.http A built-in HTTP client. context.request Describes the incoming request that triggered a Function call. context.services Exposes client objects that can access data sources and services. context.user Describes the user that initiated the request. context.values Contains static global values . Get App Metadata ( context.app ) The context.app object contains metadata about the App that
contains the Function. { "id" : string , "clientAppId" : string , "name" : string , "projectId" : string , "deployment" : { "model" : string , "providerRegion" : string , } , "lastDeployed" : string , "hostingUri" : string , } context.app.id The unique internal ID of the App that contains the Function. "60c8e59866b0c33d14ee634a" context.app.clientAppId The unique Client App ID for the App that contains the Function. "myapp-abcde" context.app.name The name of the App that contains the Function. "myapp" context.app.projectId The ID of the Atlas Project that contains the App. "5e1ec444970199272441a214" context.app.deployment An object that describes the App's deployment model and region. { "model" : "LOCAL" , "providerRegion" : "aws-us-east-1" } context.app.lastDeployed The date and time that the App was last deployed, formatted as
an ISODate string. "2022-10-31T12:00:00.000Z" context.app.hostingUri If static hosting is enabled, this value is
the base URL for hosted assets. (Static Hosting is deprecated. Learn more .) "myapp-abcde.mongodbstitch.com" Call a Function ( context.functions ) You can call any Function in your application
through the context.functions interface. context.functions.execute() Calls a specific Function and returns the result. context. functions . execute ( functionName , ... args) Parameter Type Description functionName string The name of the Function. args ... mixed A variadic list of arguments to pass to the Function. Each
Function parameter maps to a separate, comma-separated
argument. // difference: subtracts b from a using the sum function exports = function ( a, b ) { return context. functions . execute ( "sum" , a , - 1 * b) ; } ; Check the App Environment ( context.environment ) You can access information about your App's current environment configuration
and access environment-specific values through the context.environment interface. context.environment.tag The name of the app's current environment as a string. Possible values: "" "development" "testing" "qa" "production" exports = async function ( ) { switch ( context. environment . tag ) { case "" : { return "There is no current environment" } case "development" : { return "The current environment is development" } case "testing" : { return "The current environment is testing" } case "qa" : { return "The current environment is qa" } case "production" : { return "The current environment is production" } } } ; context.environment.values An object where each field maps the name of an environment value to its value in
the current environment. exports = async function ( ) { const baseUrl = context. environment . values . baseUrl } ; Connect to a MongoDB Data Source or Third-Party Service ( context.services ) You can access a client for a linked MongoDB Atlas cluster or
federated data source through the context.services interface. context.services.get() Gets a service client for the specified service or undefined if
no such service exists. context. services . get ( serviceName) Parameter Type Description serviceName string The name of the linked cluster, federated database instance, or service. Linked data sources created by your
app use one of the following default names: Cluster: mongodb-atlas federated database instance: mongodb-datafederation Read and write data in MongoDB Atlas exports = async function ( ) { // Get the cluster's data source client const mdb = context. services . get ( "mongodb-atlas" ) ; // Reference a specific database/collection const db = mdb. db ( "myApp" ) ; const collection = db. collection ( "myCollection" ) ; // Run a MongoDB query return await collection. find ( { name : "Rupert" , age : { $lt : 50 } , }) } ; Get Request Metadata ( context.request ) You can access information about the incoming request with the context.request interface. Tip The context.request interface does not include request body
payloads. context.request An object that contains information about the HTTP request that
caused the Function to execute. { "remoteIPAddress" : < string > , "requestHeaders" : < object > , "webhookUrl" : < string > , "httpMethod" : < string > , "rawQueryString" : < string > , "httpReferrer" : < string > , "httpUserAgent" : < string > , "service" : < string > , "action" : < string > } Field Type Description remoteIPAddress string The IP address of the client that issued the Function request. requestHeaders object An object where each field maps to a type of HTTP Header that was included in the request that caused
the Function to execute. The value of each field is an array of
strings where each string maps to a header of the specified type
that was included in the request. webhookUrl string Optional. In HTTPS endpoint Functions, the route of the endpoint. httpMethod string Optional. In HTTPS endpoint Functions, the HTTP method of the request that called the endpoint. rawQueryString string The query string attached to the
incoming HTTP request. All query parameters appear in the same
order as they were specified. Important! For security reasons, Atlas automatically removes
any query string key/value pair where the key is secret . For
example, if an incoming request has the query string ?secret=hello&someParam=42 then the rawQueryString for
that request is "someParam=42" . httpReferrer string Optional. The URL of the page from which the request was sent. This value is derived from the HTTP Referer header . If the request did not include a Referer header then this is undefined . httpUserAgent string Optional. Characteristic information that identifies the source
of the request, such as the software vendor, operating system, or
application type. This value is derived from the HTTP User-Agent header . If the request did not include a User-Agent header then this is undefined . The following context.request document reflects a Function call
issued from https://myapp.example.com/ by a user browsing with
Chrome 73 on macOS High Sierra: exports = function ( ) { return context. request } HIDE OUTPUT { "remoteIPAddress" : "54.173.82.137" , "httpReferrer" : "https://myapp.example.com/" , "httpUserAgent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36" , "rawQueryString" : "?someParam=foo&anotherParam=42" , "requestHeaders" : { "Content-Type" : [ "application/json" ] , "Cookie" : [ "someCookie=someValue" , "anotherCookie=anotherValue" ] } } Get User Data ( context.user ) You can access information about the application or system user that
called a Function with the context.user interface. context.user The user object of the authenticated user that
called the Function. { "id" : < string > , "type" : < string > , "data" : < document > , "identities" : < array > } Field Type Description id string A string representation of the ObjectId that uniquely identifies the
user. type string The type of the user. The following types are possible: Type Description "normal" The user is an application user logged in
through an authentication provider other than the
API Key provider. "server" The user is a server process logged in with any type of
App Services API Key. "system" The user is the system user that
bypasses all rules. data document A document that contains metadata that describes the
user. This field combines the data for all identities associated with the user, so the exact field names and values
depend on which authentication providers
the user has authenticated with. In system functions, the user.data object is empty. Use context.runningAsSystem() to test if
the function is running as a system user. custom_data document A document from your application's custom user
data collection that
specifies the user's ID. You can use the custom user data
collection to store arbitrary data about your application's
users. If you set the name field, App Services populates the username metadata field with the return value of name .
App Services automatically fetches a new copy of the data
whenever a user refreshes their access token, such as when they
log in. The underlying data is a regular MongoDB document, so you
can use standard CRUD operations through the MongoDB Atlas service to define and modify the user's custom data. Custom user data is limited to 16MB , the maximum size of a
MongoDB document. To avoid hitting this limit, consider
storing small and relatively static user data in each custom
user data document, such as the user's preferred language or
the URL of their avatar image. For data that is large,
unbounded, or frequently updated, consider only storing a
reference to the data in the custom user document or storing
the data with a reference to the user's ID rather than in the
custom user document. identities array A list of authentication provider identities associated with the
user. When a user first logs in with a specific provider, App Services
associates the user with an identity object that contains a
unique identifier and additional metadata about the user from the
provider. For subsequent logins, App Services refreshes the existing
identity data but does not create a new identity. Identity
objects have the following form: { "id" : "<Unique ID>" , "provider_type" : "<Provider Name>" , "data" : { "<Metadata Field>" : <Value> , ... } } Field Name Description id A provider-generated string that uniquely identifies this
identity. provider_type The type of authentication provider associated with this
identity. data Additional metadata from the authentication provider that
describes the user. The exact field names and values will
vary depending on which authentication providers the user
has logged in with. context.runningAsSystem() Evaluates to a boolean that is true if the Function is running as
a system user. exports = function ( ) { const isSystemUser = context. runningAsSystem ( ) if ( isSystemUser) { // Do some work with the system user. } else { // Fail. } } Reference a Value ( context.values ) You can access your app's static values in a
Function with the context.values interface. context.values.get(valueName) Gets the data associated with the provided Value name or undefined if no such value exists. This data is either a plain
text JSON value or a Secret exposed through a
value. Parameter Type Description valueName string The name of the Value. exports = function ( ) { // Get a global value (or `undefined` if no Value has the specified name) const theme = context. values . get ( "theme" ) ; console . log ( theme. colors ) // Output: { red: "#ee1111", blue: "#1111ee" } console . log ( theme. colors . red ) // Output: "#ee1111" } ; Send an HTTP Request ( context.http ) You can send HTTPS requests through a built-in client with the context.http interface. context.http.get() Sends an HTTP GET request to the
specified URL. See http.get() for detailed reference
information, including parameter definitions and return types. exports = async function ( ) { const response = await context. http . get ( { url : "https://www.example.com/users" }) // The response body is a BSON.Binary object. Parse it and return. return EJSON . parse ( response. body . text ( )) ; } ; context.http.post() Sends an HTTP POST request to the
specified URL. See http.post() for detailed reference
information, including parameter definitions and return types. exports = async function ( ) { const response = await context. http . post ( { url : "https://www.example.com/messages" , body : { msg : "This is in the body of a POST request!" } , encodeBodyAsJSON : true }) // The response body is a BSON.Binary object. Parse it and return. return EJSON . parse ( response. body . text ( )) ; } ; context.http.put() Sends an HTTP PUT request to the
specified URL. See http.put() for detailed reference
information, including parameter definitions and return types. exports = async function ( ) { const response = await context. http . put ( { url : "https://www.example.com/messages" , body : { msg : "This is in the body of a PUT request!" } , encodeBodyAsJSON : true }) // The response body is a BSON.Binary object. Parse it and return. return EJSON . parse ( response. body . text ( )) ; } ; context.http.patch() Sends an HTTP PATCH request to the
specified URL. See http.patch() for detailed reference
information, including parameter definitions and return types. exports = async function ( ) { const response = await context. http . patch ( { url : "https://www.example.com/diff.txt" , body : { msg : "This is in the body of a PATCH request!" } , encodeBodyAsJSON : true }) // The response body is a BSON.Binary object. Parse it and return. return EJSON . parse ( response. body . text ( )) ; } ; context.http.delete() Sends an HTTP DELETE request to the
specified URL. See http.delete() for detailed reference
information, including parameter definitions and return types. exports = async function ( ) { const response = await context. http . delete ( { url : "https://www.example.com/user/8675309" }) } ; context.http.head() Sends an HTTP HEAD request to the
specified URL. See http.head() for detailed reference
information, including parameter definitions and return types. exports = async function ( ) { const response = await context. http . head ( { url : "https://www.example.com/users" }) // The response body is a BSON.Binary object. Parse it and return. EJSON . parse ( response. body . text ( )) ; } ; Back Functions Next Global Modules
