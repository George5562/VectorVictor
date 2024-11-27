# Indexes - MongoDB Manual v8.0


Docs Home / MongoDB Manual Indexes On this page Use Cases Get Started Details Learn More Indexes support efficient execution of queries in MongoDB. Without
indexes, MongoDB must scan every document in a collection to return
query results. If an appropriate index exists for a query, MongoDB uses
the index to limit the number of documents it must scan. Although indexes improve query performance, adding an index has negative
performance impact for write operations. For collections with a high
write-to-read ratio, indexes are expensive because each insert must also
update any indexes. Use Cases If your application is repeatedly running queries on the same fields,
you can create an index on those fields to improve performance. For
example, consider the following scenarios: Scenario Index Type A human resources department often needs to look up employees by
employee ID. You can create an index on the employee ID field to
improve query performance. Single Field Index A salesperson often needs to look up client information by
location. Location is stored in an embedded object with fields
like state , city , and zipcode . You can create an
index on the location object to improve performance for
queries on that object. When you create an index on an embedded document, only queries that
specify the entire embedded document use the index. Queries on a
specific field within the document do not use the index. Single Field Index on an embedded
document A grocery store manager often needs to look up inventory items by
name and quantity to determine which items are low stock. You can
create a single index on both the item and quantity fields to improve query performance. Compound Index Get Started You can create and manage indexes in MongoDB Atlas , with a driver
method, or with the MongoDB Shell. MongoDB Atlas is the fully
managed service for MongoDB deployments in the cloud. Create and Manage Indexes in MongoDB Atlas For deployments hosted in MongoDB Atlas, you can create
and manage indexes with the MongoDB Atlas UI or the Atlas CLI. MongoDB Atlas
also includes a Performance Advisor that recommends indexes to improve
slow queries, ranks suggested indexes by impact, and recommends which
indexes to drop. To learn how to create and manage indexes the MongoDB Atlas UI or the Atlas
CLI, see Create, View, Drop, and Hide Indexes . To learn more about the MongoDB Atlas Performance Advisor, see Monitor and Improve Slow Queries . Create and Manage Indexes with a Driver Method or the MongoDB Shell You can create and manage indexes with a driver method or the MongoDB
Shell. To learn more, see the following resources: Create an Index Create a Compound Index Create an Index on an Array Field Create an Index to Support Geospatial Queries Details Indexes are special data structures that store a small portion of the
collection's data set in an easy-to-traverse form. MongoDB indexes use a B-tree data structure. The index stores the value of a specific field or set of fields, ordered
by the value of the field. The ordering of the index entries supports
efficient equality matches and range-based query operations. In
addition, MongoDB can return sorted results using the ordering in the
index. Restrictions Certain restrictions apply to indexes, such as the length of the index
keys or the number of indexes per collection. For details, see Index Limitations . Default Index MongoDB creates a unique index on the _id field during the creation of a
collection. The _id index prevents clients from inserting two
documents with the same value for the _id field. You cannot drop
this index. Note In sharded clusters , if you do not use
the _id field as the shard key , then your application must ensure the uniqueness of the values in the _id field.
You can do this by using a field with an auto-generated ObjectId . Index Names The default name for an index is the concatenation of the indexed keys
and each key's direction in the index ( 1 or -1 ) using underscores
as a separator. For example, an index created on { item : 1, quantity:
-1 } has the name item_1_quantity_-1 . You cannot rename an index once created. Instead, you must drop and recreate the index with a new name. To learn how to specify the name for an index, see Specify an Index Name . Index Build Performance Applications may encounter reduced performance during index builds,
including limited read/write access to the collection. For more
information on the index build process, see Index Builds on Populated Collections ,
including the Index Builds in Replicated Environments section. Learn More MongoDB provides a number of different index types to support specific
types of data and queries. To learn more, see Index Types . To learn what properties and behaviors you can specify in your index,
see Index Properties . To understand considerations you may need to make when you create an
index, see Indexing Strategies . To learn about the performance impact of indexes, see Operational Factors and Data Models . To learn about query settings and indexes, see setQuerySettings . Back Aggregation Pipeline Next Create
