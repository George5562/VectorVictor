# 2dsphere Index Versions - MongoDB Manual v8.0


Docs Home / MongoDB Manual / Indexes / Types / Geospatial / 2dsphere 2dsphere Index Versions On this page Change Index Version 2dsphere indexes are available in the following versions: 2dsphere Index Version Description Version 3 MongoDB 3.2 introduces version 3 of 2dsphere indexes.
Version 3 is the default version for 2dsphere indexes created
in MongoDB 3.2 and later. Version 2 MongoDB 2.6 introduces version 2 of 2dsphere indexes.
Version 2 is the default version for 2dsphere indexes created
in MongoDB 2.6 to 3.0. Version 1 MongoDB 2.4 introduces version 1 of 2dsphere indexes.
MongoDB 2.4 only supports version 1. Change Index Version Important Always use the default index version when possible. Only override the
default version if required for compatibility reasons. To override the default version and specify a different version for your
2dsphere index, set the 2dsphereIndexVersion option when you create
an index: db. < collection > . createIndex ( { < field > : "2dsphere" } , { "2dsphereIndexVersion" : < version > } ) Example The following command creates a version 2 2dsphere index on the address field: db. test . createIndex ( { "address" : "2dsphere" } , { "2dsphereIndexVersion" : 2 } ) Back Circle in a Sphere Next 2d
