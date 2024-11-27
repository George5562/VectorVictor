# Introduction to MongoDB - MongoDB Manual v8.0


Docs Home / MongoDB Manual Introduction to MongoDB On this page Document Database Key Features You can create a MongoDB database in the following environments: MongoDB Atlas : The fully
managed service for MongoDB deployments in the cloud MongoDB Enterprise : The
subscription-based, self-managed version of MongoDB MongoDB Community : The
source-available, free-to-use, and self-managed version of MongoDB To learn more about creating a MongoDB database with the Atlas UI,
see Get Started with Atlas . Document Database A record in MongoDB is a document, which is a data structure composed
of field and value pairs. MongoDB documents are similar to JSON
objects. The values of fields may include other documents, arrays,
and arrays of documents. The advantages of using documents are: Documents correspond to native data types in many programming
languages. Embedded documents and arrays reduce need for expensive joins. Dynamic schema supports fluent polymorphism. Collections/Views/On-Demand Materialized Views MongoDB stores documents in collections .
Collections are analogous to tables in relational databases. In addition to collections, MongoDB supports: Read-only Views On-Demand Materialized Views Key Features High Performance MongoDB provides high performance data persistence. In particular, Support for embedded data models reduces I/O activity on database
system. Indexes support faster queries and can include keys from embedded
documents and arrays. Query API The MongoDB Query API supports read and write
operations (CRUD) as well as: Data Aggregation Text Search and Geospatial Queries . Tip See also: SQL to MongoDB Mapping Chart SQL to Aggregation Mapping Chart High Availability MongoDB's replication facility, called replica set , provides: automatic failover data redundancy. A replica set is a group of
MongoDB servers that maintain the same data set, providing redundancy
and increasing data availability. Horizontal Scalability MongoDB provides horizontal scalability as part of its core functionality: Sharding distributes data across a
cluster of machines. Starting in 3.4, MongoDB supports creating zones of data based on the shard key . In a
balanced cluster, MongoDB directs reads and writes covered by a zone
only to those shards inside the zone. See the Zones manual page for more information. Support for Multiple Storage Engines MongoDB supports multiple storage engines : WiredTiger Storage Engine (including support for Encryption at Rest ) In-Memory Storage Engine for Self-Managed Deployments . In addition, MongoDB provides pluggable storage engine API that allows
third parties to develop storage engines for MongoDB. Back What is MongoDB? Next Get Started
