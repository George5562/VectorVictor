# Database Triggers - MongoDB Atlas


Docs Home / MongoDB Atlas / Interact with Data / Triggers Database Triggers On this page Create a Database Trigger Configuration Change Event Types Database Trigger Example Suspended Triggers Trigger Time Reporting Performance Optimization Database Triggers allow you to execute server-side logic whenever a database
change occurs on a linked MongoDB Atlas cluster. You can configure Triggers on
individual collections, entire databases, and on an entire cluster. Unlike SQL data triggers, which run on the database server, Atlas database
Triggers run on a serverless compute layer that scales independently of the
database server. Triggers automatically call Atlas Functions and can forward events to external handlers
through AWS EventBridge. Use database Triggers to implement event-driven data interactions. For
example, you can automatically update information in one document when a
related document changes or send a request to an external service
whenever a new document is inserted. Database Triggers use MongoDB change streams to watch for real-time changes in a collection. A change stream is a
series of database events that each
describe an operation on a document in the collection. Your app opens a
single change stream for each collection with at least one enabled
Trigger. If multiple Triggers are enabled for a collection they all
share the same change stream. Important Change Stream Limitations There are limits on the total number of change streams you can open
on a cluster, depending on the cluster's size. For more information, see change stream limitations . Additionally, you cannot define a database Trigger on a serverless instance or federated database instance because they do not support change streams. You control which operations cause a Trigger to fire as well as what
happens when it does. For example, you can run a Function whenever a
specific field of a document is updated. The Function can access the
entire change event, so you always know what changed. You can also pass
the change event to AWS EventBridge to handle
the event outside of Atlas . Triggers support $match expressions to filter change events and $project expressions to limit the data included in each event. Warning In deployment and database level Triggers, it is possible to configure Triggers
in a way that causes other Triggers to fire, resulting in recursion.
Examples include a database-level Trigger writing to a collection within the
same database, or a cluster-level logger or log forwarder writing logs to
another database in the same cluster. Create a Database Trigger You can create a database Trigger from the Atlas UI or with the
App Services CLI. Atlas UI App Services CLI Navigate to the Triggers Page If it's not already displayed, select the
organization that contains your project from the Organizations menu in the navigation bar. If it's not already displayed, select your project
from the Projects menu in the navigation bar. In the sidebar, click Triggers under
the Services heading. The Triggers page displays. Click Add Trigger to open the Trigger configuration page. Select the Database Trigger type. Configure the Trigger, then click Save . Authenticate a MongoDB Atlas user: Use your MongoDB Atlas Administration API Key to
log in to the App Services CLI: appservices login --api-key="<API KEY>" --private-api-key="<PRIVATE KEY>" Pull your App's latest configuration files: Run the following command to get a local copy of your configuration files: appservices pull --remote=<App ID> By default, the command pulls files into the current working directory. You can
specify a directory path with the optional --local flag. Add a database Trigger configuration file to the triggers subdirectory in your
local app files. Deploy your changes: Run the following command to deploy your changes: appservices push Note Atlas does not enforce specific filenames for Trigger
configuration files. However, once imported, Atlas will rename
each configuration file to match the name of the Trigger it defines. Configuration Database Triggers have the following configuration options: Trigger Details Within the Trigger Details section, you can select the scope that you want the Trigger to Watch Against , based on the level of granularity you want. Your
options are: Collection , when a change occurs on a specified collection Database , when a change occurs on any collection in a
specified database Deployment , when deployment changes occur on a specified
cluster. If you select the Deployment source type, the following
databases are not watched for changes: The admin databases admin , local , and config The sync databases __realm_sync and __realm_sync_<app_id> Important The deployment-level source type is only available on dedicated tiers. Depending on which source type you are using, the additional options differ. The
following table describes these options. Source Type Options Collection Cluster Name . The name of the MongoDB cluster that the
Trigger is associated with. Database Name . The MongoDB database that contains the watched
collection. Collection Name . The MongoDB collection to watch. Optional.
If you leave this option blank, the Source Type changes to "Database." Operation Type . The operation types that cause the Trigger to fire.
Select the operation types you want the Trigger to respond to. Options
include: Insert Update Replace Delete Note: Update operations executed from MongoDB Compass or the MongoDB Atlas Data Explorer fully replace the previous document. As a result,
update operations from these clients generate Replace change events rather than Update events. Full Document . If enabled, Update change events include
the latest majority-committed version of the modified document after the change was applied in
the fullDocument field. Note: Regardless of this setting, Insert and Replace events always
include the fullDocument field. Delete events never include
the fullDocument field. Document Preimage . When enabled, change events include a
copy of the modified document from immediately before the change was
applied in the fullDocumentBeforeChange field. This has performance considerations . All change events
except for Insert events include the document preimage. Database Cluster Name . The name of the MongoDB cluster that the
Trigger is associated with. Database Name . The MongoDB database to watch. Optional.
If you leave this option blank, the source type changes to Deployment unless you are on a shared tier, in which case Atlas will not
let you save the Trigger. Operation Type . The operation types that cause the Trigger to fire.
Select the operation types you want the  Trigger to respond to.
Options include: Create Collection Modify Collection Rename Collection Drop Collection Shard Collection Reshard Collection Refine Collection Shard Key Note: Update operations executed from MongoDB Compass or the MongoDB Atlas Data Explorer fully replace the previous document. As a result,
update operations from these clients will generate Replace change events rather than Update events. Full Document . If enabled, Update change events include
the latest majority-committed version of the modified document after the change was applied in
the fullDocument field. Note: Regardless of this setting, Insert and Replace events always
include the fullDocument field. Delete events never include
the fullDocument field. Document Preimage . When enabled, change events include a
copy of the modified document from immediately before the change was
applied in the fullDocumentBeforeChange field. This has performance considerations . All change events
except for Insert events include the document preimage. Disabled
for Database and Deployment sources to limit unnecessary watches on the
cluster for a new collection being created. Deployment Cluster Name . The name of the MongoDB cluster that the
Trigger is associated with. Operation Type . The operation types that occur in the cluster that cause
the Trigger to fire. Select the operation types you want the Trigger
to respond to. Options include: Drop Database Full Document . If enabled, Update change events include
the latest majority-committed version of the modified document after the change was applied in
the fullDocument field. Note: Regardless of this setting, Insert and Replace events always
include the fullDocument field. Delete events never include
the fullDocument field. Document Preimage . When enabled, change events include a
copy of the modified document from immediately before the change was
applied in the fullDocumentBeforeChange field. This has performance considerations . All change events
except for Insert events include the document preimage. Disabled
for Database and Deployment sources to limit unnecessary watches on the
cluster for a new collection being created. Tip Preimages and Performance Optimization Preimages require additional storage overhead that may affect
performance. If you're not using preimages on a collection,
you should disable preimages. To learn more, see Disable
Collection-Level Preimages . Document preimages are supported on non-sharded Atlas clusters running
MongoDB 4.4+, and on sharded Atlas clusters running MongoDB 5.3 and later.
You can upgrade a non-sharded cluster (with preimages) to a
sharded cluster, as long as the cluster is running 5.3 or later. Trigger Configurations Field Description Auto-Resume If enabled, when this Trigger's resume token
can't be found in the cluster's oplog, the Trigger automatically resumes
processing events at the next relevant change stream event.
All change stream events from when the Trigger was suspended until the Trigger
resumes execution do not have the Trigger fire for them. Event Ordering If enabled, Trigger events are processed in the order in which they occur.
If disabled, events can be processed in parallel, which is faster when
many events occur at the same time. If event ordering is enabled, multiple executions of this Trigger will occur
sequentially based on the timestamps of the change events. If event ordering is
disabled, multiple executions of this Trigger will occur independently. Tip: To improve performance for Triggers that respond to bulk database
operations, disable event
ordering. Skip Events On Re-Enable Disabled by default. If enabled, any change events that occurred while this
Trigger was disabled will not be processed. Event Type Within the Event Type section, you choose what action is taken when
the Trigger fires. You can choose to run a Function or use AWS EventBridge . Advanced Within the Advanced section, the following optional configuration
options are available: Field Description Project Expression A $project expression that selects a subset of fields from each event in the change
stream. You can use this to optimize the trigger's execution . The expression is an object that maps the name of fields in the change
event to either a 0 , which excludes the field, or a 1 , which
includes it. An expression can have values of either 0 or 1 but
not both together. This splits projections into two categories,
inclusive and exclusive: An inclusive project expression specifies fields to include in each
change event document. The expression is an object that maps the name
of fields to include to a 1 . If you don't include a field, it is
not included in the projected change event. The following projection includes only the _id and fullDocument fields: { _id : 1 , fullDocument : 1 } An exclusive project expression specifies fields to exclude from
each change event document. The expression is an object that maps the
name of fields to include to a 0 . If you don't exclude a field, it
is included in the projected change event. The following projection excludes the _id and fullDocument fields: { _id : 0 , fullDocument : 0 } You cannot exclude the operation_type field with a projection.
This ensures that the trigger can always check if it should run for
a given event's operation type. Match Expression A $match expression document
that Atlas uses to filter which change events cause the Trigger to
fire. The Trigger evaluates all change event objects that it receives against
this match expression and only executes if the expression evaluates to true for a given change event. MongoDB performs a full equality match for embedded documents in a match
expression. If you want to match a specific field in an embedded document,
refer to the field directly using dot-notation . For more information, see Query on Embedded Documents in
the MongoDB server manual. To optimize performance, limit the number of fields that the Trigger processes
by using a $match expression. Learn more. Maximum Throughput If the linked data source is a dedicated server (M10+ Tier),
you can increase the maximum throughput beyond the default 10,000 concurrent processes. Important: To enable maximum throughput, you must disable Event Ordering. Before increasing the maximum throughput, consider whether one or more of
your Triggers are calling a rate-limited external API. Increasing the
Trigger rate might result in exceeding those limits. Increasing the throughput may also add a larger workload, affecting
overall cluster performance. Change Event Types Database change events represent individual changes in a specific
collection of your linked MongoDB Atlas cluster. Every database event has the same operation type and structure as the change event object that was
emitted by the underlying change stream. Change events have the
following operation types: Operation Type Description Insert Document (All Trigger types) Represents a new document added to the collection. Update Document (All Trigger types) Represents a change to an existing document in the collection. Delete Document (All Trigger types) Represents a document deleted from the collection. Replace Document (All Trigger types) Represents a new document that replaced a document in the collection. Create Collection (Database and Deployment Trigger types only) Represents the creation of a new collection. Modify Collection (Database and Deployment Trigger types only) Represents the modification collection. Rename Collection (Database and Deployment Trigger types only) Represents collection being renamed. Drop Collection (Database and Deployment Trigger types only) Represents a collection being dropped. Shard Collection (Database and Deployment Trigger types only) Represents a collection changing from unsharded to sharded. Reshard Collection (Database and Deployment Trigger types only) Represents a change to a collection's sharding. Refine Collection Shard Key (Database and Deployment Trigger types only) Represents a change in the shard key of a collection. Create Indexes (Database and Deployment Trigger types only) Represents the creation of a new index. Drop Indexes (Database and Deployment Trigger types only) Represents an index being dropped. Drop Database (Deployment Trigger type only) Represents a database being dropped. Database change event objects have the following general form: { _id : <ObjectId> , "operationType" : <string> , "fullDocument" : <document> , "fullDocumentBeforeChange" : <document> , "ns" : { "db" : <string> , "coll" : <string> } , "documentKey" : { "_id" : <ObjectId> } , "updateDescription" : <document> , "clusterTime" : <Timestamp> } Database Trigger Example An online store wants to notify its customers whenever one of their
orders changes location. They record each order in the store.orders collection as a document that resembles the following: { _id : ObjectId( "59cf1860a95168b8f685e378" ) , customerId : ObjectId( "59cf17e1a95168b8f685e377" ) , orderDate : ISODate( "2018-06-26T16:20:42.313Z" ) , shipDate : ISODate( "2018-06-27T08:20:23.311Z" ) , orderContents : [ { qty : 1 , name : "Earl Grey Tea Bags - 100ct" , price : NumberDecimal( "10.99" ) } ] , shippingLocation : [ { location : "Memphis" , time : ISODate( "2018-06-27T18:22:33.243Z" ) } , ] } To automate this process, the store creates a database Trigger that
listens for Update change events in the store.orders collection.
When the Trigger observes an Update event, it passes the change event object to its associated Function, textShippingUpdate . The Function checks the change event for any
changes to the shippingLocation field and, if it was updated, sends
a text message to the customer with the new location of the order. Atlas UI App Services CLI Trigger Configuration { "type" : "DATABASE" , "name" : "shippingLocationUpdater" , "function_name" : "textShippingUpdate" , "config" : { "service_name" : "mongodb-atlas" , "database" : "store" , "collection" : "orders" , "operation_types" : [ "UPDATE" ] , "unordered" : false , "full_document" : true , "match" : { } } , "disabled" : false } textShippingUpdate exports = async function ( changeEvent ) { // Destructure out fields from the change stream event object const { updateDescription , fullDocument } = changeEvent ; // Check if the shippingLocation field was updated const updatedFields = Object . keys ( updateDescription. updatedFields ) ; const isNewLocation = updatedFields. some ( field => field. match ( /shippingLocation/ ) ) ; // If the location changed, text the customer the updated location. if ( isNewLocation) { const { customerId , shippingLocation } = fullDocument ; const mongodb = context. services . get ( "mongodb-atlas" ) ; const customers = mongodb. db ( "store" ). collection ( "customers" ) ; const { location } = shippingLocation. pop ( ) ; const customer = await customers. findOne ( { _id : customerId }) ; const twilio = require ( 'twilio' ) ( // Your Account SID and Auth Token from the Twilio console: context. values . get ( "TwilioAccountSID" ) , context. values . get ( "TwilioAuthToken" ) , ) ; await twilio. messages . create ( { To : customer. phoneNumber , From : context. values . get ( "ourPhoneNumber" ) , Body : `Your order has moved! The new location is ${location} .` }) } } ; Suspended Triggers Database Triggers may enter a suspended state in response to an event
that prevents the Trigger's change stream from continuing. Events that
can suspend a Trigger include: invalidate events such as dropDatabase , renameCollection , or those caused by
a network disruption. the resume token required to resume the change stream is no longer in the
cluster oplog . The App logs
refer to this as a ChangeStreamHistoryLost error. In the event of a suspended or failed Trigger, Atlas sends the
project owner an email alerting them of the issue. Automatically Resume a Suspended Trigger You can configure a Trigger to automatically resume if the Trigger was suspended
because the resume token is no longer in the oplog.
The Trigger does not process any missed change stream events between
when the resume token is lost and when the resume process completes. When creating or updating a Database Trigger in the Atlas UI: Navigate to the configuration page of the Trigger you want to automatically
resume if suspended. In the Advanced (Optional) section, select Auto-Resume
Triggers . Save and deploy the changes. Manually Resume a Suspended Trigger When you manually resume a suspended Trigger, your App attempts to resume the Trigger
at the next change stream event after the change stream stopped.
If the resume token is no longer in the cluster oplog, the Trigger
must be started without a resume token. This means the Trigger begins
listening to new events but does not process any missed past events. You can adjust the oplog size to keep the resume token for more time after
a suspension by scaling your |service| cluster .
Maintain an oplog size a few times greater than
your cluster's peak oplog throughput (GB/hour) to reduce the risk of a
suspended Trigger's resume token dropping off the oplog
before the Trigger executes.
View your cluster's oplog throughput in the Oplog GB/Hour graph in the |service| cluster metrics . You can restart a suspended Trigger from the Atlas UI or with the App Services CLI. Atlas UI App Services CLI 1 In Atlas , go to the Triggers page for your project. If it's not already displayed, select the
organization that contains your project from the Organizations menu in the navigation bar. If it's not already displayed, select your project
from the Projects menu in the navigation bar. In the sidebar, click Triggers under
the Services heading. The Triggers page displays. 2 Find the Suspended Trigger On the Triggers page, find the Trigger that you want to
disable in the list of Triggers. Atlas marks suspended Triggers
with a Status of Suspended . 3 Restart the Trigger Click Restart in the Trigger's Actions column.
You can choose to restart the Trigger with a change stream resume token or
open a new change stream. Indicate whether or not to use a resume token, then click Resume Database Trigger . Note: If you use a resume token , Atlas attempts to resume the Trigger's underlying change
stream at the event immediately following the last
change event it processed. If successful, the Trigger
processes any events that occurred while it was
suspended. If you do not use a resume token, the
Trigger begins listening for new events but will not
fire for any events that occurred while it was
suspended. 1 Authenticate a MongoDB Atlas User Use your MongoDB Atlas Administration API Key to
log in to the App Services CLI: appservices login --api-key="<API KEY>" --private-api-key="<PRIVATE KEY>" 2 Pull Your App's Latest Configuration Files Run the following command to get a local copy of your configuration files: appservices pull --remote=<App ID> By default, the command pulls files into the current working directory. You can
specify a directory path with the optional --local flag. 3 Verify the Trigger Configuration File Exists If you exported a new copy of your application, it should already
include an up-to-date configuration file for the suspended Trigger.
You can confirm that the configuration file exists by looking
in the /triggers directory for a Trigger configuration file with the same name as the Trigger. 4 Redeploy the Trigger After you have verified that the Trigger configuration file exists,
push the configuration back to your app. App Services
automatically attempts to resume any suspended Triggers included
in the deployment. appservices push Trigger Time Reporting The list of Triggers in the Atlas UI shows three timestamps: Last Modified This is the time the Trigger was created or most recently changed. Latest Heartbeat Atlas keeps track of the last time a Trigger was run. If the Trigger
is not sending any events, the server sends a heartbeat to ensure the Trigger's
resume token stays fresh. Whichever event is most recent is shown as the Latest Heartbeat . Last Cluster Time Processed Atlas also keeps track of the Last Cluster Time Processed ,
which is the last time the change stream backing a Trigger emitted an event. It
will be older than the Latest Heartbeat if there have been no events
since the most recent heartbeat. Performance Optimization Disable Event Ordering for Burst Operations Consider disabling event ordering if your Trigger fires on a collection that
receives short bursts of events (e.g. inserting data as part of a daily batch
job). Ordered Triggers wait to execute a Function for a particular event until
the Functions of previous events have finished executing. As a
consequence, ordered Triggers are effectively rate-limited by the run
time of each sequential Trigger Function. This may cause a significant
delay between the database event appearing on the change stream and the
Trigger firing. In certain extreme cases, database events might fall off
the oplog before a long-running ordered Trigger processes them. Unordered Triggers execute Functions in parallel if possible, which can be
significantly faster (depending on your use case) but does not guarantee that
multiple executions of a Trigger Function occur in event order. Disable Collection-Level Preimages Document preimages require your cluster to record additional data about
each operation on a collection. Once you enable preimages for any
Trigger on a collection, your cluster stores preimages for every
operation on the collection. The additional storage space and compute overhead may degrade Trigger
performance depending on your cluster configuration. To avoid the storage and compute overhead of preimages, you must disable
preimages for the entire underlying MongoDB collection. This is a
separate setting from any individual Trigger's preimage setting. If you disable collection-level preimages, then no active Trigger on
that collection can use preimages. However, if you delete or disable all
preimage Triggers on a collection, then you can also disable
collection-level preimages. To learn how, see Disable Preimages for a Collection . Use Match Expressions to Limit Trigger Invocations You can limit the number of Trigger invocations by specifying a $match expression in the Match
Expression field. Atlas evaluates the match expression against the
change event document and invokes the Trigger only if the expression evaluates
to true for the given change event. The match expression is a JSON document that specifies the query conditions
using the MongoDB read query syntax . We recommend only using match expressions when the volume of Trigger events
measurably becomes a performance issue. Until then, receive all events and
handle them individually in the Trigger Function code. The exact shape of the change event document depends on the event that caused
the Trigger to fire. For details, see the reference for each event type: insert update replace delete create modify rename drop shardCollection reshardCollection refineCollectionShardKey dropDatabase The following match expression allows the Trigger to fire
only if the change event object specifies that the status field in
a document changed. updateDescription is a field of the update Event object . { "updateDescription.updatedFields.status" : { "$exists" : true } } The following match expression allows the Trigger to fire only when a
document's needsTriggerResponse field is true . The fullDocument field of the insert , update , and replace events represents a document after the
given operation. To receive the fullDocument field, you must enable Full Document in your Trigger configuration. { "fullDocument.needsTriggerResponse" : true } Testing Match Expressions The following procedure shows one way to test whether your match expression
works as expected: Download the MongoDB Shell (mongosh) and use it to connect to your cluster . Replacing DB_NAME with your database name, COLLECTION_NAME with your
collection name, and YOUR_MATCH_EXPRESSION with the match expression you
want to test, paste the following into mongosh to open a change stream on an
existing collection: db. getSiblingDB ( DB_NAME ). COLLECTION_NAME . watch ( [ { $match : YOUR_MATCH_EXPRESSION }]) while ( ! watchCursor. isClosed ( )) { if ( watchCursor. hasNext ( )) { print ( tojson ( watchCursor. next ( ))) ; } } In another terminal window, use mongosh to make changes to some test
documents in the collection. Observe what the change stream filters in and out. Use Project Expressions to Reduce Input Data Size In the Project Expression field,
limit the number of fields that the Trigger processes by using a $project expression. Note Project is inclusive only When using Triggers, a projection expression is inclusive only .
Project does not support mixing inclusions and exclusions.
The project expression must be inclusive because Triggers require you
to include operationType . If you want to exclude a single field, the projection expression must
include every field except the one you want to exclude.
You can only explicitly exclude _id , which is included by default. A Trigger is configured with the following Project Expression : { "_id" : 0 , "operationType" : 1 , "updateDescription.updatedFields.status" : 1 } The change event object that Atlas passes to the Trigger Function
only includes the fields specified in the projection, as in the following
example: { "operationType" : "update" , "updateDescription" : { "updatedFields" : { "status" : "InProgress" } } } Tip See also: Triggers examples on Github. Back Triggers Next Scheduled Triggers
