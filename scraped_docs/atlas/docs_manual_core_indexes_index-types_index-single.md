# Single Field Indexes - MongoDB Manual v8.0


Docs Home / MongoDB Manual / Indexes / Types Single Field Indexes On this page Use Cases Get Started Single field indexes store information from a single field in a
collection. By default, all collections have an index on the _id
field . You can add additional indexes to speed up
important queries and operations. You can create a single-field index on any field in a document,
including: Top-level document fields Embedded documents Fields within embedded documents When you create an index, you specify: The field on which to create the index. The sort order for the indexed values (ascending or descending). A sort order of 1 sorts values in ascending order. A sort order of -1 sorts values in descending order. Important Using a descending single-field index may negatively impact index
performance. For best performance, only use ascending single-field
indexes. To create a single-field index, use the following prototype: db. < collection > . createIndex ( { < field > : 1 } ) This image shows an ascending index on a single field, score : In this example, each document in the collection that has a value for
the score field is added to the index in ascending order. You can create and manage single field indexes in the UI for deployments hosted in MongoDB Atlas . Use Cases If your application repeatedly runs queries on the same field, you can
create an index on that field to improve performance. For example, your
human resources department often needs to look up employees by employee
ID. You can create an index on the employee ID field to improve the
performance of that query. Indexing commonly queried fields increases the chances of covering those queries. Covered queries are queries
that can be satisfied entirely using an index, without examining any
documents. This optimizes query performance. Get Started To create an index on a single field, see these examples: Create an Index on a Single Field Create an Index on an Embedded Field Create an Index on an Embedded Document Back Types Next Create
