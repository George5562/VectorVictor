# Case-Insensitive Indexes - MongoDB Manual v8.0


Docs Home / MongoDB Manual / Indexes / Properties Case-Insensitive Indexes On this page Command Syntax Behavior Examples Create a Case-Insensitive Index Case-Insensitive Indexes on Collections with a Default Collation Case-insensitive indexes support queries that perform string comparisons
without regard for case. Case insensitivity is derived from collation . Important Case-insensitive indexes typically do not improve performance for $regex queries. The $regex implementation is not
collation-aware and cannot utilize case-insensitive indexes efficiently. Command Syntax You can create a case-insensitive index with db.collection.createIndex() by specifying the collation option: db. collection . createIndex ( { < field > : < sortOrder > } , { collation : { locale : < locale > , strength : < 1 | 2 > } } ) To specify a collation for a case-insensitive index, include the
following fields in the collation object: Field Description locale Specifies language rules. For a list of available locales, see Supported Languages and Locales . strength Determines comparison rules. A strength value of 1 or 2
indicates case-insensitive collation. For additional collation fields, see Collation . Behavior To use an index that specifies a collation, query and sort operations
must specify the same collation as the index. If a collection has
defined a collation, all queries and indexes inherit that collation
unless they explicitly specify a different collation. Examples Create a Case-Insensitive Index To use a case-insensitive index on a collection with no default
collation, create an index with a collation and set the strength parameter to 1 or 2 (see Collation for a detailed
description of the strength parameter). You must specify the same
collation at the query level in order to use the index-level collation. The following example creates a collection with no default collation,
then adds an index on the type field with a case-insensitive
collation. db. createCollection ( "fruit" ) db. fruit . createIndex ( { type : 1 } , { collation : { locale : 'en' , strength : 2 } } ) To use the index, queries must specify the same collation. db. fruit . insertMany ( [ { type : "apple" } , { type : "Apple" } , { type : "APPLE" } ] ) db. fruit . find ( { type : "apple" } ) // does not use index, finds one result db. fruit . find ( { type : "apple" } ). collation ( { locale : 'en' , strength : 2 } ) // uses the index, finds three results db. fruit . find ( { type : "apple" } ). collation ( { locale : 'en' , strength : 1 } ) // does not use the index, finds three results Case-Insensitive Indexes on Collections with a Default Collation When you create a collection with a default collation, all the indexes
you create subsequently inherit that collation unless you specify a
different collation. All queries which do not
specify a different collation also inherit the default collation. The following example creates a collection called names with a
default collation, then creates an index on the first_name field. db. createCollection ( "names" , { collation : { locale : 'en_US' , strength : 2 } } ) db. names . createIndex ( { first_name : 1 } ) // inherits the default collation Insert a small collection of names: db. names . insertMany ( [ { first_name : "Betsy" } , { first_name : "BETSY" } , { first_name : "betsy" } ] ) Queries on this collection use the specified collation by default,
and if possible use the index as well. db. names . find ( { first_name : "betsy" } ) // inherits the default collation: { collation: { locale: 'en_US', strength: 2 } } // finds three results The above operation uses the collection's default collation and finds
all three documents. It uses the index on the first_name field for
better performance. It is still possible to perform case sensitive searches on this
collection by specifying a different collation in the query: db. names . find ( { first_name : "betsy" } ). collation ( { locale : 'en_US' } ) // does not use the collection's default collation, finds one result The above operation finds only one document, because it uses a
collation with no strength value specified. It does not use the
collection's default collation or the index. Back Properties Next Hidden
