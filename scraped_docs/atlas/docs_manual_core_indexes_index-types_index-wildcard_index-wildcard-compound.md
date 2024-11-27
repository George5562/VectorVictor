# Compound Wildcard Indexes - MongoDB Manual v8.0


Docs Home / MongoDB Manual / Indexes / Types / Wildcard Compound Wildcard Indexes On this page Use Cases Search Using the Attribute Pattern Behavior General Considerations for Wildcard Indexes Compound Wildcard Index Considerations Get Started Filter Fields with a wildcardProjection Use a Helper Method to Create a Wildcard Index Learn More New in version 7.0 . MongoDB supports creating wildcard indexes on a field or a set of
fields. A compound index has multiple index terms. A compound wildcard
index has one wildcard term and one or more additional index terms. Important Wildcard indexes do not replace workload-based index planning. For more information on creating indexes that support your workload, see Create Indexes to Support Your Queries . Use Cases Search Using the Attribute Pattern The attribute pattern is a useful technique for searching documents that share common
characteristics. Unfortunately, it is expensive to create a lot of individual indexes to
cover all of the possible queries. A wildcard index is a good
alternative to creating a large number of individual indexes because one
wildcard index can efficiently cover many potential queries. Consider a schema like: { tenantId : < Number > , tenantRegion : < Number > , customFields : { addr : < String > , name : < String > , blockId : < Number > , ... } dateOpened : < Date > } You might want to query aspects of the customFields field for
tenants that have a particular tenantId . You could create a series
of individual indexes: { tenantId : 1 , "customFields.addr" : 1 } { tenantId : 1 , "customFields.name" : 1 } { tenantId : 1 , "customFields.blockId" : 1 } ... This approach is difficult to maintain and you are likely to reach the
maximum number of indexes per collection (64). Use a compound wildcard index instead. The compound wildcard index is
easier to write, easier to maintain, and is unlikely to reach the 64
index collection limit. This example creates a compound wildcard index on the salesData collection: db. runCommand ( { createIndexes : "salesData" , indexes : [ { key : { tenantId : 1 , "customFields.$**" : 1 } , name : "tenant_customFields" } ] } ) The wildcard, "customFields.$**" , specifies all of the sub-fields in
the customFields field. The other index term, tenantId , is not a
wildcard specification; it is a standard field specification. Behavior To create wildcard indexes, use a standard index creation command: createIndexes createIndex() createIndexes() General Considerations for Wildcard Indexes Wildcard indexes omit the _id field by default. To include the _id field in a wildcard index, you must explicitly include it in
the wildcardProjection document. db. salesData . createIndex ( { "$**" : 1 } , { "wildcardProjection" : { "_id" : 1 , "customers.lastName" : 1 , "customers.FirstName" : 1 , } } ) You can create more than one wildcard index on a collection. A wildcard index may cover the same fields as other indexes in the
collection. Wildcard indexes are sparse . They only
include entries for documents that contain the indexed field. The document is not indexed if all of the fields in the compound
wildcard index are missing. Compound Wildcard Index Considerations Compound wildcard indexes are sparse indexes. Documents are included in the index if they are missing the wildcard
field but have one of the compound fields. Index fields, including wildcard fields, can be sorted in ascending
( 1 ) or descending ( -1 ) order. Get Started Filter Fields with a wildcardProjection You can use a wildcardProjection to specify individual sub-fields. db. runCommand ( { createIndexes : "salesData" , indexes : [ { key : { tenantId : 1 , "$**" : 1 } , name : "tenant_customFields_projection" , wildcardProjection : { "customFields.addr" : 1 , "customFields.name" : 1 } } ] } ) The wildcard index term, "$**" , specifies every field in the
collection. The wildcardProjection limits the index to the specified
fields, "customFields.addr" and "customFields.name" . You can only use a wildcardProjection when the wildcard term is $** . Use a Helper Method to Create a Wildcard Index MongoDB provides shell helper methods for most database commands . These shell
methods offer a simplified syntax and are functionally equivalent to
the database commands. The shell helper for the first example is: db. salesData . createIndex ( { tenantId : 1 , "customFields.$**" : 1 } , { name : "tenant_customFields_shellHelper" } ) The shell helper for the second example is: db. salesData . createIndex ( { tenantId : 1 , "$**" : 1 } , { "wildcardProjection" : { "customFields.addr" : 1 , "customFields.name" : 1 } , name : "tenant_customFields_projection_helper" } ) If you want to compare the shell commands and the database commands, you
must drop the indexes between command invocations. You cannot create
the same index twice, even with different names. To drop an index, insert the index name and run db.collection.dropIndex() . db. salesData . dropIndex ( "tenant_customFields" ) The preceding command removes the "tenant_customFields" index from
the salesData database. Learn More Behavioral details for wildcard indexes Single wildcard indexes Wildcard text indexes Back Use All Fields Next Reference
