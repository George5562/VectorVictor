# Create, View, Drop, and Hide Indexes - MongoDB Atlas


Docs Home / MongoDB Atlas / Interact with Data Create, View, Drop, and Hide Indexes On this page Required Roles Considerations View Indexes Create an Index Drop an Index Hide an Index You can use the Atlas CLI or the Atlas UI to manage indexes on your collections. Indexes support the efficient execution of queries in MongoDB and should
be considered for fields which your application reads often. To learn
more about creating effective indexes, see Indexing Strategies . You can enable auto-creation of indexes for a
Serverless instance. To learn more,
see Auto-Create Indexes for Serverless Instances . Required Roles To create , drop , or hide indexes,
you must have access provided by at least one of the following roles: Project Owner or Organization Owner Project Data Access Admin Considerations By default, you can have up to three concurrent index builds. To learn
more, see Maximum Concurrent Index Builds . When you initiate a rolling index build, the node will be in HOST_DOWN state for the duration of the build. To cancel a rolling index build, you must contact MongoDB support . View Indexes To view index information for a collection: 1 In Atlas , go to the Clusters page for your project. If it's not already displayed, select the organization that
contains your desired project from the Organizations menu in the
navigation bar. If it's not already displayed, select your desired project
from the Projects menu in the navigation bar. If it's not already displayed, click Clusters in the
sidebar. The Clusters page displays. 2 Go to the Collections page. Click the Browse Collections button for your cluster. The Data Explorer displays. 3 Select the database for the collection. The main panel and Namespaces on the left side list the
collections in the database. click to enlarge 4 Select the collection on the left-hand side or in the main panel. The main panel displays the Find , Indexes ,
and Aggregation views. 5 Select the Indexes view. The indexes table lists the indexes and associated index information
for the collection. Index information includes the index definition,
the size, and the usage frequency. click to enlarge Create an Index Tip When you create indexes, keep the ratio of reads to writes on the
target collection in mind. Indexes come with a performance cost, but
are more than worth the cost for frequent queries on large data sets.
Before you create an index, review the documented indexing strategies . Note You can build full-text search with Atlas Search and semantic search with Atlas Vector Search . Atlas Search offers fine-grained text indexing. To learn
more, see Review Atlas Search Index Syntax and How to Index Fields for Vector Search . Atlas CLI Atlas UI To create a rolling index for your Atlas cluster using the
Atlas CLI, run the following command: atlas clusters indexes create [indexName] [options] To learn more about the command syntax and parameters, see the
Atlas CLI documentation for atlas clusters indexes create . Tip See: Related Links Install the Atlas CLI Connect to the Atlas CLI To create an index for a collection by using the Atlas UI: 1 Click the Indexes tab. Select the collection you wish to index, and go to the Indexes tab. 2 Click Create Index . In the Create Index modal, enter the index key specification document: { < field1 > : < index type > , ... } Example To create a compound index on the fields category (ascending order) and score (descending order), specify the
index specification document: { category : 1 , score : - 1 } To learn more about indexes, see Indexes . 3 (Optional) Specify the index options . When you create an index, you can specify a variety of index options . Examples: For partial indexes , specify the partialFilterExpression option . For sparse indexes , specify the sparse option . For TTL indexes , specify the expireAfterSeconds option . For 2d Indexes , specify the options for 2d Indexes { < option1 > : < value1 > , ... } Example The following options document specifies the unique option and
the name for the index: { unique : true , name : "myUniqueIndex" } Note You cannot perform a rolling build for a unique index. If you
enable building indexes in a rolling fashion with the unique index option, Atlas rejects your configuration
with an error message. 4 (Optional) Set the Collation options. Use collation to specify language-specific rules for string comparison,
such as rules for lettercase and accent marks. The collation document contains a locale field which indicates the ICU Locale code , and may contain other
fields to define collation behavior. Example The following collation option document specifies a locale value
of fr for a French language collation: { "locale" : "fr" } To review the list of locales that MongoDB collation supports, see
the list of languages and locales . To learn more about collation
options, including which are enabled by default for each locale, see Collation in the MongoDB manual. 5 (Optional) Enable building indexes in a rolling fashion. Important Rolling index builds succeed only when they meet certain conditions.
To ensure your index build succeeds, avoid the following design
patterns that commonly trigger a restart loop: Index key exceeds the index key limit Index name already exists Index on more than one array field Index on collection that has the maximum number of text indexes Text index on collection that has the maximum number of text indexes Note the Atlas UI doesn't support building indexes with a rolling
build for M0 Free clusters and M2/M5 Shared clusters. You can't build indexes with a rolling build
for Serverless instances. For workloads which cannot tolerate performance decrease due to index
builds, consider building indexes in a rolling fashion. To maintain cluster availability: Atlas removes one node from the cluster at a time
starting with a secondary . More than one node can go down at a time, but Atlas always keeps
a majority of the nodes online. Atlas automatically cancels rolling index builds
that don't succeed on all nodes. When a rolling index build completes
on some nodes, but fails on others, Atlas cancels the build
and removes the index from any nodes that it was successfully built on. In the event of a rolling index build cancellation, Atlas generates an activity feed event and sends a notification email to the project owner
with the following information: Name of the cluster on which the rolling index build failed Namespace on which the rolling index build failed Project that contains the cluster and namespace Organization that contains the project Link to the activity feed event To learn more about rebuilding indexes, see Build Indexes on
Replica Sets . Note Unique index options are
incompatible with building indexes in a rolling fashion. If you specify unique in the Options pane, Atlas rejects your configuration with an error message. 6 Click Create . 7 In the Confirm Operation modal, confirm your index. Drop an Index To drop an index from a collection by using the Atlas UI: 1 In Atlas , go to the Clusters page for your project. If it's not already displayed, select the organization that
contains your desired project from the Organizations menu in the
navigation bar. If it's not already displayed, select your desired project
from the Projects menu in the navigation bar. If it's not already displayed, click Clusters in the
sidebar. The Clusters page displays. 2 Go to the Collections page. Click the Browse Collections button for your cluster. The Data Explorer displays. 3 Go to the Indexes tab. Select the collection with the index that you want to drop. Click the Indexes tab. 4 Drop the index. Under the Action column, click the Drop Index icon for the index that you want to drop. 5 Confirm action. In the dialog box, type the name of the index
and click Drop . Important You can't delete or hide the _id index. To learn more, see Unique Indexes . Consider hiding the index to evaluate the impact of dropping an index before you
drop it. To learn more, see Hidden Indexes . Note Atlas CLI Limitation You can't drop a cluster's index by using the Atlas CLI. Hide an Index To hide an index by using the Atlas UI: 1 In Atlas , go to the Clusters page for your project. If it's not already displayed, select the organization that
contains your desired project from the Organizations menu in the
navigation bar. If it's not already displayed, select your desired project
from the Projects menu in the navigation bar. If it's not already displayed, click Clusters in the
sidebar. The Clusters page displays. 2 Go to the Collections page. Click the Browse Collections button for your cluster. The Data Explorer displays. 3 Go to the Indexes tab. Select the collection with the index that you want to hide. Click the Indexes tab. 4 Hide the index. Under the Action column, click the Hide Index icon for the index that you want to hide. 5 Confirm action. In the dialog box, click Confirm . Note To unhide the index, click the icon again and click Confirm to confirm your action. Back Documents Next Aggregation Pipelines
