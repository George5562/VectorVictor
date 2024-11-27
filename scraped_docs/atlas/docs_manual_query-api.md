# MongoDB Query API - MongoDB Manual v8.0


Docs Home / MongoDB Manual / Introduction MongoDB Query API On this page Document Model Data as Code Getting Started The MongoDB Query API is the mechanism that you use to interact with
your data. The Query API comprises two ways to query data in MongoDB: CRUD Operations Aggregation pipelines You can use the Query API to perform: Adhoc queries . Explore your MongoDB data with mongosh , Compass , VSCode or a MongoDB driver . Data transformations . Use aggregation pipelines to
reshape your data and perform calculations. Document join support Use $lookup and $unionWith to combine data from different collections. Graph and geospatial queries . Use operators such as $geoWithin and $geoNear to analyze geospatial
data and $graphLookup for graph data. Full-text search . Use the $search stage to
perform efficient text search on your data. Semantic search . Use the $vectorSearch stage to
perform semantic search on your data. Indexing . Improve your MongoDB query performance by using the correct index type for your data architecture. On-demand materialized views . Use $out and $merge to create materialized views on common queries. Time series analysis . Query and aggregate your time-stamped data
with time series collections . Document Model A document in MongoDB is a data structure composed of field and value
pairs. Documents are stored as BSON which is the binary representation of JSON . This low level of abstraction helps you develop quicker
and reduces the efforts around querying and data modeling. The document
model provides several advantages, including: Documents correspond to native data types in many programming
languages. Embedded documents and arrays reduce need for expensive joins. Flexible schema. Documents do not need to have the same set of fields
and the data type for a field can differ across documents within a
collection. Data as Code The MongoDB Query API supports drivers for major
programming languages. These drivers allow you to make calls to the
database and generate queries using the syntax native to your
application. Getting Started To get started, visit the MongoDB Getting Started Guide . Here you can
find resources, code examples and tutorials that demonstrate the MongoDB Query API . Back Documents Next BSON Types
