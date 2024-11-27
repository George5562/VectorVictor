# Compound Indexes - MongoDB Manual v8.0


Docs Home / MongoDB Manual / Indexes / Types Compound Indexes On this page Use Cases Get Started Details Field Limit Field Order Sort Order Hashed Index Fields Index Prefixes Sparse Compound Indexes Learn More Compound indexes collect and sort data from two or more fields in each
document in a collection. Data is grouped by the first field in the
index and then by each subsequent field. For example, the following image shows a compound index where documents
are first grouped by userid in ascending order (alphabetically).
Then, the scores for each userid are sorted in descending order: Indexing commonly queried fields increases the
likelihood of covered queries . A
covered query is a query that can be satisfied entirely using an index
and does not have to examine any documents, leading to greatly improved performance. To create a compound index, use the following prototype: db. < collection > . createIndex ( { < field1 > : < sortOrder > , < field2 > : < sortOrder > , ... < fieldN > : < sortOrder > } ) You can create and manage compound indexes in the UI for deployments hosted in MongoDB Atlas . Use Cases If your application repeatedly runs a query that contains multiple
fields, you can create a compound index to improve performance for that
query. For example, a grocery store manager often needs to look up
inventory items by name and quantity to determine which items are low
stock. You can create a compound index on both the item and quantity fields to improve query performance. A compound index on commonly queried fields increases the chances of covering those queries. Covered queries
are queries that can be satisfied entirely using an index, without
examining any documents. This optimizes query performance. Get Started To create a compound index, see Create a Compound Index . Details This section describes technical details and limitations for compound
indexes. Field Limit A single compound index can contain up to 32 fields. Field Order The order of the indexed fields impacts the effectiveness of a compound
index. Compound indexes contain references to documents according to the
order of the fields in the index. To create efficient compound indexes,
follow the ESR (Equality, Sort, Range) rule . Sort Order Indexes store references to fields in either ascending ( 1 ) or
descending ( -1 ) sort order. For compound indexes, sort order can
determine whether the index supports a sort operation. For more
information, see Compound Index Sort Order . Hashed Index Fields Compound indexes may contain a single hashed index field . Index Prefixes Index prefixes are the beginning subsets of indexed fields. Compound
indexes support queries on all fields included in the index prefix. For example, consider this compound index: { "item" : 1 , "location" : 1 , "stock" : 1 } The index has these index prefixes: { item: 1 } { item: 1, location: 1 } MongoDB can use the compound index to support queries on these field
combinations: item item and location item , location , and stock MongoDB can also use the index to support a query on the item and stock fields, since the item field corresponds to a prefix.
However, only the item field in the index can support this query.
The query cannot use the stock field which follows location . Index fields are parsed in order; if a query omits an index prefix, it
is unable to use any index fields that follow that prefix. MongoDB cannot use the compound index to support queries on these
field combinations: location stock location and stock Without the item field, none of the preceding field combinations
correspond to a prefix index. Tip Remove Redundant Indexes If you have a collection that has both a compound index and an index on
its prefix (for example, { a: 1, b: 1 } and { a: 1 } ), if
neither index has a sparse or unique constraint, you can remove the index on the prefix
( { a: 1 } ). MongoDB uses the compound index in all of the situations
that it would have used the prefix index. Sparse Compound Indexes Compound indexes can contain different types of sparse indexes. The
combination of index types determines how the compound index matches
documents. This table summarizes the behavior of a compound index that contains
different types of sparse indexes: Compound Index Components Compound Index Behavior Ascending indexes Descending indexes Only indexes documents that contain a value for at least one of
the keys. Ascending indexes Descending indexes Geospatial indexes Only indexes a document when it contains a value for one of
the geospatial fields. Does not index documents in the
ascending or descending indexes. Ascending indexes Descending indexes Text indexes Only indexes a document when it matches one of the text fields. Does not index documents in the ascending or descending
indexes. Learn More To learn how to create efficient compound indexes, see The ESR (Equality, Sort, Range) Rule . Back Embedded Documents Next Create
