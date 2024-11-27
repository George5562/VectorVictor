# Index Types - MongoDB Manual v8.0


Docs Home / MongoDB Manual / Indexes Index Types On this page Single Field Index Compound Index Multikey Index Geospatial Index Text Index Hashed Index Clustered Index This page describes the types of indexes you can create in MongoDB.
Different index types support different types of data and queries. Single Field Index Single field indexes collect and sort data from a single field in each
document in a collection. This image shows an index on a single field, score : To learn more, see Single Field Indexes . Compound Index Compound indexes collect and sort data from two or more fields in each
document in a collection. Data is grouped by the first field in the
index and then by each subsequent field. For example, the following image shows a compound index where documents
are first grouped by userid in ascending order (alphabetically).
Then, the scores for each userid are sorted in descending order: To learn more, see Compound Indexes . Multikey Index Multikey indexes collect and sort data stored in arrays. You do not need to explicitly specify the multikey type. When you create
an index on a field that contains an array value, MongoDB automatically
sets the index to be a multikey index. This image shows a multikey index on the addr.zip field: To learn more, see Multikey Indexes . Geospatial Index Geospatial indexes improve performance for queries on geospatial
coordinate data. To learn more, see Geospatial Indexes . MongoDB provides two types of geospatial indexes: 2d indexes that use planar geometry to return
results. 2dsphere indexes that use spherical geometry
to return results. Text Index Text indexes support text search queries on fields containing string content. To learn more, see Text Indexes on Self-Managed Deployments . Note Use Atlas Search or Atlas Vector Search on Atlas Deployments For data hosted on MongoDB Atlas , MongoDB offers the
following text search solutions: Atlas Search provides improved performance
and functionality compared to on-premises text search. Atlas Vector Search provides vector search capabilities to perform semantic, hybrid, and generative
search. Hashed Index Hashed indexes support hashed sharding . Hashed indexes index the hash of the value
of a field. To learn more, see Hashed Indexes . Clustered Index New in version 5.3 . Clustered indexes specify the order in which clustered collections store data. Collections created with a
clustered index are called clustered collections. To learn how to create a collection with a clustered index, see Clustered Collection Examples . Back Drop Next Single Field
