# Authentication Triggers - MongoDB Atlas


Docs Home / MongoDB Atlas / Interact with Data / Triggers Authentication Triggers On this page Configuration Authentication Events Example As of September 2024, the Atlas Device SDKs are deprecated and will reach
end of life in September 2025. This will affect authentication Triggers,
because they will no longer have authentication events to react to. An authentication Trigger fires when a user interacts with an authentication provider . You can
use authentication Triggers to implement advanced user management. Some uses include: Storing new user data in your linked cluster. Maintaining data integrity upon user deletion. Calling a service with a user's information when they log in. Configuration Authentication Triggers have the following configuration options: Field Description Trigger Type The type of the Trigger. For authentication Triggers,
set this value to AUTHENTICATION . Trigger Name The name of the Trigger. Linked Function The name of the Function that the Trigger
executes when it fires. This object is the only argument the Trigger
passes to the Function after an authentication event object causes the Trigger to fire. Operation Type The authentication operation type that causes the Trigger to
fire. Providers A list of one or more authentication provider types. The Trigger only listens for
authentication events produced by these providers. Authentication Events Authentication events represent user interactions with an authentication
provider. Each event corresponds to a single user action with one of the
following operation types: Operation Type Description LOGIN Represents a single instance of a user logging in. CREATE Represents the creation of a new user. DELETE Represents the deletion of a user. If the deleted user was linked to
multiple providers, the DELETE event for that user includes all
linked providers. Authentication event objects have the following form: { "operationType" : <string> , "providers" : <array of strings> , "user" : <user object> , "time" : <ISODate> } Field Description operationType The operation type of the authentication event. providers The authentication providers that emitted the event. One of the following names represents each
authentication provider: "anon-user" "local-userpass" "api-key" "custom-token" "custom-function" "oauth2-facebook" "oauth2-google" "oauth2-apple" user The user object of the user that interacted with the authentication
provider. time The time at which the event occurred. Example An online store wants to store custom metadata for each of its customers
in Atlas . Each customer needs a document in the store.customers collection.
Then, the store can record and query metadata in the customer's document. The collection must represent each customer. To guarantee this, the store
creates an authentication Trigger. This Trigger listens for newly created users
in the email/password authentication provider, then it passes the authentication event object to its linked
Function createNewUserDocument . The createNewUserDocument Function creates a new document that describes the
user and their activity. The Function then inserts the document into the store.customers collection. createNewUserDocument Function exports = async function ( authEvent ) { const mongodb = context. services . get ( "mongodb-atlas" ) ; const customers = mongodb. db ( "store" ). collection ( "customers" ) ; const { user , time } = authEvent ; const isLinkedUser = user. identities . length > 1 ; if ( isLinkedUser) { const { identities } = user ; return users. updateOne ( { id : user. id } , { $set : { identities } } ) } else { return users. insertOne ( { _id : user. id , ... user }) . catch ( console . error ) } await customers. insertOne ( newUser) ; } Tip See also: Triggers examples on Github. Back Scheduled Triggers Next Disable a Trigger
