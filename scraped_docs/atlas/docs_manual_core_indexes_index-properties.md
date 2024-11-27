# Index Properties - MongoDB Manual v8.0


Docs Home / MongoDB Manual / Indexes Index Properties On this page Case-Insensitive Indexes Hidden Indexes Partial Indexes Sparse Indexes TTL Indexes Unique Indexes Index properties affect how the query planner uses an index and how
indexed documents are stored. You can specify index properties as
optional parameters when you create an index. The following sections explain the index properties that you can specify
when building an index. Note Not all index types are compatible with all index properties. Case-Insensitive Indexes Case-insensitive indexes support
queries on strings without considering letter case. Hidden Indexes Hidden indexes are not visible to the query planner and cannot be used
to support a query. You can use hidden indexes to evaluate the potential impact of dropping
an index without actually dropping it. If the impact is negative, you
can unhide the index instead of having to recreate a dropped index.
Hidden indexes are fully maintained and can be used immediately once
unhidden. Partial Indexes Partial indexes only index the documents in
a collection that meet a specified filter expression. Partial indexes
have lower storage requirements and reduced performance costs for index
creation and maintenance. Partial indexes offer a superset of the functionality of sparse indexes
and should be preferred over sparse indexes. Sparse Indexes Sparse indexes only contain entries for
documents that have the indexed field. These indexes skip documents that
do not have the indexed field. TTL Indexes TTL indexes automatically remove documents
from a collection after a certain amount of time. Use these indexes for
data that only needs to persist for a finite amount of time, like
machine generated event data, logs, and session information. Unique Indexes Unique indexes cause MongoDB to reject
duplicate values for the indexed field. These indexes are useful when
your documents contain a unique identifier, such as a userId . Back Create Next Case-Insensitive
