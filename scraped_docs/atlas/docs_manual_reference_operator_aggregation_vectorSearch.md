# $vectorSearch (aggregation) - MongoDB Manual v8.0


Docs Home / MongoDB Manual / Aggregation Operations / Reference / Stages $vectorSearch (aggregation) $vectorSearch performs a semantic search on data in your Atlas
cluster. If you store vector embeddings that are less than or equal to
4096 dimensions in width for any kind of data along with other data in
your collection on the Atlas cluster, you can seamlessly index the
vector data along with your other data. You can then use the $vectorSearch stage to pre-filter your data and perform
semantic search against the indexed fields. Important The $vectorSearch aggregation pipeline stage is only available
for collections hosted on MongoDB Atlas cluster tiers
running MongoDB version 6.0.11 or later. To learn more, see Atlas Vector Search . Note You cannot use a $vectorSearch stage in a $facet stage. Learn More To learn more about creating Atlas Vector Search indexes, see Index Vector Embeddings . To learn more about $vectorSearch pipeline stage syntax
and usage, see Vector Search Queries . Back $unwind Next Operators
